import settings
from .base_page import BasePage
from .doctor_page import DoctorPage
from .locators import AppointmentPageLocators


class AppointmentPage(BasePage):
    def __init__(self, browser, open_page=True, check_url=True):

        self.url = settings.APPOINTMENT_PAGE_URL

        super(AppointmentPage, self).__init__(browser=browser, open_page=open_page, check_url=check_url, url=self.url)

    def input_patient_data(self):
        surname_input = self.browser.find_element(*AppointmentPageLocators.SURNAME)
        surname_input.send_keys('Иванов')
        name_input = self.browser.find_element(*AppointmentPageLocators.NAME)
        name_input.send_keys('Петр')
        birthday_date = self.browser.find_element(*AppointmentPageLocators.BIRTHDAY_DATE)
        birthday_date.send_keys('09082007')
        phone_number = self.browser.find_element(*AppointmentPageLocators.PHONE_NUMBER)
        phone_number.send_keys('9881234567')

    def should_be_correct_time(self, time_doctor):
        time_appointment = self.browser.find_element(*AppointmentPageLocators.TIME_APPOINTMENT).text
        assert time_doctor == time_appointment, \
            'The time on the appointment page does not match the doctor time'

    def should_be_appointment_with_the_club(self):
        url = self.browser.current_url
        assert 'type=club' in url, "Doctor's appointment is not a club"

    def should_be_appointment_with_the_default(self):
        url = self.browser.current_url
        assert 'type=club' not in url, "Doctor's appointment is not default"
