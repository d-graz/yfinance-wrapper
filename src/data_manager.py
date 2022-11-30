import yfinance as yf
import subprocess
import sys

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

    def create(self,start_date=None,end_date,period=None):
        if len(self.tickers) == 0:
            print("Error : no tickers have been loaded. Please load them using 'load()' method")                
            help()
        

def help():
    print("Please visit https://github.com/d-graz/yfinance-wrapper for more information")
    sys.exit(-1)

prova = DataManager()
