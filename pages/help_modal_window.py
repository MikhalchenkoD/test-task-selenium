from .base_page import BasePage
from .locators import HelpModalWindowLocators


class HelpModalWindow(BasePage):

    def should_be_modal_window_open(self):
        assert self.is_element_present(*HelpModalWindowLocators.MODAL_WINDOW), 'Help modal window is not presented'

    def fill_fields_incorrectly(self):
        name_field = self.browser.find_element(*HelpModalWindowLocators.NAME_FIELD)
        name_field.send_keys('Андрей')

        checkbox = self.browser.find_element(*HelpModalWindowLocators.CHECKBOX)
        checkbox.click()

        btn = self.browser.find_element(*HelpModalWindowLocators.SUBMIT_BTN)
        btn.click()


    def should_be_error_popup_after_incorrectly_fill(self):
        assert self.is_element_present(*HelpModalWindowLocators.PHONE_ERROR_POPUP), 'Error popup is not presented'
