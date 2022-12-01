import yfinance as yf
import subprocess
import sys

from date_manager import DateManager

class DataManager:

    def __init__(self):
        self.dir = "data"
        self.start_date = None
        self.end_date = None
        self.period = None
        self.db = []
        self.tickers = []
        subprocess.run(["mkdir", "-p", self.dir], stdout=subprocess.PIPE, text=True)
        output = subprocess.run(["ls", "-l", self.dir], stdout=subprocess.PIPE, text=True)
        output = str(output.stdout)
        output = output.split("\n")
        output.pop(len(output)-1)
        output.pop(0)
        ar = []
        for element in output:
            obj = element.split(" ")
            for i in range(len(obj)-1):
                obj.pop(0)
            string = obj[0]
            ar.append(string)
        for element in ar:
            if "__part__" in element and ".csv" in element:
                print("Download part founded (probably due to hard stop of the program).")
                print("Unfortunately at the moment the program is not able to recovery the previos job.")
                print("Please remove them and execute again.")
                print("TIP: you can run 'rm *__part__*' to remove all files")
                sys.exit(-1)
            elif ".csv" in element:
                string = element.replace(".csv","")
                self.db.append(string)
        print(self.db)

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
        for ticker in self.tickers:
            self.download(ticker,dateManager.calculate_time_span(),dateManager.interval)
    
    def download(self,ticker,date_span,interval):
        count = 1
        for date in date_span:
            filename = self.dir+"/"+ticker+"__part__"+str(count)+".csv"
            data = yf.download(ticker,start=date[0],end=date[1],interval=interval,ignore_tz = False)
            data.to_csv(filename)
            count = count + 1
        if interval == "1m":
            partial_files = []
            string = ticker+"__part__"
            output = subprocess.run(["ls", "-l", self.dir], stdout=subprocess.PIPE, text=True)
            output = str(output.stdout)
            output = output.split("\n")
            output.pop(len(output)-1)
            output.pop(0)
            for element in output:
                obj = element.split(" ")
                for i in range(len(obj)-1):
                    obj.pop(0)
                if string in obj[0]:
                    partial_files.append(obj[0])
            filename = self.dir+"/"+ticker+".csv"
            total_file = open(filename,"w")
            for partial_file in partial_files:
                partial_file_filename = self.dir+"/"+partial_file
                partial_file_file = open(partial_file_filename,"r")
                lines = partial_file_file.readlines()
                total_file.writelines(lines)
                partial_file_file.close()
                subprocess.run(["rm", partial_file_filename], stdout=subprocess.PIPE, text=True)
            total_file.close()


def help():
    print("Please visit https://github.com/d-graz/yfinance-wrapper for more information")
    sys.exit(-1)

objDataManager = DataManager()
objDateManager = DateManager(period="25d")
objDataManager.download("AAPL",objDateManager.calculate_time_span(),objDateManager.interval)
