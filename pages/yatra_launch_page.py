import logging
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.buses_page import BusesPage
from utilities.utils import Utils


class LaunchPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    GOING_TO_RESULT_LIST = "//div[@class='viewport']//div[1]/li"
    SELECT_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    POPULAR_FLIGHTS = '//div[@class="popular_destination popular-destination-module carousalModuleArea"]//a[@class="VueCarousel-slide items"]'
    BUSES_ICON = "//span[@class='demo-icon icon-buses']"

    def get_depart_from_field(self):
        return self.wait_intil_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def get_going_to_field(self):
        return self.wait_intil_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)

    def get_going_to_results(self):
        return self.wait_for_presece_of_all_elements(By.XPATH, self.GOING_TO_RESULT_LIST)

    def get_departure_date_field(self):
        return self.wait_intil_element_is_clickable(By.XPATH, self.SELECT_DATE_FIELD)

    def get_all_dates_field(self):
        return self.wait_intil_element_is_clickable(By.XPATH, self.ALL_DATES)

    def get_popular_flights(self):
        return self.wait_for_presece_of_all_elements(By.XPATH, self.POPULAR_FLIGHTS)

    def get_buses_icon(self):
        return self.wait_intil_element_is_clickable(By.XPATH, self.BUSES_ICON)





    def depart_from_location(self, departlocation):
        self.get_depart_from_field().click()
        self.get_depart_from_field().send_keys(departlocation)
        self.get_depart_from_field().send_keys(Keys.ENTER)
        time.sleep(2)

        # depart_from = self.wait_intil_element_is_clickable(By.XPATH, "//input[@id='BE_flight_origin_city']")
        # depart_from.click()
        # time.sleep(2)
        # depart_from.send_keys(departlocation)
        # time.sleep(2)
        # depart_from.send_keys(Keys.ENTER)
        # time.sleep(2)

    def goingto(self, goingtolocation):
        self.get_going_to_field().click()
        self.get_going_to_field().send_keys(goingtolocation)
        time.sleep(2)
        search_results = self.get_going_to_results()
        self.log.warning('La cantidad de resultados en going to son: ' + str(len(search_results)))          #Cambie el print por log
        for results in search_results:
            self.log.warning(results.text)                                                             #Cambie el print por log
            if goingtolocation in results.text:
                results.click()
                break

    def select_departure_date(self, departuredate):
        self.get_departure_date_field().click()
        """ESPERO QUE SEAN CLICKEABLES Y LUEGO LE PONGO EL FIND ELEMENTS PARA BUSCAR TODAS LAS FECHAS"""
        all_dates = self.get_all_dates_field().find_elements(By.XPATH, self.ALL_DATES)

        for date in all_dates:
            if date.get_attribute('data-date') == departuredate:  # Aca estoy harcodeando el 30/03/20323, en realidad deberia poner una variable
                date.click()
                time.sleep(3)
                break

    def search_flights(self, depart_location, goingto_location, depart_date):
        self.depart_from_location(depart_location)
        self.goingto(goingto_location)
        self.select_departure_date(depart_date)

    def click_buses_icon(self):            #como al clickear el boton de buses se va a otra pagina (trigger point), retorno el objeto de la nueva pagina, asi puedo usar elementos de esta nueva pagina sin crear otro elemeto de la pagina.
        self.get_buses_icon().click()      #Aca se mueve a una nueva pagina
        time.sleep(5)
        buses_icon_result = BusesPage(self.driver)                                 #In order to reduce the object creation. Creamos el objeto de la nueva pagina en el metodo que me lleva a esa pagina.
        return buses_icon_result
