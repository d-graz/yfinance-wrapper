import yfinance as yf
import sys

from date_manager import DateManager
import linux_cmd as lcmd

class DataManager:

    def __init__(self):
        self.dir = "data"
        self.start_date = None
        self.end_date = None
        self.period = None
        self.db = []
        self.tickers = []
        lcmd.mkdir(self.dir)
        output = lcmd.ls(self.dir)
        for element in output:
            if "__part__" in element and ".csv" in element:
                print("Download part founded (probably due to hard stop of the program).")
                print("Unfortunately at the moment the program is not able to recovery the previos job.")
                print("Please remove them and execute again.")
                print("TIP: you can run 'rm *__part__*' to remove all files")
                sys.exit(-1)
            elif ".csv" in element:
                string = element.replace(".csv","")
                self.db.append(string)

    def load(self,tickers=None,filename=None,format=None):
        self.tickers = []
        if tickers==None and (filename==None or format==None):
            print("Argument error :")
            print("Please specify tickers whith a string or a filename and a format")
            help()
        if tickers != None:
            self.tickers = tickers.split(" ")
        else:
            tickers_file = open(filename,"r")
            lines = tickers_file.readlines()
            if format == "vertical":
                for line in lines:
                    string = line.replace("\n","")
                    if string != "":
                        self.tickers.append(string)
            elif format == "horizontal":
                string = lines[0].replace("\n","")
                self.tickers = string.split(" ")
            elif format == "comma":
                string = lines[0].replace("\n","")
                self.tickers = string.split(",")
            else:
                print("Error : format "+format+" not recognized")
                print("Available formats are : vertical, horizontal, comma")
                help()

    def create(self,start_date=None,end_date=None,period=None):
        if len(self.tickers) == 0:
            print("Error : no tickers have been loaded. Please load them using 'load()' method")                
            help()
        if period == None and (start_date == None or end_date == None):
            print("Error : please specify a period or a start and end date")
            help()
        if period != None:
            dateManager = DateManager(period=period)
        else:
            dateManager = DateManager(start_date=start_date,end_date=end_date)
        counter = 1
        time_span = dateManager.calculate_time_span()
        print("DEBUG : printing obtained date_span")
        print(time_span)
        print("DEBUG ENDS")
        for ticker in self.tickers:
            self.download(ticker,time_span,dateManager.interval)
            print(str(counter)+" out of "+str(len(self.tickers))+" downloaded")
            counter = counter + 1
    
    def download(self,ticker,date_span,interval):
        if len(date_span) > 1:
            count = 1
            for date in date_span:
                filename = self.dir+"/"+ticker+"__part__"+str(count)+".csv"
                if interval == "1m" or interval == "1h":
                    data = yf.download(ticker,start=date[0],end=date[1],interval=interval,ignore_tz = False)
                else:
                    data = yf.download(ticker,start=date[0],end=date[1],interval=interval)
                data.to_csv(filename)
                count = count + 1
            partial_files = []
            string = ticker+"__part__"
            output = lcmd.ls(self.dir)
            for element in output:
                if string in element:
                    partial_files.append(element)
            final_filename = self.dir+"/"+ticker+".csv"
            final_file = open(final_filename,"w")
            first = True
            for element in partial_files:
                partial_file_filename = self.dir+"/"+element
                partial_file = open(partial_file_filename,"r")
                lines = partial_file.readlines()
                if first == False:
                    lines.pop(0)
                else:
                    first = False
                final_file.writelines(lines)
                partial_file.close()
                lcmd.rm(file=partial_file_filename)
            final_file.close()
        else:
            filename = self.dir+"/"+ticker+".csv"
            if interval == "1m" or interval == "1h":
                    data = yf.download(ticker,start=date_span[0][0],end=date_span[0][1],interval=interval,ignore_tz = False)
            else:
                data = yf.download(ticker,start=date_span[0][0],end=date_span[0][1],interval=interval)
            data.to_csv(filename)



def help():
    print("Please visit https://github.com/d-graz/yfinance-wrapper for more information")
    sys.exit(-1)


