from auth_page import AuthPage
from auth_page import RegPage
from auth_page import RecoveryPage
from settings import Settings
from selenium.webdriver.common.by import By
import time


def test_autorization_by_phone(browser):
    """Тест авторизации по номеру телефона с корректными данными"""
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.authrization_by_phone()
    auth.enter_username(Settings.VALID_PHONE)
    auth.enter_password(Settings.VALID_PHONE_PASS)
    auth.btn_click()


    LOCATOR = (By.XPATH, '/html[1]/body[1]/div[1]/header[1]/div[1]/div[2]/div[1]/div[2]')

    assert auth.find_element(LOCATOR).text == "Выйти"


def test_autorization_by_phone_with_invalid_pass(browser):
    """Тест авторизации по номеру телефона с некорректным паролем"""
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.authrization_by_phone()
    auth.enter_username(Settings.VALID_PHONE)
    auth.enter_password(Settings.INVALID_PHONE_PASS)
    auth.btn_click()

    LOCATOR = (By.XPATH, '/html/body/div[1]/main/section[2]/div/div/p/span')

    assert auth.find_element(LOCATOR).text == "Неверный логин или пароль"


def test_autorization_by_phone_without_pass(browser):
    """Тест авторизации по номеру телефона с некорректным паролем (пустое поле)"""
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.authrization_by_phone()
    auth.enter_username(Settings.VALID_PHONE)
    auth.enter_password(Settings.ZERO_PASS)
    auth.btn_click()

    LOCATOR = (By.XPATH, '/html/body/div[1]/main/section[2]/div/div/p/span')

    assert auth.find_element(LOCATOR).text == "Неверный логин или пароль"


def test_autorization_by_phone_without_phone(browser):
    """Тест авторизации по номеру телефона, без ввода номера телефона с корректным паролем"""
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.authrization_by_phone()
    auth.enter_username(Settings.ZERO_LOGIN)
    auth.enter_password(Settings.VALID_PHONE_PASS)
    auth.btn_click()

    LOCATOR = (By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/span')

    assert auth.find_element(LOCATOR).text == "Введите номер телефона"


def test_autorization_by_phone_with_invalid_phone(browser):
    """Тест авторизации по номеру телефона, с некорректным номером телефона и с корректным паролем"""
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.authrization_by_phone()
    auth.enter_username(Settings.INVALID_PHONE)
    auth.enter_password(Settings.VALID_PHONE_PASS)
    auth.btn_click()

    LOCATOR = (By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/span')

    assert auth.find_element(LOCATOR).text == "Неверный формат телефона"



def test_autorization_by_mail(browser):
    """Тест авторизации по электронной почте с корректными данными"""
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.authrization_by_mail()
    auth.enter_username(Settings.VALID_MAIL)
    auth.enter_password(Settings.VALID_MAIL_PASS)
    auth.btn_click()


    LOCATOR = (By.XPATH, '/html/body/div/header/div/div[2]/div/div[1]/a[2]')

    assert auth.find_element(LOCATOR).text == 'Личный кабинет'



def test_autorization_by_mail_with_invalid_pass(browser):
    """Тест авторизации по электронной почте с некорректным паролем"""
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.authrization_by_mail()
    auth.enter_username(Settings.VALID_MAIL)
    auth.enter_password(Settings.INVALID_MAIL_PASS)
    auth.btn_click()


    LOCATOR = (By.XPATH, '/html/body/div[1]/main/section[2]/div/div/p/span')

    assert auth.find_element(LOCATOR).text == "Неверный логин или пароль"


def test_autorization_by_mail_with_phone_data(browser):
    """Тест авторизации по электронной почте с данными для входа по номеру телефона"""
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.authrization_by_mail()
    auth.enter_username(Settings.VALID_PHONE)
    auth.enter_password(Settings.VALID_PHONE_PASS)
    auth.btn_click()


    LOCATOR = (By.XPATH, '/html/body/div/header/div/div[2]/div/div[1]/a[2]')

    assert auth.find_element(LOCATOR).text == 'Личный кабинет'


def test_autorization_by_login_with_invalid_data(browser):
    """Тест авторизации по логину с некорректными данными"""
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.authrization_by_login()
    auth.enter_username(Settings.INVALID_LOGIN)
    auth.enter_password(Settings.INVALID_LOGIN_PASS)
    auth.btn_click()


    LOCATOR = (By.XPATH, '/html/body/div[1]/main/section[2]/div/div/p/span')

    assert auth.find_element(LOCATOR).text == "Неверный логин или пароль"



def test_autorization_by_ls_with_invalid_data(browser):
    """Тест авторизации по лицевому счету с некорректными данными"""
    auth = AuthPage(browser)
    auth.go_to_site()
    auth.authrization_by_LS()
    auth.enter_username(Settings.INVALID_LS)
    auth.enter_password(Settings.INVALID_LS_PASS)
    auth.btn_click()


    LOCATOR = (By.XPATH, '/html/body/div[1]/main/section[2]/div/div/p/span')

    assert auth.find_element(LOCATOR).text == "Неверный логин или пароль"

def test_registration_by_new_phone(browser):
    """Тест регистрации по новому телефону"""
    reg = RegPage(browser)
    reg.go_to_site()
    reg.go_reg_page()
    reg.enter_reg_name(Settings.NEW_USER_NAME)
    reg.enter_reg_surname(Settings.NEW_UESR_SURNAME)
    reg.enter_reg_login(Settings.NEW_PHONE)
    reg.enter_reg_pass(Settings.NEW_REG_PASS)
    reg.enter_reg_pass_confim(Settings.NEW_REG_PASS)
    reg.reg_btn_click()

    LOCATOR = (By.CLASS_NAME, 'card-container__title')
    assert reg.find_element(LOCATOR).text == "Код подтверждения отправлен"

def test_registration_by_reg_phone(browser):
    """Тест регистрации по уже зарегистрированному телефону"""
    reg = RegPage(browser)
    reg.go_to_site()
    reg.go_reg_page()
    reg.enter_reg_name(Settings.NEW_USER_NAME)
    reg.enter_reg_surname(Settings.NEW_UESR_SURNAME)
    reg.enter_reg_login(Settings.VALID_PHONE)
    reg.enter_reg_pass(Settings.NEW_REG_PASS)
    reg.enter_reg_pass_confim(Settings.NEW_REG_PASS)
    reg.reg_btn_click()


    LOCATOR = (By.CLASS_NAME, 'card-modal__title')
    assert reg.find_element(LOCATOR).text == "Учётная запись уже существует"

def test_registration_by_new_mail(browser):
    """Тест регистрации по новому телефону"""
    reg = RegPage(browser)
    reg.go_to_site()
    reg.go_reg_page()
    reg.enter_reg_name(Settings.NEW_USER_NAME)
    reg.enter_reg_surname(Settings.NEW_UESR_SURNAME)
    reg.enter_reg_login(Settings.NEW_MAIL)
    reg.enter_reg_pass(Settings.NEW_REG_PASS)
    reg.enter_reg_pass_confim(Settings.NEW_REG_PASS)
    reg.reg_btn_click()

    LOCATOR = (By.CLASS_NAME, 'card-container__title')
    assert reg.find_element(LOCATOR).text == "Код подтверждения отправлен"

def test_registration_by_reg_mail(browser):
    """Тест регистрации по уже зарегистрированной электронной почте"""
    reg = RegPage(browser)
    reg.go_to_site()
    reg.go_reg_page()
    reg.enter_reg_name(Settings.NEW_USER_NAME)
    reg.enter_reg_surname(Settings.NEW_UESR_SURNAME)
    reg.enter_reg_login(Settings.VALID_MAIL)
    reg.enter_reg_pass(Settings.NEW_REG_PASS)
    reg.enter_reg_pass_confim(Settings.NEW_REG_PASS)
    reg.reg_btn_click()

    LOCATOR = (By.CLASS_NAME, 'card-modal__title')
    assert reg.find_element(LOCATOR).text == "Учётная запись уже существует"


def test_receive_code_for_recovery_by_phone(browser):
    """Тест проверки отправки кода для восстановления пароля по номеру телефона (задержка поставлена для ввода капчи производится вручную)"""
    recovery = RecoveryPage(browser)
    recovery.go_to_site()
    recovery.go_to_recovery_page()
    recovery.recovery_by_phone()
    recovery.enter_recovery_username(Settings.VALID_PHONE)

    time.sleep(60)

    recovery.recovery_btn_click()

    LOCATOR = (By.CLASS_NAME, "card-container__title")

    assert recovery.find_element(LOCATOR).text == "Восстановление пароля"


def test_receive_code_for_recovery_by_invalid_phone(browser):
    """Тест восстановления пароля по некорректному номеру телефона (задержка поставлена для ввода капчи производится вручную)"""
    recovery = RecoveryPage(browser)
    recovery.go_to_site()
    recovery.go_to_recovery_page()
    recovery.recovery_by_phone()
    recovery.enter_recovery_username(Settings.INVALID_PHONE)

    time.sleep(60)

    recovery.recovery_btn_click()

    LOCATOR = (By.CLASS_NAME, "rt-input-container__meta rt-input-container__meta--error")

    assert recovery.find_element(LOCATOR).text == "Неверный формат телефона"

def test_recovery_by_phone(browser):
    """Тест восстановления пароля по номеру телефона при введении кода (задержки поставлены для ввода капчи/кода, который производится вручную)"""
    recovery = RecoveryPage(browser)
    recovery.go_to_site()
    recovery.go_to_recovery_page()
    recovery.recovery_by_phone()
    recovery.enter_recovery_username(Settings.VALID_PHONE)

    time.sleep(60)

    recovery.recovery_btn_click()

    time.sleep(100)

    recovery.enter_new_recovery_password(Settings.NEW_VALID_PHONE_PASS)
    recovery.enter_new_recovery_password_confim(Settings.NEW_VALID_PHONE_PASS)
    recovery.recovery_btn_upd_click()

    LOCATOR = (By.CLASS_NAME, "card-container__title")

    assert recovery.find_element(LOCATOR).text == "Авторизация"


def test_recovery_by_phone_with_old_code(browser):
    """Тест восстановления пароля по номеру телефона при введении кода с истекшим сроком действия (задержки поставлены для ввода капчи/кода, который производится вручную)"""
    recovery = RecoveryPage(browser)
    recovery.go_to_site()
    recovery.go_to_recovery_page()
    recovery.recovery_by_phone()
    recovery.enter_recovery_username(Settings.VALID_PHONE)

    time.sleep(60)

    recovery.recovery_btn_click()

    time.sleep(130)

    LOCATOR = (By.ID, "form-error-message")

    assert recovery.find_element(LOCATOR).text == "Срок действия кода истёк. Пожалуйста, запросите код снова"

def test_recovery_by_phone_with_invalid_code(browser):
    """Тест восстановления пароля по номеру телефона при введении некорректного кода (задержки поставлены для ввода капчи/кода, который производится вручную)"""
    recovery = RecoveryPage(browser)
    recovery.go_to_site()
    recovery.go_to_recovery_page()
    recovery.recovery_by_phone()
    recovery.enter_recovery_username(Settings.VALID_PHONE)

    time.sleep(60)

    recovery.recovery_btn_click()

    time.sleep(60)

    LOCATOR = (By.ID, "form-error-message")

    assert recovery.find_element(LOCATOR).text == "Неверный код. Повторите попытку"

def test_recovery_by_mail(browser):
    """Тест восстановления пароля по электронной почте (задержка поставлена для ввода капчи производится вручную)"""
    recovery = RecoveryPage(browser)
    recovery.go_to_site()
    recovery.go_to_recovery_page()
    recovery.recovery_by_mail()
    recovery.enter_recovery_username(Settings.VALID_MAIL)

    time.sleep(120)

    recovery.recovery_btn_click()

    LOCATOR = (By.CLASS_NAME, "card-container__title")

    assert recovery.find_element(LOCATOR).text == "Восстановление пароля"


def test_recovery_by_invalid_mail(browser):
    """Тест восстановления пароля по некорректной электронной почте (задержка поставлена для ввода капчи производится вручную)"""
    recovery = RecoveryPage(browser)
    recovery.go_to_site()
    recovery.go_to_recovery_page()
    recovery.recovery_by_mail()
    recovery.enter_recovery_username(Settings.INVALID_MAIL)

    time.sleep(60)

    recovery.recovery_btn_click()

    LOCATOR = (By.ID, "form-error-message")

    time.sleep(60)

    assert recovery.find_element(LOCATOR).text == "Неверный логин или текст с картинки"
