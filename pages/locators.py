from selenium.webdriver.common.by import By


class BasePageLocators:
    MAIN_PAGE_LINK = (By.CSS_SELECTOR, '.t228__imgwrapper')
    BUYER_INFO_PAGE_LINK = (By.CSS_SELECTOR, '.t228__list.t-menu__list  li:nth-child(1) a')
    SUPPLIERS_INFO_PAGE_LINK = (By.CSS_SELECTOR, '.t228__list.t-menu__list  li:nth-child(2) a')
    AGENTS_INFO_PAGE_LINK = (By.CSS_SELECTOR, '.t228__list.t-menu__list  li:nth-child(3) a')
    START_WORK_PAGE_LINK = (By.CSS_SELECTOR, '.t228__right_buttons_but:nth-child(1) a')
    HELP_MODAL_WINDOW_LINK = (By.CSS_SELECTOR, '.t228__right_buttons_but:nth-child(2) a')

class MainPageLocators:
    FIRST_POPUP = (By.LINK_TEXT, '#popup1')



class HelpModalWindowLocators:
    MODAL_WINDOW = (By.CSS_SELECTOR, '.t396__elem.tn-elem.tn-elem__5865880741684954125877')
    NAME_FIELD = (By.CSS_SELECTOR, '#nm-1683455236864')
    CHECKBOX = (By.CSS_SELECTOR, '#form586588074 .t-input-group.t-input-group_cb .t-checkbox__indicator')
    SUBMIT_BTN = (By.CSS_SELECTOR, '.tn-atom__sbs-anim-wrapper .t-form__inputsbox .tn-form__submit button')
    PHONE_ERROR_POPUP = (By.CSS_SELECTOR, '.t-input-group.t-input-group_ph.js-error-control-box .t-input-block .t-input-error')


class StartWorkPageLocators:
    AUTH_FORM = (By.CSS_SELECTOR, '.auth-form form')
    EMAIL_FIELD = (By.CSS_SELECTOR, '.auth-form form input[name="email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '.auth-form form input[name="password"]')
    SUBMIT_BTN = (By.CSS_SELECTOR, '.btn')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.form-control-feedback')