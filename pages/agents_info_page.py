from .base_page import BasePage

class AgentsInfoPage(BasePage):
    def should_be_agents_info_page_url(self):
        assert 'agent' in self.browser.current_url