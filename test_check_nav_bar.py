import time

import pytest

from pages.main_page import MainPage
from pages.buyer_info_page import BuyerInfoPage
from pages.suppliers_info_page import SuppliersInfoPage
from pages.agents_info_page import AgentsInfoPage


class TestCheckNavBar:
    def test_should_see_buyer_info_page_link(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_be_buyer_info_page_link()


    def test_go_to_buyer_info_page(self, browser):
        page = MainPage(browser)
        page.open()

        page.go_to_buyer_info_page()
        buyer_info_page = BuyerInfoPage(browser)
        buyer_info_page.should_be_buyer_info_page_url()


    def test_should_see_suppliers_info_page_link(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_be_suppliers_info_page_link()


    def test_go_to_suppliers_info_page(self, browser):
        page = MainPage(browser)
        page.open()

        page.go_to_suppliers_info_page()
        buyer_info_page = SuppliersInfoPage(browser)
        buyer_info_page.should_be_suppliers_info_page_url()


    def test_should_see_agents_info_page_link(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_be_agents_info_page_link()


    def test_go_to_agents_info_page(self, browser):
        page = MainPage(browser)
        page.open()

        page.go_to_agents_info_page()
        buyer_info_page = AgentsInfoPage(browser)
        buyer_info_page.should_be_agents_info_page_url()
