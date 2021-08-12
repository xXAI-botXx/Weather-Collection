import csv
from datetime import datetime as dt

from wheather_bot import Wheather_Bot

class Collector(object):

    REAL_FIELDS = ['time', 'date', 'real_temperature', 'real_wind_mean', 'real_wind_gusts',
              'real_wind_direction', 'real_weather_state', 'real_visibility']

    PRED_FIELDS = []

    def __init__(self):
        self.bot = Wheather_Bot()
   
    def run(self):
       real_data, pred_data = self.bot.run()
       self.save_real(real_data)
       self.save_pred(pred_data)
       self.write_log("New Wheather Data Entry was collected.")

    def save_real(self, new_entry:dict):
        with open('DATA/freiburg_real_weather_data.csv', 'a') as csv_file:  
            writer = csv.DictWriter(csv_file, fieldnames=Collector.REAL_FIELDS)
            #writer.writeheader()
            writer.writerow(new_entry)

    def save_pred(self, new_entry:dict):
        with open('DATA/freiburg_pred_weather_data.csv', 'a') as csv_file:  
            writer = csv.DictWriter(csv_file, fieldnames=Collector.PRED_FIELDS)
            #writer.writeheader()
            writer.writerow(new_entry)

    def create_backup(self):
        pass

    def write_log(self, txt:str):
        now = dt.now()
        with open('DATA/log.txt', 'a') as f:
            f.write(f"- {now}   {txt}")
    