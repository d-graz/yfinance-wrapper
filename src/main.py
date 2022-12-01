###############################
# Example of usage of library #
###############################

# library import
from data_manager import DataManager

dataManager = DataManager()

#load tickers from file
dataManager.load(filename="../tickers/tickers_file.txt",format="vertical")

#download ticker from yahoo finance (using yfinance)
dataManager.create(period="2y")

