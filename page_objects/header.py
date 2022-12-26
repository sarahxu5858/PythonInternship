from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from .base_page import Page


class Header(Page):

    locators = {
     "logo_icon": ("CLASS_NAME", 'header__heading-logo'),
     "shop_by_conern_drpdown": ("CSS", 'details#Details-HeaderMenu-1 span')
    }
    SHOP_BY_CONCERN_DRPDOWN = (By.CSS_SELECTOR, 'details#Details-HeaderMenu-1 span')
    SHOP_BY_PRODUCT_DRPDOWN = (By.CSS_SELECTOR, 'details#Details-HeaderMenu-2 span')
    SHOP_BY_CATEGORY_DRPDOWN = (By.CSS_SELECTOR, 'details#Details-HeaderMenu-3 span')
    SHOP_ALL_BTN = (By.CSS_SELECTOR, 'a[href="/collections/all"]')
    PROFILE_ICON = (By.CSS_SELECTOR, 'use[href="#icon-search"]')
    CART_ICON = (By.CSS_SELECTOR, 'a[href="/collections/all"]')
    ACNE_PROD = (By.CSS_SELECTOR, 'a[href="/collections/for-acne"')
    # SIGN_AGEING_PROD =
    # DARK_SPOTS_PROD =
    # DRY_SKIN_PROD =
    # UNDER_EYE_CARE_PROD =
    FACE_WASHES_PROD = (By.CSS_SELECTOR, '#HeaderMenu-MenuList-2 a[href="/collections/face-wash"')
    # SUNSCREENS_PROD =
    # SKINCARE_ROUTINE_PROD =
    # SKIN_REPAIR_PROD =
    #
    # FACE_PROD_PROD =
    # HAIR_PROD =
    # BODY_PROD =


    def navigate_to_home_page(self):
        self.logo_icon.click()

    def click_by_concern(self):
        return self.click(*self.SHOP_BY_CONCERN_DRPDOWN)

    def click_by_product(self):
        return self.click(*self.SHOP_BY_PRODUCT_DRPDOWN)

    def click_by_category(self):
        return self.click(*self.SHOP_BY_CATEGORY_DRPDOWN)

    def select_by_concern_acne(self, item):
        concern_by = self.find_element(*self.SHOP_BY_CONCERN_DRPDOWN)
        select = Select(concern_by)
        select.select_by_value(item)

    def click_select_acne(self):
        return self.click(*self.ACNE_PROD)

    def click_select_face_wash(self):
        return self.click(*self.FACE_WASHES_PROD)
