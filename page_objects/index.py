from components.add_person_form import AddPersonForm
from components.persons_table import PersonsTable
from page_objects.page import Page

__author__ = 'Ivan'


class Index(Page):
    PATH = ""

    @property
    def form(self):
        return AddPersonForm(self.driver)

    @property
    def table(self):
        return PersonsTable(self.driver)

    def add_user(self, name, birthday_year, birthday_month, birthday_day, gender, email, tel):
        self.form.set_name(name)
        self.form.set_email(email)
        self.form.set_birthday(birthday_year, birthday_month, birthday_day)
        self.form.set_gender(gender)
        self.form.set_tel(tel)
        self.form.submit()


    def delete_user(self, email):
        return self.table.delete_user(email)

    def delete_all_users(self):
        self.table.delete_all_users()

    def check_user_in_the_table(self, name, birthday_year, birthday_month, birthday_day, gender, email, tel):
        return self.table.check_user_in_the_table(name, birthday_year, birthday_month, birthday_day, gender, email, tel)

    def check_user_with_specified_email_in_the_table(self, email):
        return self.table.check_user_with_specified_email_in_the_table(email)

    def check_long_name_error_message_appeared(self):
        return "Ensure this field has no more than 127 characters." in self.form.check_name_error_message()

    def check_empty_name_error_message_appeared(self):
        return "This field may not be blank" in self.form.check_name_error_message()

    def check_user_with_the_same_email_exists_error_message_appeared(self):
        return "This field must be unique." in self.form.check_email_error_message()

    def check_user_with_the_same_tel_exists_error_message_appeared(self):
        return "This field must be unique." in self.form.check_tel_error_message()

    def check_long_telephone_error_message_appeared(self):
        return "Phone number must be in the 10-digits format." in self.form.check_tel_error_message()

    def check_short_telephone_error_message_appeared(self):
        return "Phone number must be in the 10-digits format." in self.form.check_tel_error_message()

    def check_invalid_telephone_error_message_appeared(self):
        return "Phone number must be in the 10-digits format." in self.form.check_tel_error_message()

    def check_invalid_email_error_message_appeared(self):
        return "Enter a valid email address." in self.form.check_email_error_message()

    def check_empty_email_error_message_appeared(self):
        return "This field may not be blank" in self.form.check_email_error_message()

    def check_empty_tel_error_message_appeared(self):
        return "This field may not be blank" in self.form.check_tel_error_message()

    def check_user_from_the_future_error_message_appeared(self):
        return "Birthday must be date in the past." in self.form.check_birthday_error_message()