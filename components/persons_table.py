from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from components.component import Component
from components.constants import ElementsCssSelectors

__author__ = 'Ivan'


class PersonsTable(Component):
    def delete_all_users(self):
        delete_buttons = self.driver.find_elements_by_css_selector(ElementsCssSelectors.DELETE_PERSON_BUTTON)
        for b in delete_buttons:
            b.click()

    def delete_user(self, email):
        column_indices = self._get_columns_indices()
        try:
            rows = WebDriverWait(self.driver, 5, 0.1).until(
                lambda l: l.find_elements_by_css_selector('#table_body tr')
            )
        except Exception:
            return
        for r in rows:
            fields = r.find_elements_by_css_selector(ElementsCssSelectors.TABLE_ITEM)
            email_in_row = fields[column_indices['E-mail']].text
            if email_in_row == email:
                delete_button = fields[column_indices['Delete']]
                delete_button.click()


    def check_user_with_specified_email_in_the_table(self, email):
        column_indices = self._get_columns_indices()
        try:
            rows = WebDriverWait(self.driver, 5, 0.1).until(
                lambda l: l.find_elements_by_css_selector('#table_body tr')
            )
        except Exception:
            return False
        for r in rows:
            fields = r.find_elements_by_css_selector(ElementsCssSelectors.TABLE_ITEM)
            email_in_row = fields[column_indices['E-mail']].text
            if email_in_row == email:
                return True
        return False

    def check_user_in_the_table(self, name, birthday_year, birthday_month, birthday_day, gender, email, tel):
        column_indices = self._get_columns_indices()
        try:
            rows = WebDriverWait(self.driver, 5, 0.1).until(
                lambda l: l.find_elements_by_css_selector('#table_body tr')
            )
        except Exception:
            return False
        for r in rows:
            fields = r.find_elements_by_css_selector(ElementsCssSelectors.TABLE_ITEM)
            email_in_row = fields[column_indices['E-mail']].text
            if email_in_row == email:

                name_in_row = fields[column_indices['Name']].text
                birthday_in_row = fields[column_indices['Birthday']].text
                birthday_year_in_row = int(birthday_in_row.split('-')[0])
                birthday_month_in_row = int(birthday_in_row.split('-')[1])
                birthday_day_in_row = int(birthday_in_row.split('-')[2])
                tel_in_row = fields[column_indices['Telephone']].text
                gender_in_row = fields[column_indices['Gender']].text
                if name_in_row == name and birthday_year_in_row == birthday_year and birthday_month_in_row == birthday_month and birthday_day_in_row == birthday_day and tel_in_row == tel and gender_in_row == gender:
                    return True
        return False

    def _get_columns_indices(self):
        columns = WebDriverWait(self.driver, 5, 0.1).until(
            lambda l: l.find_elements_by_css_selector(ElementsCssSelectors.TABLE_COLUMN_HEADERS)
        )

        columns_indices = {}

        for i, c in enumerate(columns):
            columns_indices[c.text] = i

        return columns_indices