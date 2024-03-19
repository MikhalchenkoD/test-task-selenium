from .base_page import BasePage


class SuppliersInfoPage(BasePage):
    def should_be_suppliers_info_page_url(self):
        assert 'suppliers' in self.browser.current_url