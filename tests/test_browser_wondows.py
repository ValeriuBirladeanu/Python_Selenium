import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Alerts, Frame & Windows - Browser_Windows")
class TestBrowserWindows(BaseTest):

    @allure.title("Test opened new tab")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_open_new_table(self):
        self.browser_windows.open()
        self.browser_windows.click_new_tab_button()
        self.browser_windows.check_opened_new_tab()

    @allure.title("Test opened new window")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_open_new_table(self):
        self.browser_windows.open()
        self.browser_windows.click_new_window_button()
        self.browser_windows.check_opened_new_window()