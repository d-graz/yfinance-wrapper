# yfinance-wrapper
Tool to manage .csv historic files through yfinance
### Legal disclaimer
- Yahoo!, Y!Finance, and Yahoo! finance are registered trademarks of Yahoo, Inc. Please see their term of use and remember that Yahoo finance API are meant for personal use only
- yfinance library is under Apache 2.0 license
### Table of content
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Credits](#credits)

## Introduction <a name="introduction"></a>
When operating in almost every sector of AI the importance of a well organized and homogeneous dataset is huge, and AlgoTrading is no different. This project is a very basic attempt to organize data gained from Yahoo-finance throught yfinance library. The aim of the tool is to obtain the most granular data available on Yahoo-finance for a given set of tickers and a given period with a really few lines of python code. The output of the tool is a set of `.csv` file (one per ticker), so afterward import is easy.

## Installation <a name="installation"></a>
Simply run `pip install yfinance --upgrade --no-cache-dir` to install yfinance library

## Usage <a name="usage"></a>
The tool offers 2 main calls:
```
# loads the tickers into the program
def load(self,tickers=None,filename=None,format=None):
```
|param|type|info|
|-----|:--:|----|
|`self` |class| default parametes for class (you shuod ignore it)|
|`tickers`|array/ collection of string|array which contains tickers. Can be used instead of using `filename` and `format`|
|`filename`|string|path to a file which contains a list of tickers. **Must be used with** `format` param|
|`format`|string=`vertical`/`horizontal`/`comma`|string attribute , **used in combination with** `filename`,which represent the formatting of the file. `vertical` means that for every line a single ticker is present meanwhile `horizontal` and `comma` means that all the tickers are on 1 single line, separated by a space(`horizontal` formatting) or by a comma (`comma` formatting)|

Please see `src/main.py` for an example of usage.

## Credits <a name="credits"></a>
Special thanks to:
- https://github.com/ranaroussi/yfinance $\rightarrow$ yfinance library
- https://github.com/ricbrea/Yahoo-Finance-Project $\rightarrow$ list of tickers (`tickers/tickers_file.txt`)
