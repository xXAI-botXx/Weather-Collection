from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import random
import time
from enum import Enum

class Collector(object):

    mode = Enum('mode', 'ID NAME XPATH')

    def __init__(self):
        self.WAIT_TIME_MIN = 2
        self.WAIT_TIME_MAX = 5
        self.TIMEOUT = 30
        self.REAL_DATA_URL = 'https://wetterstationen.meteomedia.de/?map=Baden-Wuerttemberg&station=108030'
        self.PREDICTED_DATA_URL = 'https://wetterstationen.meteomedia.de/?map=Baden-Wuerttemberg&station=108030'

    def run(self):
        self.results = dict()
        # real data
        # ...
        # predicted data
        # ...

    def wait(self, element, mode:int) -> bool:
        try:
            if mode == Collector.mode.ID:
                WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_element_located((By.ID, element)))
                return True
            elif mode == Collector.mode.NAME:
                WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_element_located((By.NAME, element)))
                return True
            elif mode == Collector.mode.XPATH:
                WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_element_located((By.XPATH, element)))
                return True
        except TimeoutException:
            #print("Loading took too much time!")
            return False

    # ----> Real Data <----
    def call_real_data_website(self):
        self.driver = webdriver.Edge('Emmendingen/Driver/msedgedriver.exe')
        self.driver.get(self.REAL_DATA_URL)
        time.sleep(random.randint(self.WAIT_TIME_MIN, self.WAIT_TIME_MAX))

    def get_temperature(self) -> float:
        pass

    def get_wind_mean(self) -> float:
        pass

    def get_wind_gusts(self) -> float:
        pass

    def get_wind_direction(self) -> str:
        pass

    def get_weather_state(self) -> str:    # maybe a enum
        pass

    def get_visibility(self) -> float:
        pass

    def get_date(self) -> str:
        pass
        # data from the website or from datetime

    def get_time(self) -> str:
        pass
        # time from the website or from datetime

    # ----> Predicted Data <----
    def call_PREDICTED_DATA_URL(self):
        self.driver = webdriver.Edge('Emmendingen/Driver/msedgedriver.exe')
        self.driver.get(self.PREDICTED_DATA_URL)
        time.sleep(random.randint(self.WAIT_TIME_MIN, self.WAIT_TIME_MAX))
    