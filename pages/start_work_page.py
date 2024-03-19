from .base_page import BasePage
from .locators import StartWorkPageLocators


class StartWorkPage(BasePage):
    def should_be_auth_form(self):
        assert self.is_element_present(*StartWorkPageLocators.AUTH_FORM), 'Auth form is not presented'

    def fill_fields_incorrectly(self):
        email_field = self.browser.find_element(*StartWorkPageLocators.EMAIL_FIELD)
        email_field.send_keys('test@test.com')

        password_field = self.browser.find_element(*StartWorkPageLocators.PASSWORD_FIELD)
        password_field.send_keys('the best password in the world')

        btn = self.browser.find_element(*StartWorkPageLocators.SUBMIT_BTN)
        btn.click()

    def should_be_error_message_after_incorrectly_fill(self):
        assert self.is_element_present(*StartWorkPageLocators.ERROR_MESSAGE), 'Error message is not presented'


    def should_be_text_in_input_equal_entered_text(self):
        email_field = self.browser.find_element(*StartWorkPageLocators.EMAIL_FIELD)

        assert email_field.get_attribute('value') == 'test@test.com', 'Text in input not equal to entered field'