from selenium.webdriver.support.wait import WebDriverWait
from components.component import Component
from components.constants import ElementsCssSelectors, Constants

__author__ = 'Ivan'



class AddPersonForm(Component):

    def set_name(self, name):
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda l: l.find_element_by_css_selector(ElementsCssSelectors.NAME_INPUT)
        ).send_keys(name)

    def set_birthday(self, year, month, day):
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda l: l.find_element_by_css_selector(ElementsCssSelectors.BIRTHDAY_INPUT)
        ).click()
        while True:
            decade = WebDriverWait(self.driver, 1, 0.1).until(
                lambda l: l.find_element_by_css_selector('.datepicker-years .datepicker-switch')
            ).text
            low_year = int(decade.split('-')[0])
            high_year = int(decade.split('-')[1])
            if low_year > year:
                WebDriverWait(self.driver, 1, 0.1).until(
                    lambda l: l.find_element_by_css_selector('.datepicker-years th.prev')
                ).click()
            elif high_year < year:
                WebDriverWait(self.driver, 1, 0.1).until(
                    lambda l: l.find_element_by_css_selector('.datepicker-years th.next')
                ).click()
            else:
                break

        years = WebDriverWait(self.driver, 1, 0.1).until(
            lambda l: l.find_elements_by_css_selector('.datepicker-years span.year:not(.old):not(.new)')
        )

        for y in years:
            if int(y.text) == year:
                y.click()
                break

        months = WebDriverWait(self.driver, 1, 0.1).until(
            lambda l: l.find_elements_by_css_selector('.datepicker-months span.month')
        )

        for m in months:
            if Constants.MONTHS[month] == m.text:
                m.click()
                break

        days = WebDriverWait(self.driver, 1, 0.1).until(
            lambda l: l.find_elements_by_css_selector('.datepicker-days td.day:not(.old):not(.new)')
        )

        for d in days:
            if int(d.text) == day:
                d.click()
                break

    def set_gender(self, gender):
        if gender == Constants.MALE:
            self.driver.find_element_by_css_selector(ElementsCssSelectors.GENDER_MALE_INPUT).click()
        elif gender == Constants.FEMALE:
            self.driver.find_element_by_css_selector(ElementsCssSelectors.GENDER_FEMALE_INPUT).click()

    def set_email(self, email):
        self.driver.find_element_by_css_selector(ElementsCssSelectors.EMAIL_INPUT).send_keys(email)

    def set_tel(self, tel):
        self.driver.find_element_by_css_selector(ElementsCssSelectors.TEL_INPUT).send_keys(tel)

    def check_email_error_message(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda l: l.find_element_by_css_selector(ElementsCssSelectors.EMAIL_ERROR_MESSAGE_SPAN)
        ).text

    def check_name_error_message(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda l: l.find_element_by_css_selector(ElementsCssSelectors.NAME_ERROR_MESSAGE_SPAN)
        ).text

    def check_gender_error_message(self):
        pass

    def check_tel_error_message(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda l: l.find_element_by_css_selector(ElementsCssSelectors.TEL_ERROR_MESSAGE_SPAN)
        ).text

    def check_birthday_error_message(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda l: l.find_element_by_css_selector(ElementsCssSelectors.BIRTHDAY_ERROR_MESSAGE_SPAN)
        ).text

    def submit(self):
        self.driver.find_element_by_css_selector(ElementsCssSelectors.ADD_PERSON_BUTTON).click()