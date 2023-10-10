import pytest
import unittest
from pages.yatra_launch_page import LaunchPage
from utilities.utils import Utils
from ddt import ddt, data


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerify2(unittest.TestCase):
    log = Utils.custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    def test_otros(self):
        print('Otros test fueron corridos')
