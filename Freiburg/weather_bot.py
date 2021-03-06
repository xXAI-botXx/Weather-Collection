from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import random
import time
from enum import Enum
from datetime import datetime as dt
 
# Weathering with AI

class Weather_Bot(object):

    mode = Enum('mode', 'ID NAME XPATH')
    RUN_ON_REPLIT = True

    def __init__(self):
        self.WAIT_TIME_MIN = 2
        self.WAIT_TIME_MAX = 5
        self.TIMEOUT = 30
        self.REAL_DATA_URL = 'https://www.wetterdienst.de/Deutschlandwetter/Freiburg_im_Breisgau/Aktuell/108030'

    def run(self) -> dict:
        self.collect_real_data()
        return self.real_data

    def wait(self, element, mode) -> bool:
        try:
            if mode == Weather_Bot.mode.ID:
                WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_element_located((By.ID, element)))
                return True
            elif mode == Weather_Bot.mode.NAME:
                WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_element_located((By.NAME, element)))
                return True
            elif mode == Weather_Bot.mode.XPATH:
                WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_element_located((By.XPATH, element)))
                return True
        except TimeoutException:
            #print("Loading took too much time!")
            return False

    # ----> Real Data <----
    # - Hour (int)
    # - Minute (int)
    # - Date (str)
    # - Temperature (celsius)
    # - Dew-Point (celsius)
    # - Humidity (percentage)
    # - Weather State
    # - Visibility (km)
    # - Rainfall (mm)
    # - Airpressure
    # - Wind (km/h)
    # - Wind-busts (km/h)
    # - Wind-Direction (str -> N or SW or ...)

    def collect_real_data(self):
        self.real_data = dict()
        self.call_real_data_website()
        self.real_data['hour'] = self.get_hour()
        self.real_data['minute'] = self.get_minute()
        self.real_data['date'] = self.get_date()
        self.real_data['real_temperature'] = self.get_real_temperature()
        self.real_data['real_dew_point'] = self.get_real_dew_point()
        self.real_data['real_humidity'] = self.get_real_humidity()
        self.real_data['real_rainfall'] = self.get_real_rainfall()
        self.real_data['real_air_pressure'] = self.get_real_air_pressure()
        self.real_data['real_weather_state'] = self.get_real_weather_state()
        self.real_data['real_visibility'] = self.get_real_visibility()
        self.real_data['real_wind'] = self.get_real_wind()
        self.real_data['real_wind_gusts'] = self.get_real_wind_gusts()
        self.real_data['real_wind_direction'] = self.get_real_wind_direction()
        self.driver.close()

    def call_real_data_website(self):
        #self.driver = webdriver.Edge('Freiburg/Driver/msedgedriver.exe')
        #self.driver = webdriver.Firefox()
        if Weather_Bot.RUN_ON_REPLIT:
            #chrome_options = Options()
            #chrome_options.add_argument('--no-sandbox')
            #chrome_options.add_argument('--disable-dev-shm-usage')
            #self.driver = webdriver.Chrome("Freiburg/Driver/chromedriver", options=chrome_options)
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome("Freiburg/Driver/chromedriver.exe")
        self.driver.get(self.REAL_DATA_URL)
        time.sleep(random.randint(self.WAIT_TIME_MIN, self.WAIT_TIME_MAX))
        elem = self.driver.find_element_by_xpath("//button[@class='cc-nb-okagree']")
        elem.click()
        time.sleep(0.5)

    def get_date(self) -> str:
        now = dt.now()
        return f"{now.day}.{now.month}.{now.year}"

    # returnt hour -> minutes wayne?
    def get_hour(self) -> int:
        try:
            elements = self.driver.find_elements_by_xpath("//span[@class='vorhersage_schrift1']")
            for elem in elements:
                if elem.text.endswith("Uhr"):
                    return int(elem.text.split(" ")[1].split(":")[0])
            return -999
        except:
            return -999

    def get_minute(self) -> int:
        try:
            elements = self.driver.find_elements_by_xpath("//span[@class='vorhersage_schrift1']")
            for elem in elements:
                if elem.text.endswith("Uhr"):
                    return int(elem.text.split(" ")[1].split(":")[1])
            return -999
        except:
            return -999

    def get_real_temperature(self) -> float:
        try:
            element_to_hover = self.driver.find_element_by_id("temp_1")
            hover = ActionChains(self.driver).move_to_element(element_to_hover)
            hover.perform()
            
            # elem.get_attribute('value')
            elements = self.driver.find_elements_by_xpath("//span[@style='line-height: 18px;']")
            for i, elem in enumerate(elements):
                if elem.text.startswith("Temperatur:"):
                    return float(elem.text.split(" ")[1])
                #print(f"{i}. {elem.text}")
            return -999
        except:
            return -999

    def get_real_dew_point(self) -> float:
        try:
            element_to_hover = self.driver.find_element_by_id("temp_1")
            hover = ActionChains(self.driver).move_to_element(element_to_hover)
            hover.perform()
            
            elements = self.driver.find_elements_by_xpath("//span[@style='line-height: 18px;']")
            for elem in elements:
                if elem.text.startswith("Taupunkt:"):
                    return float(elem.text.split(" ")[1])
            return -999
        except:
            return -999

    def get_real_humidity(self) -> int:
        try:
            element_to_hover = self.driver.find_element_by_id("temp_1")
            hover = ActionChains(self.driver).move_to_element(element_to_hover)
            hover.perform()
            
            elements = self.driver.find_elements_by_xpath("//span[@style='line-height: 18px;']")
            for elem in elements:
                if elem.text.startswith("Feuchte:"):
                    return int(elem.text.split(" ")[1])
            return -999
        except:
            return -999

    def get_real_weather_state(self) -> str:
        try:
            element_to_hover = self.driver.find_element_by_id("symbol_1")
            hover = ActionChains(self.driver).move_to_element(element_to_hover)
            hover.perform()

            element_to_hover = self.driver.find_element_by_id("symbol_1")
            hover = ActionChains(self.driver).move_to_element(element_to_hover)
            hover.perform()
            
            elements = self.driver.find_elements_by_xpath("//span[@style='line-height: 18px;']")
            for elem in elements:
                if elem.text.startswith("Wetterzustand:"):
                #if "Wetterzustand:" in elem.text:
                    return " ".join(elem.text.split(" ")[1:]).replace('??', 'oe').replace('??', 'ae').replace('??', 'ue')
            return -999
        except:
            return -999

    def get_real_visibility(self) -> float:
        try:
            element_to_hover = self.driver.find_element_by_id("symbol_1")
            hover = ActionChains(self.driver).move_to_element(element_to_hover)
            hover.perform()
            
            elements = self.driver.find_elements_by_xpath("//span[@style='line-height: 18px;']")
            for elem in elements:
                if elem.text.startswith("Sichtweite:"):
                    return float(elem.text.split(" ")[1])
            return -999
        except:
            return -999

    def get_real_rainfall(self) -> str:
        try:
            elem = self.driver.find_element_by_id("nieders_1")
            return float(elem.text.split(" ")[0])
        except:
            return -999

    # bekomme ich richtiges Element?
    def get_real_air_pressure(self) -> float:
        try:
            elements = self.driver.find_elements_by_xpath("//span[@class='vorhersage_schrift2']")
            for elem in elements:
                if elem.text.endswith("hPa"):
                    return float(elem.text.split(" ")[0])
            return -999
        except:
            return -999

    def get_real_wind(self) -> float:
        try:
            elements = self.driver.find_elements_by_xpath("//span[@class='vorhersage_schrift2']")
            for elem in elements:
                try:    # if split doesnt work
                    if "km/h" in elem.text and len(elem.text.split(" ")) == 3:
                        return int(elem.text.split(" ")[0])
                except:
                    pass
            return -999
        except:
            return -999

    def get_real_wind_gusts(self) -> float:
        try:
            elem = self.driver.find_element_by_id("wind_1")
            return int(elem.text.split(" ")[1])
        except:
            return -999

    # right elem?
    def get_real_wind_direction(self) -> str:
        try:
            elements = self.driver.find_elements_by_xpath("//span[@class='vorhersage_schrift2']")
            for elem in elements:
                try:    # if split doesnt work
                    if "km/h" in elem.text and len(elem.text.split(" ")) == 3:
                        return elem.text.split(" ")[2]
                except:
                    pass
            return -999
        except:
            return -999


if __name__ == '__main__':
    bot = Weather_Bot()
    bot.collect_real_data()
    #bot.collect_real_data()
    #d = bot.real_data
    #for key, value in d.items():
    #    print(f"{key}: {value}")