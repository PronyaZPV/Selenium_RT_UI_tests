import pytest
from selenium.common.exceptions import TimeoutException

from ..pages.auth_page import AuthPage
from ..pages.footer import Footer
from ..pages.header import Header
from ..pages.recovery_page import RecoveryPage
from ..pages.registration_page import RegistrationPage
from ..parameters import *


@pytest.mark.auth
def test_auth_page_elements(browser):   # RT_AUTH-001
    auth_page = AuthPage(browser)
    footer = Footer(browser)
    header = Header(browser)
    auth_page.go_to_site()

    assert header.header().is_displayed()
    assert header.header_logo().is_displayed()

    assert footer.footer().is_displayed()
    assert footer.footer_info().is_displayed()
    assert footer.footer_phone().is_displayed()
    assert footer.footer_phone().text == '8 800 100 0 800', 'Некорректный номер телефона поддержки'

    left_width = auth_page.left_body().size['width']
    right_width = auth_page.right_body().size['width']
    assert left_width == right_width

    assert auth_page.left_body().is_displayed()
    assert auth_page.left_body().text == 'Личный кабинет\nПерсональный помощник в цифровом мире Ростелекома', \
        'Invalid text in left side'
    assert auth_page.body_logo().is_displayed()

    assert auth_page.right_body().is_displayed()
    assert auth_page.form_title().text == 'Авторизация', 'Форма авторизации не открылась'


@pytest.mark.auth
def test_footer_elements(browser):   # RT_AUTH-002
    footer = Footer(browser)
    footer.go_to_site()

    assert footer.footer().is_displayed()
    assert footer.footer_info().is_displayed()
    assert footer.footer_phone().is_displayed()
    assert footer.footer_phone().text == '8 800 100 0 800', 'Некорректный номер телефона поддержки'
    assert footer.footer_copyright().is_displayed()
    assert footer.footer_cookies().is_displayed()
    assert footer.footer_agreement().is_displayed()


@pytest.mark.auth
def test_auth_form_elements(browser):   # RT_AUTH-003
    auth_page = AuthPage(browser)
    auth_page.go_to_site()

    assert auth_page.auth_form().is_displayed()
    assert auth_page.form_title().text == 'Авторизация', 'Форма авторизации не открылась'
    assert auth_page.tabs_menu().is_displayed()
    assert auth_page.login_field().is_displayed()
    assert auth_page.pass_field().is_displayed()
    assert auth_page.checkbox_remember_me().is_displayed()
    assert auth_page.forgot_password_muted().is_displayed()
    assert auth_page.enter_button().is_displayed()
    assert auth_page.agreement_contract().is_displayed()
    assert auth_page.social_providers().is_displayed()
    assert auth_page.register_link().is_displayed()


@pytest.mark.auth
def test_tabs_menu_elements(browser):   # RT_AUTH-004
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    tabs = auth_page.tabs_menu().text
    assert tabs == AuthPage.LIST_TABS_MENU_ELEMENTS


@pytest.mark.auth
def test_tabs_menu_logins(browser):   # RT_AUTH-005
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    assert auth_page.phone_field().is_displayed()

    auth_page.click_on_tab_menu_email()
    assert auth_page.email_field().is_displayed()

    auth_page.click_on_tab_menu_login()
    assert auth_page.login_field_in_tab().is_displayed()

    auth_page.click_on_tab_menu_ls()
    assert auth_page.input_ls_field().is_displayed()


@pytest.mark.auth
def test_auto_change_tab(browser):   # RT_AUTH-006
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.clear_all()
    auth_page.enter_login('email@email.ru')
    auth_page.submit()
    assert auth_page.email_field().is_displayed()

    auth_page.clear_all()
    auth_page.enter_login('+79112223344')
    auth_page.submit()
    assert auth_page.phone_field().is_displayed()


@pytest.mark.auth
def test_error_login_and_pass(browser):   # RT_AUTH-007
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.clear_all()
    auth_page.enter_login('+79000000000')
    auth_page.enter_pass('12qwe!Q')
    auth_page.enter_button().click()

    assert auth_page.form_error_message().is_displayed()
    assert auth_page.forgot_password_active().is_displayed()


@pytest.mark.auth
def test_login_mask(browser):   # RT_AUTH-008
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.clear_all()
    auth_page.enter_login('9')
    assert auth_page.input_login_mask() == '79'


@pytest.mark.auth
def test_recovery_link(browser):   # RT_AUTH-009
    auth_page = AuthPage(browser)
    recovery_page = RecoveryPage(browser)
    auth_page.go_to_site()
    auth_page.forgot_password_muted().click()

    assert recovery_page.form_title().text == 'Восстановление пароля', 'Форма восстановления пароля не открылась'


@pytest.mark.auth
def test_agreement_link(browser):   # RT_AUTH-0010
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.agreement_contract().click()
    browser.switch_to.window(browser.window_handles[1])
    assert auth_page.agreement_contract_page().is_displayed()


@pytest.mark.auth
def test_registry_link(browser):   # RT_AUTH-0011
    auth_page = AuthPage(browser)
    registration_page = RegistrationPage(browser)
    auth_page.go_to_site()
    auth_page.register_link().click()

    assert registration_page.form_title().text == 'Регистрация', 'Форма регистрации не открылась'


@pytest.mark.auth
def test_social_links(browser):   # RT_REG-001
    auth_page = AuthPage(browser)
    auth_page.go_to_site()

    assert auth_page.social_vk().is_displayed()
    assert auth_page.social_ya().is_displayed()
    assert auth_page.social_ok().is_displayed()
    assert auth_page.social_mail().is_displayed()
    assert auth_page.social_google().is_displayed()


@pytest.mark.register
def test_registration_form_elements(browser):   # RT_REG-001
    reg_page = RegistrationPage(browser)
    RegistrationPage.go_to_registration_page(browser)

    assert reg_page.form_title().text == 'Регистрация', 'Форма регистрации не открылась'
    assert reg_page.registration_form().is_displayed()
    assert reg_page.firstname_field().is_displayed()
    assert reg_page.lastname_field().is_displayed()
    assert reg_page.region_dropdown().is_displayed()
    assert reg_page.login_field().is_displayed()
    assert reg_page.password_field().is_displayed()
    assert reg_page.password_confirm_field().is_displayed()
    assert reg_page.enter_button().is_displayed()
    assert reg_page.form_agreement().is_displayed()


@pytest.mark.register
def test_registration_errors(browser):   # RT_REG-002
    reg_page = RegistrationPage(browser)
    RegistrationPage.go_to_registration_page(browser)
    reg_page.enter_button().click()

    assert reg_page.count_of_errors() == 5


@pytest.mark.register
@pytest.mark.parametrize('name', valid_names, ids=valid_names_ids)
def test_name_validation_positive(browser, name):   # RT_REG-003 - pisitive
    if name is None:
        name = ''
    RegistrationPage.go_to_registration_page(browser)
    reg_page = RegistrationPage(browser)
    reg_page.clear_all()
    reg_page.enter_firstname(name)
    reg_page.submit()
    try:
        reg_page.validation_error()
        assert False, 'Отобразилась ошибка валидации, а не должна'
    except TimeoutException:
        assert True


@pytest.mark.register
@pytest.mark.parametrize('name', invalid_names, ids=invalid_names_ids)
def test_name_validation_negative(browser, name):   # RT_REG-003 - negative
    if name is None:
        name = ''
    RegistrationPage.go_to_registration_page(browser)
    reg_page = RegistrationPage(browser)
    reg_page.clear_all()
    reg_page.enter_firstname(name)
    reg_page.submit()
    try:
        reg_page.validation_error()
        assert True
    except TimeoutException:
        assert False, 'Ошибка валидации не отобразилась, а должна быть'


@pytest.mark.register
@pytest.mark.parametrize('lastname', valid_names, ids=valid_names_ids)
def test_lastname_validation_positive(browser, lastname):   # RT_REG-004 - pisitive
    if lastname is None:
        lastname = ''
    RegistrationPage.go_to_registration_page(browser)
    reg_page = RegistrationPage(browser)
    reg_page.clear_all()
    reg_page.enter_lastname(lastname)
    reg_page.submit()
    try:
        reg_page.validation_error()
        assert False, 'Отобразилась ошибка валидации, а не должна'
    except TimeoutException:
        assert True


@pytest.mark.register
@pytest.mark.parametrize('lastname', invalid_names, ids=invalid_names_ids)
def test_lastname_validation_negative(browser, lastname):   # RT_REG-004 - negative
    if lastname is None:
        lastname = ''
    RegistrationPage.go_to_registration_page(browser)
    reg_page = RegistrationPage(browser)
    reg_page.clear_all()
    reg_page.enter_lastname(lastname)
    reg_page.submit()
    try:
        reg_page.validation_error()
        assert True
    except TimeoutException:
        assert False, 'Ошибка валидации не отобразилась, а должна быть'


@pytest.mark.register
@pytest.mark.parametrize('password', valid_password, ids=valid_password_ids)
def test_password_validation_positive(browser, password):   # RT_REG-005 - pisitive
    if password is None:
        password = ''
    RegistrationPage.go_to_registration_page(browser)
    reg_page = RegistrationPage(browser)

    reg_page.clear_all()
    reg_page.enter_password(password)
    # time.sleep(1)
    reg_page.submit()
    try:
        reg_page.validation_error()
        assert False, 'Отобразилась ошибка валидации, а не должна'
    except TimeoutException:
        assert True


@pytest.mark.register
@pytest.mark.parametrize('password', invalid_password, ids=invalid_password_ids)
def test_password_validation_negative(browser, password):   # RT_REG-005 - negative
    if password is None:
        password = ''
    RegistrationPage.go_to_registration_page(browser)
    reg_page = RegistrationPage(browser)
    reg_page.clear_all()
    reg_page.enter_password(password)
    reg_page.submit()
    try:
        reg_page.validation_error()
        assert True
    except TimeoutException:
        assert False, 'Ошибка валидации не отобразилась, а должна быть'
