from .base_page import BasePage


class BuyerInfoPage(BasePage):
    def should_be_buyer_info_page_url(self):
        assert 'buy' in self.browser.current_url
