from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.url = 'https://dircont.com/'
        self.browser.implicitly_wait(5)

    def open(self):
        self.browser.get(self.url)


    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def go_to_main_page(self):
        link = self.browser.find_element(*BasePageLocators.MAIN_PAGE_LINK)
        link.click()

    def go_to_buyer_info_page(self):
        link = self.browser.find_element(*BasePageLocators.BUYER_INFO_PAGE_LINK)
        link.click()

    def go_to_suppliers_info_page(self):
        link = self.browser.find_element(*BasePageLocators.SUPPLIERS_INFO_PAGE_LINK)
        link.click()

    def go_to_agents_info_page(self):
        link = self.browser.find_element(*BasePageLocators.AGENTS_INFO_PAGE_LINK)
        link.click()

    def go_to_start_work_page(self):
        link = self.browser.find_element(*BasePageLocators.START_WORK_PAGE_LINK)
        link.click()

    def open_help_modal_window(self):
        link = self.browser.find_element(*BasePageLocators.HELP_MODAL_WINDOW_LINK)
        link.click()

    def should_be_buyer_info_page_link(self):
        assert self.is_element_present(*BasePageLocators.BUYER_INFO_PAGE_LINK), "Buyer info page link is not presented"

    def should_be_suppliers_info_page_link(self):
        assert self.is_element_present(*BasePageLocators.SUPPLIERS_INFO_PAGE_LINK), "Suppliers info page link is not presented"

    def should_be_agents_info_page_link(self):
        assert self.is_element_present(*BasePageLocators.AGENTS_INFO_PAGE_LINK), "Agents info page link is not presented"

    def should_be_main_page_link(self):
        assert self.is_element_present(*BasePageLocators.MAIN_PAGE_LINK), "Main page link is not presented"
