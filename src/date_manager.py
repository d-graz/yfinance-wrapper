from datetime import date, timedelta

class DateManager:

    def __init__(self,start_date=None,end_date,period=None):
        if period != None:
            days_per_year = 365
            self.last_date = (date.today()-timedelta(days=1)).isoformat()
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
            self.first_date = (date.today()-timedelta(days=days_per_year*factor*period)).isoformat()
        else:
            self.first_date = datetime.strptime(start_date, '%Y-%m-%d')
            self.last_date = datetime.strptime(end_date, '%Y-%m-%d')
            self.first_date = self.first_date.isoformat()
            self.last_date = self.last_date.isoformat()
    
    def calculate_time_span(self):
        six_day_step = True
        one_day_step = True
        if abs(self.last_date +self.first_date) < 6:
            six_day_step = False
        while six_day_step:
            
