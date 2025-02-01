import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Elements - Links")
class TestLinks(BaseTest):

    @allure.title("Verify switching to new tab")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_switch_new_tab(self):
        self.links.open()
        self.links.is_opened()
        self.links.switch_new_tab()
        self.links.check_switch_new_tab()

    @allure.title("Verify created link")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_created_link(self):
        self.links.open()
        self.links.is_opened()
        self.links.click_link("created")
        self.links.verify_link_response_and_text("created")

    @allure.title("Verify no content link")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_no_content_link(self):
        self.links.open()
        self.links.is_opened()
        self.links.click_link("no_content")
        self.links.verify_link_response_and_text("no_content")

    @allure.title("Verify moved link")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_moved_link(self):
        self.links.open()
        self.links.is_opened()
        self.links.click_link("moved")
        self.links.verify_link_response_and_text("moved")

    @allure.title("Verify bad request link")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_bad_request_link(self):
        self.links.open()
        self.links.is_opened()
        self.links.click_link("bad_request")
        self.links.verify_link_response_and_text("bad_request")

    @allure.title("Verify unauthorized link")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_unauthorized_link(self):
        self.links.open()
        self.links.is_opened()
        self.links.click_link("unauthorized")
        self.links.verify_link_response_and_text("unauthorized")

    @allure.title("Verify forbidden link")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_forbidden_link(self):
        self.links.open()
        self.links.is_opened()
        self.links.click_link("forbidden")
        self.links.verify_link_response_and_text("forbidden")

    @allure.title("Verify not found link")
    @pytest.mark.smoke
    @pytest.mark.screenshot
    def test_not_found_link(self):
        self.links.open()
        self.links.is_opened()
        self.links.click_link("not_found")
        self.links.verify_link_response_and_text("not_found")