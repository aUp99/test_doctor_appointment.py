import random

import settings
from .base_page import BasePage
from .locators import DoctorPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DoctorPage(BasePage):
    def __init__(self, browser, open_page=True, check_url=True):

        self.url = settings.DOCTOR_PAGE_URL

        super(DoctorPage, self).__init__(browser=browser, open_page=open_page, check_url=check_url, url=self.url)

    def click_on_club_tab(self):
        club_tab_button = self.browser.find_element(*DoctorPageLocators.CLUB_TAB_BUTTON)
        club_tab_button.click()

    def click_on_default_tab(self):
        club_tab_button = self.browser.find_element(*DoctorPageLocators.DEFAULT_TAB_BUTTON)
        club_tab_button.click()

    def click_on_cheaper_than_clinic(self):
        cheaper_than_clinic = self.browser.find_element(*DoctorPageLocators.CHEAPER_THAN_CLINIC)
        cheaper_than_clinic.click()

    def select_time(self):
        time = random.choice(self.browser.find_elements(*DoctorPageLocators.TIME_DOCTOR))
        correct_time = time.text
        time.click()
        return correct_time

    def click_on_make_an_appointment(self):
        make_an_appointment = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((DoctorPageLocators.MAKE_AN_APPOINTMENT_BUTTON)))
        make_an_appointment.click()
