"""ACA VAN LOS METODOS COMUNES QUE PUEDO REUTILIZAR EN TODAS LAS PAGINAS"""
"""TODO LO QUE TENGA DRIVER VA ACA, LO QUE NO TENGA DRIVER VA A LAS UTILITIES"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver            #This links this class with the main Webdriver (the only webdriver)

    def page_scroll(self):
        """Escrollear toda la pagina para que cargue la info en el DOM completa"""
        total_height = int(self.driver.execute_script("return document.body.scrollHeight"))
        for i in range(1, total_height, 15):
            self.driver.execute_script("window.scrollTo(0, {});".format(i))

    def wait_for_presece_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        print("La cantidad de rutas frecuentes son: " + str(len(list_of_elements)))
        return list_of_elements

    def wait_intil_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def get_title_of_the_page(self):
        return self.driver.title



