import csv
import os
from datetime import datetime as dt

from weather_bot import Weather_Bot

class Collector(object):

    REAL_FIELDS = ['hour', 'minute', 'date', 'real_temperature', 'real_dew_point', 'real_humidity',
                   'real_weather_state', 'real_visibility', 'real_rainfall', 
                   'real_air_pressure', 'real_wind', 'real_wind_gusts', 'real_wind_direction']

    PRED_FIELDS = []

    def __init__(self):
        self.bot = Weather_Bot()
   
    def run(self):
       real_data, pred_data = self.bot.run()
       self.save_real(real_data)
       #self.save_pred(pred_data)
       self.write_log("\nNew Wheather Data Entry was collected.\n")

    # entferne die letzte Zeile -> es soll nur eine letzte Zeile geben
    def save_real_alt(self, new_entry:dict):
        with open('Freiburg/DATA/freiburg_real_weather_data.csv', 'a') as csv_file:  
            writer = csv.DictWriter(csv_file, fieldnames=Collector.REAL_FIELDS)
            #writer.writeheader()
            writer.writerow(new_entry)
            self.remove_last_line('Freiburg/DATA/freiburg_real_weather_data.csv')

    def save_real(self, new_entry:dict):
        with open('Freiburg/DATA/freiburg_real_weather_data.csv', 'r') as csv_file: 
            if csv_file.readlines()[0].split('\n')[-1] != '':
                exist_empty_line = False
            else:
                exist_empty_line = True

        with open('Freiburg/DATA/freiburg_real_weather_data.csv', 'a') as csv_file:  
            if not exist_empty_line:
                csv_file.write('\n')

            for key in Collector.REAL_FIELDS:
                csv_file.write(f"{new_entry[key]}")
                if key != 'real_wind_direction':
                    csv_file.write(', ')
            
            csv_file.write('\n')

    def save_pred(self, new_entry:dict):
        with open('Freiburg/DATA/freiburg_pred_weather_data.csv', 'a') as csv_file:  
            writer = csv.DictWriter(csv_file, fieldnames=Collector.PRED_FIELDS)
            #writer.writeheader()
            writer.writerow(new_entry)

    def remove_last_line(self, path:str):
        with open(path, 'r') as f:
            content = f.readlines()

        print(content)
        content = content[0].split("\n")
        print(content)

        if content[-1] == '':
            with open(path, 'w') as f:
                for line in content[:-1]:
                    f.write(line)

        #if content[-1] != '\n':
        #    with open(path, 'a') as f:
        #        f.write('\n')

    def create_backup(self):
        # create file name
        path = os.getcwd()
        files = os.listdir(path+"/Freiburg/backup")
        now = dt.now()
        now = f"{now.day}.{now.month}.{now.year}"
        name = f"{now}_backup_000"
        i = 1
        while name in files:
            name = f"{now}_backup_{i:03d}"
            i += 1

        # clone content
        with open('Freiburg/DATA/freiburg_real_weather_data.csv', 'r') as f:
            clone = f.readlines()

        # write clone as backup
        with open(f"{path}/Freiburg/backup/{name}", "w") as f:
            f.write(clone)


    def write_log(self, txt:str):
        now = dt.now()
        with open('Freiburg/DATA/log.txt', 'a') as f:
            f.write(f"- {now}   {txt}")

    
if __name__ == '__main__':
    collector = Collector()
    collector.run()
    