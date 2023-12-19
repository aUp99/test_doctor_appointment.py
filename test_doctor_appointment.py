from pages.appointment_page import AppointmentPage
from pages.doctor_page import DoctorPage


class TestUserMakeAnAppointment:

    def test_guest_can_sign_up_at_the_club_tub(self, browser):
        page1 = DoctorPage(browser)
        page1.open()
        page1.click_on_club_tab()
        correct_time = page1.select_time()

        page2 = AppointmentPage(browser, open_page=False)
        page2.input_patient_data()
        page2.should_be_correct_time(correct_time)
        page2.should_be_appointment_with_the_club()

    def test_guest_can_sign_up_at_the_default_tub(self, browser):
        page1 = DoctorPage(browser)
        page1.open()
        page1.click_on_default_tab()
        correct_time = page1.select_time()

        page2 = AppointmentPage(browser, open_page=False)
        page2.input_patient_data()
        page2.should_be_correct_time(correct_time)
        page2.should_be_appointment_with_the_default()

    def test_quest_can_sign_up_at_the_cheaper_than_clinic(self, browser):
        page1 = DoctorPage(browser)
        page1.open()
        page1.click_on_cheaper_than_clinic()
        page1.click_on_make_an_appointment()

        page2 = AppointmentPage(browser, open_page=False)
        page2.input_patient_data()
