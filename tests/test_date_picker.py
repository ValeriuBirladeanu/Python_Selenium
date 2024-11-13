import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Widgets")
class TestDatePicker(BaseTest):
    @allure.title("Test select date in calendar")
    @pytest.mark.smoke
    def test_select_date(self):
        self.date_picker.open()
        self.date_picker.is_opened()
        self.date_picker.select_date()
        self.date_picker.verify_date()