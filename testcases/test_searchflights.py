import pytest
import softest
from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils
from base.base_driver import BaseDriver
from ddt import ddt, data, unpack, file_data


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerify(softest.TestCase):
    log = Utils.custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    @data(*Utils.read_data_from_csv("C:\\Users\\naman.MSI\\Documents\\workspace_python\\Manish-Verma-selenium_course\\Manish - TestFramework\\testdata\\tdatacsv.csv"))#("C:\\Users\\naman.MSI\\Documents\\workspace_python\\Manish-Verma-selenium_course\\TestFramework\\testdata\\tdatacsv.csv"))
    @unpack
    def test_search_flights(self, goingfrom, goingto, date, text_to_check):
        """Launching browser and opening the travel website"""
        """SELECCIONO VUELOS DE ORIGEN, LLEGADA Y FECHA"""
        self.lp.search_flights(goingfrom, goingto, date)
        """SCROLL"""
        self.lp.page_scroll()
        """VERIFICA QUE LOS VUELOS FRECUENTES CONTENGAN 'Starting From' EN EL TEXTO"""
        popular_flights = self.lp.get_popular_flights()
        self.ut.assert_list_item_text(popular_flights, text_to_check)
        """NADA QUER VER, QUE VAYA Y CLICKEE EN LOS BUSES"""
        buses_icon_result = self.lp.click_buses_icon()
        #bp = BusesPage(self.driver)
        buses_icon_result.click_search_buses_button()
        self.log.info('Imprimo cualquier cosa en los test, solo para usar los logs.')

    def test_2(self):
        """Launching browser and opening the travel website"""
        """SELECCIONO VUELOS DE ORIGEN, LLEGADA Y FECHA"""
        self.lp.search_flights("New Delhi", "New York", "24/04/2023")
        """SCROLL"""
        self.lp.page_scroll()
        """VERIFICA QUE LOS VUELOS FRECUENTES CONTENGAN 'Delhi' EN EL TEXTO"""
        popular_flights = self.lp.get_popular_flights()
        self.ut.assert_list_item_text(popular_flights, "Delhi")
        """NADA QUER VER, QUE VAYA Y CLICKEE EN LOS BUSES"""
        buses_icon_result = self.lp.click_buses_icon()
        #bp = BusesPage(self.driver)
        buses_icon_result.click_search_buses_button()
        print(f'The title is:  {self.lp.get_title_of_the_page()}')


#COMANDO EJEMPLO: pytest -v --browser chrome --url https://www.yatra.com
# pytest -v --browser chrome --url https://www.yatra.com --html=reports/nombre_del_archivo.html --self-contained-html





