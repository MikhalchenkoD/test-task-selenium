import time

from pages.main_page import MainPage
from pages.start_work_page import StartWorkPage

class TestStartWorkPage:

    def test_open_start_work_page(self, browser):
        page = MainPage(browser)
        page.open()

        page.go_to_start_work_page()
        help_modal_window = StartWorkPage(browser)
        help_modal_window.should_be_auth_form()


    def test_fill_fields_incorrectly(self, browser):
        page = MainPage(browser)
        page.open()

        page.go_to_start_work_page()
        help_modal_window = StartWorkPage(browser)
        help_modal_window.fill_fields_incorrectly()
        help_modal_window.should_be_error_message_after_incorrectly_fill()


    def test_text_in_input_equal_entered_text(self, browser):
        page = MainPage(browser)
        page.open()

        page.go_to_start_work_page()
        help_modal_window = StartWorkPage(browser)
        help_modal_window.fill_fields_incorrectly()
        help_modal_window.should_be_text_in_input_equal_entered_text()