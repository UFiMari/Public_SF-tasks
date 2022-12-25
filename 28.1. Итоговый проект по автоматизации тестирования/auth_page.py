from base_page import BasePage
from selenium.webdriver.common.by import By

class RTLocators:
    LOCATOR_RT_AUTH_BY_PHONE = (By.ID, "t-btn-tab-phone")
    LOCATOR_RT_AUTH_BY_MAIL = (By.ID, "t-btn-tab-mail")
    LOCATOR_RT_AUTH_BY_LOGIN = (By.ID, "t-btn-tab-login")
    LOCATOR_RT_AUTH_BY_LS = (By.ID, "t-btn-tab-ls")

    LOCATOR_RT_USERNAME = (By.ID, "username")
    LOCATOR_RT_PASSWORD = (By.ID, "password")
    LOCATOR_RT_BTN = (By.ID, "kc-login")


class RegLocators:
    LOCATOR_RT_REG = (By.ID, "kc-register")
    LOCATOR_RT_REG_NAME = (By.NAME, "firstName")
    LOCATOR_RT_REG_SURNAME = (By.NAME, "lastName")
    LOCATOR_RT_REG_LOGIN = (By.ID, "address")
    LOCATOR_RT_REG_PASS = (By.ID, "password")
    LOCATOR_RT_REG_PASS_CONFIM = (By.ID, "password-confirm")
    LOCATOR_RT_REG_BTN = (By.NAME, "register")


class RecoveryLocators:
    LOCATOR_RT_RECOVERY = (By.ID, "forgot_password")
    LOCATOR_RT_RECOVERY_PHONE = (By.ID, "t-btn-tab-phone")
    LOCATOR_RT_RECOVERY_MAIL = (By.ID, "t-btn-tab-mail")
    LOCATOR_RT_RECOVERY_LOGIN = (By.ID, "t-btn-tab-login")
    LOCATOR_RT_RECOVERY_LS = (By.ID, "t-btn-tab-ls")
    LOCATOR_RT_RECOVERY_USERNAME = (By.ID, "username")
    LOCATOR_RT_RECOVERY_BTN = (By.ID, "reset")
    LOCATOR_RT_RECOVERY_NEW_PASS = (By.ID, "password-new")
    LOCATOR_RT_RECOVERY_NEW_PASS_CONFIM = (By.ID, "password-confirm")
    LOCATOR_RT_RECOVERY_BTN_UPD = (By.CLASS_NAME, "update-password-form")

class AuthPage(BasePage):

    def authrization_by_phone(self):
        return self.find_element(RTLocators.LOCATOR_RT_AUTH_BY_PHONE, time=5).click()

    def authrization_by_mail(self):
        return self.find_element(RTLocators.LOCATOR_RT_AUTH_BY_MAIL, time=5).click()

    def authrization_by_login(self):
        return self.find_element(RTLocators.LOCATOR_RT_AUTH_BY_LOGIN, time=5).click()

    def authrization_by_LS(self):
        return self.find_element(RTLocators.LOCATOR_RT_AUTH_BY_LS, time=5).click()

    def enter_username(self, value):
        return self.find_element(RTLocators.LOCATOR_RT_USERNAME, time=5).send_keys(value)

    def enter_password(self, value):
        return self.find_element(RTLocators.LOCATOR_RT_PASSWORD, time=5).send_keys(value)

    def btn_click(self):
        return self.find_element(RTLocators.LOCATOR_RT_BTN, time=5).click()


class RegPage(BasePage):

    def go_reg_page(self):
        return self.find_element(RegLocators.LOCATOR_RT_REG, time=5).click()

    def enter_reg_name(self, value):
        return self.find_element(RegLocators.LOCATOR_RT_REG_NAME, time=5).send_keys(value)

    def enter_reg_surname(self, value):
        return self.find_element(RegLocators.LOCATOR_RT_REG_SURNAME, time=5).send_keys(value)

    def enter_reg_login(self, value):
        return self.find_element(RegLocators.LOCATOR_RT_REG_LOGIN, time=5).send_keys(value)

    def enter_reg_pass(self, value):
        return self.find_element(RegLocators.LOCATOR_RT_REG_PASS, time=5).send_keys(value)

    def enter_reg_pass_confim(self, value):
        return self.find_element(RegLocators.LOCATOR_RT_REG_PASS_CONFIM, time=5).send_keys(value)

    def reg_btn_click(self):
        return self.find_element(RegLocators.LOCATOR_RT_REG_BTN, time=5).click()


class RecoveryPage(BasePage):
    def go_to_recovery_page(self):
        return self.find_element(RecoveryLocators.LOCATOR_RT_RECOVERY, time=5).click()

    def recovery_by_phone(self):
        return self.find_element(RecoveryLocators.LOCATOR_RT_RECOVERY_PHONE, time=5).click()

    def recovery_by_mail(self):
        return self.find_element(RecoveryLocators.LOCATOR_RT_RECOVERY_MAIL, time=5).click()

    def recovery_by_login(self):
        return self.find_element(RecoveryLocators.LOCATOR_RT_RECOVERY_LOGIN, time=5).click()

    def recovery_by_LS(self):
        return self.find_element(RecoveryLocators.LOCATOR_RT_RECOVERY_LS, time=5).click()

    def enter_recovery_username(self, value):
        return self.find_element(RecoveryLocators.LOCATOR_RT_RECOVERY_USERNAME, time=5).send_keys(value)

    def recovery_btn_click(self):
        return self.find_element(RecoveryLocators.LOCATOR_RT_RECOVERY_BTN, time=5).click()

    def enter_new_recovery_password(self, value):
        return self.find_element(RecoveryLocators.LOCATOR_RT_RECOVERY_NEW_PASS, time=5).send_keys(value)

    def enter_new_recovery_password_confim(self, value):
        return self.find_element(RecoveryLocators.LOCATOR_RT_RECOVERY_NEW_PASS_CONFIM, time=5).send_keys(value)

    def recovery_btn_upd_click(self):
        return self.find_element(RecoveryLocators.LOCATOR_RT_RECOVERY_BTN, time=5).click()
