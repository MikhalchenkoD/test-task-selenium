import time

from pages.main_page import MainPage
from pages.help_modal_window import HelpModalWindow
class TestHelpModalWindow:
    def test_open_help_modal_window(self, browser):
        page = MainPage(browser)
        page.open()

        page.open_help_modal_window()
        help_modal_window = HelpModalWindow(browser)
        help_modal_window.should_be_modal_window_open()

    def test_fill_fields_incorrectly(self, browser):
        page = MainPage(browser)
        page.open()

        page.open_help_modal_window()
        help_modal_window = HelpModalWindow(browser)

        help_modal_window.fill_fields_incorrectly()
        help_modal_window.should_be_error_popup_after_incorrectly_fill()
