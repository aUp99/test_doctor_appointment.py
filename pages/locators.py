from selenium.webdriver.common.by import By


class DoctorPageLocators:
    CLUB_TAB_BUTTON = (By.CSS_SELECTOR, '[data-doctor-id="888804"] .appointment-type-tab__item:nth-child(1)')
    DEFAULT_TAB_BUTTON = (By.CSS_SELECTOR, '[data-doctor-id="888804"] .appointment-type-tab__item:nth-child(2)')
    TIME_DOCTOR = (By.CSS_SELECTOR, '[data-doctor-id="888804"] .slot-set__item')
    CHEAPER_THAN_CLINIC = (By.CSS_SELECTOR, '[data-doctor-id="888804"] .ui-text_underline')
    MAKE_AN_APPOINTMENT_BUTTON = (By.CSS_SELECTOR, '.v-dialog--active a.v-size--default')


class AppointmentPageLocators:
    SURNAME = (By.CSS_SELECTOR, 'input#last_name')
    NAME = (By.CSS_SELECTOR, 'input#first_name')
    BIRTHDAY_DATE = (By.CSS_SELECTOR, 'input#birthday')
    PHONE_NUMBER = (By.CSS_SELECTOR, 'input[name="phone"]')
    TIME_APPOINTMENT = (By.CSS_SELECTOR, 'span.ui-text_color_neur-blue')

