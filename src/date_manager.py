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
            elif "mo" in period:
                factor = 1/12
                period = period.replace("mo","")
                period = int(period)
            elif "y" in period:
                factor = 1
                period = period.replace("y","")
                period = int(period)
            self.days_to_dowload = round(days_per_year*factor*period)
            self.first_date = (date.today()-timedelta(days=self.days_to_dowload))
        else:
            self.first_date = datetime.strptime(start_date, '%Y-%m-%d')
            self.last_date = datetime.strptime(end_date, '%Y-%m-%d')
    
    def calculate_time_span(self):
        results = []
        six_day_step = True
        if self.days_to_dowload < 6:
            six_day_step = False
        date1 = self.first_date
        date2 = (date1+timedelta(days=5))
        while six_day_step:
            data = []
            data.append(date1.isoformat())
            data.append(date2.isoformat())
            results.append(data)
            date1 = (date2+timedelta(days=1))
            date2 = (date1+timedelta(days=5))
            self.days_to_dowload = self.days_to_dowload - 6
            if self.days_to_dowload < 6:
                six_day_step = False
        data = []
        data.append(date1.isoformat())
        data.append(self.last_date.isoformat())
        results.append(data)
        return results

#dm = DateManager(period="8d")
#r = dm.calculate_time_span()
#print("printing results")
#print(r)
#print("done")
            
