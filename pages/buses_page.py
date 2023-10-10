import logging
import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class BusesPage(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    SEARCH_BUSES_BUTTON = "//input[@value='Search Buses']"

    def get_search_buses_button(self):
        return self.wait_intil_element_is_clickable(By.XPATH, self.SEARCH_BUSES_BUTTON)

    def click_search_buses_button(self):
        self.get_search_buses_button().click()
        time.sleep(2)
        self.log.info('Imprimo cualquier cosa solo para usar los logs')


