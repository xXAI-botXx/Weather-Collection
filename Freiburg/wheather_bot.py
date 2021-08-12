from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import random
import time
from enum import Enum
 

class Wheather_Bot(object):
    mode = Enum('mode', 'ID NAME XPATH')

    def __init__(self):
        self.WAIT_TIME_MIN = 2
        self.WAIT_TIME_MAX = 5
        self.TIMEOUT = 30
        self.REAL_DATA_URL = 'https://wetterstationen.meteomedia.de/?map=Baden-Wuerttemberg&station=108030'
        self.PREDICTED_DATA_URL = 'https://wetterstationen.meteomedia.de/?map=Baden-Wuerttemberg&station=108030'

    def run(self) -> tuple:
        # real data
        self.collect_real_data()
        # predicted data
        self.collect_predicted_data()
        return (self.real_data, self.pred_data)

    def wait(self, element, mode:int) -> bool:
        try:
            if mode == Wheather_Bot.mode.ID:
                WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_element_located((By.ID, element)))
                return True
            elif mode == Wheather_Bot.mode.NAME:
                WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_element_located((By.NAME, element)))
                return True
            elif mode == Wheather_Bot.mode.XPATH:
                WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_element_located((By.XPATH, element)))
                return True
        except TimeoutException:
            #print("Loading took too much time!")
            return False

    # ----> Real Data <----
    def collect_real_data(self):
        self.real_data = dict()
        self.call_real_data_website()
        self.real_data['time'] = self.get_time()
        self.real_data['date'] = self.get_date()
        self.real_data['real_temperature'] = self.get_real_temperature()
        self.real_data['real_wind_mean'] = self.get_real_wind_mean()
        self.real_data['real_wind_gusts'] = self.get_real_wind_gusts()
        self.real_data['real_wind_direction'] = self.get_real_wind_direction()
        self.real_data['real_weather'] = self.get_real_weather_state()
        self.real_data['real_visibility'] = self.get_real_visibility()

    def call_real_data_website(self):
        self.driver = webdriver.Edge('Emmendingen/Driver/msedgedriver.exe')
        self.driver.get(self.REAL_DATA_URL)
        time.sleep(random.randint(self.WAIT_TIME_MIN, self.WAIT_TIME_MAX))

    def get_real_temperature(self) -> float:
        pass

    def get_real_wind_mean(self) -> float:
        pass

    def get_real_wind_gusts(self) -> float:
        pass

    def get_real_wind_direction(self) -> str:
        pass

    def get_real_weather_state(self) -> str:    # maybe a enum
        pass

    def get_real_visibility(self) -> float:
        pass

    def get_date(self) -> str:
        pass
        # data from the website or from datetime

    def get_time(self) -> str:
        pass
        # time from the website or from datetime

    # ----> Predicted Data <----
    def collect_predicted_data(self):
        self.pred_data = dict()
        # ...

    def call_PREDICTED_DATA_URL(self):
        self.driver = webdriver.Edge('Emmendingen/Driver/msedgedriver.exe')
        self.driver.get(self.PREDICTED_DATA_URL)
        time.sleep(random.randint(self.WAIT_TIME_MIN, self.WAIT_TIME_MAX))