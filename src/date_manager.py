from datetime import date, timedelta

class DateManager:

    def __init__(self,start_date=None,end_date=None,period=None):
        if period != None:
            days_per_year = 365
            self.last_date = (date.today()-timedelta(days=1))
            if "d" in period:
                factor = 1/365
                period = period.replace("d","")
                period = int(period)
                self.interval = "1m"
            elif "mo" in period:
                factor = 1/12
                period = period.replace("mo","")
                period = int(period)
                self.interval = "1h"
            elif "y" in period:
                factor = 1
                period = period.replace("y","")
                period = int(period)
                if period > 2:
                    self.interval = "1d"
                else:
                    self.interval = "1h"
            else:
                print("Error :"+period+" is a not supported format")
                print("Please visit https://github.com/d-graz/yfinance-wrapper for more information")
                sys.exit(-1)
            self.days_to_dowload = round(days_per_year*factor*period) - 1
            self.first_date = (date.today()-timedelta(days=self.days_to_dowload))
        else:
            self.first_date = datetime.strptime(start_date, '%Y-%m-%d')
            self.last_date = datetime.strptime(end_date, '%Y-%m-%d')
            two_months = (date.today()-timedelta(days=60))
            two_years = (date.today()-timedelta(days=730))
            if self.first_date < two_months:
                if self.first_date < two_years:
                    self.interval = "1d"
                else:
                    self.interval = "1h"
            else:
                self.interval = "1m"
    
    def calculate_time_span(self):
        results = []
        if self.interval == "1m":
            day_steps = True
            if self.days_to_dowload < 6:
                day_steps = False
            date1 = self.first_date
            date2 = (date1+timedelta(days=5))
            while day_steps:
                data = []
                data.append(date1.isoformat())
                data.append(date2.isoformat())
                results.append(data)
                date1 = date2
                date2 = (date1+timedelta(days=5))
                self.days_to_dowload = self.days_to_dowload - 5
                if self.days_to_dowload < 6:
                    day_steps = False
            if self.days_to_dowload > 0:
                data = []
                data.append(date1.isoformat())
                data.append(self.last_date.isoformat())
                results.append(data)
        else:
            data = []
            data.append(self.first_date)
            data.append(self.last_date)
            results.append(data)
        print("printing result for debug")
        print(results)
        print("done")
        return results
            

#dm = DateManager(period="8d")
#r = dm.calculate_time_span()
#print("printing results")
#print(r)
#print("done")
            
