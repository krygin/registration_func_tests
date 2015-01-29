from components.constants import Constants
from page_objects.index import Index

__author__ = 'Ivan'

import unittest

from selenium.webdriver import DesiredCapabilities, Remote


class Test(unittest.TestCase):
    def setUp(self):
        self.browser = 'CHROME'
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, self.browser).copy()
        )
        self.index = Index(self.driver)
        self.index.open()

    def tearDown(self):
        try:
            self.index.delete_all_users()
        except Exception:
            pass
        finally:
            self.driver.quit()

    #positive tests

    def test_add_male(self):
        self.index.add_user(
            Constants.VALID_NAME_1,
            Constants.VALID_BIRTHDAY_YEAR_1,
            Constants.VALID_BIRTHDAY_MONTH_1,
            Constants.VALID_BIRTHDAY_DAY_1,
            Constants.MALE,
            Constants.VALID_EMAIL_1,
            Constants.VALID_TEL_1
        )
        added = self.index.check_user_in_the_table(
            Constants.VALID_NAME_1,
            Constants.VALID_BIRTHDAY_YEAR_1,
            Constants.VALID_BIRTHDAY_MONTH_1,
            Constants.VALID_BIRTHDAY_DAY_1,
            Constants.MALE,
            Constants.VALID_EMAIL_1,
            Constants.VALID_TEL_1
        )
        self.assertTrue(added)

    def test_add_female(self):
        self.index.add_user(
            Constants.VALID_NAME_1,
            Constants.VALID_BIRTHDAY_YEAR_1,
            Constants.VALID_BIRTHDAY_MONTH_1,
            Constants.VALID_BIRTHDAY_DAY_1,
            Constants.FEMALE,
            Constants.VALID_EMAIL_1,
            Constants.VALID_TEL_1
        )
        added = self.index.check_user_in_the_table(
            Constants.VALID_NAME_1,
            Constants.VALID_BIRTHDAY_YEAR_1,
            Constants.VALID_BIRTHDAY_MONTH_1,
            Constants.VALID_BIRTHDAY_DAY_1,
            Constants.FEMALE,
            Constants.VALID_EMAIL_1,
            Constants.VALID_TEL_1
        )
        self.assertTrue(added)

    def test_delete_user(self):
        self.index.add_user(
            Constants.VALID_NAME_1,
            Constants.VALID_BIRTHDAY_YEAR_1,
            Constants.VALID_BIRTHDAY_MONTH_1,
            Constants.VALID_BIRTHDAY_DAY_1,
            Constants.MALE,
            Constants.VALID_EMAIL_1,
            Constants.VALID_TEL_1
        )
        added = self.index.check_user_with_specified_email_in_the_table(Constants.VALID_EMAIL_1)
        if not added:
            raise Exception
        self.index.delete_user(Constants.VALID_EMAIL_1)
        exists = self.index.check_user_with_specified_email_in_the_table(Constants.VALID_EMAIL_1)
        self.assertFalse(exists)

    #negative tests

    def test_add_user_with_long_name(self):
        self.index.add_user(
            Constants.LONG_NAME,
            Constants.VALID_BIRTHDAY_YEAR_1,
            Constants.VALID_BIRTHDAY_MONTH_1,
            Constants.VALID_BIRTHDAY_DAY_1,
            Constants.MALE,
            Constants.VALID_EMAIL_1,
            Constants.VALID_TEL_1
        )
        added = self.index.check_user_with_specified_email_in_the_table(Constants.VALID_EMAIL_1)
        message = self.index.check_long_name_error_message_appeared()

        self.assertFalse(added)
        self.assertTrue(message)

    def test_add_user_with_empty_name(self):
        self.index.add_user(
            "",
            Constants.VALID_BIRTHDAY_YEAR_1,
            Constants.VALID_BIRTHDAY_MONTH_1,
            Constants.VALID_BIRTHDAY_DAY_1,
            Constants.MALE,
            Constants.VALID_EMAIL_1,
            Constants.VALID_TEL_1
        )
        added = self.index.check_user_with_specified_email_in_the_table(Constants.VALID_EMAIL_1)
        message = self.index.check_empty_name_error_message_appeared()
        self.assertFalse(added)
        self.assertTrue(message)

    def test_add_user_born_in_the_future(self):
        self.index.add_user(
            Constants.VALID_NAME_1,
            Constants.BIRTHDAY_YEAR_IN_THE_FUTURE,
            Constants.BIRTHDAY_MONTH_IN_THE_FUTURE,
            Constants.BIRTHDAY_DAY_IN_THE_FUTURE,
            Constants.MALE,
            Constants.VALID_EMAIL_1,
            Constants.VALID_TEL_1
        )
        added = self.index.check_user_with_specified_email_in_the_table(Constants.VALID_EMAIL_1)
        message = self.index.check_user_from_the_future_error_message_appeared()
        self.assertFalse(added)
        self.assertTrue(message)

    def test_add_user_with_existing_email(self):
        self.index.add_user(
            Constants.VALID_NAME_1,
            Constants.VALID_BIRTHDAY_YEAR_1,
            Constants.VALID_BIRTHDAY_MONTH_1,
            Constants.VALID_BIRTHDAY_DAY_1,
            Constants.MALE,
            Constants.VALID_EMAIL_1,
            Constants.VALID_TEL_1
        )
        user_1_added = self.index.check_user_in_the_table(
            Constants.VALID_NAME_1,
            Constants.VALID_BIRTHDAY_YEAR_1,
            Constants.VALID_BIRTHDAY_MONTH_1,
            Constants.VALID_BIRTHDAY_DAY_1,
            Constants.MALE,
            Constants.VALID_EMAIL_1,
            Constants.VALID_TEL_1
        )
        if not user_1_added:
            raise Exception
        self.index.add_user(
            Constants.VALID_NAME_2,
            Constants.VALID_BIRTHDAY_YEAR_2,
            Constants.VALID_BIRTHDAY_MONTH_2,
            Constants.VALID_BIRTHDAY_DAY_2,
            Constants.MALE,
            Constants.VALID_EMAIL_1,
            Constants.VALID_TEL_2
        )
        user_2_added = self.index.check_user_in_the_table(
            Constants.VALID_NAME_2,
            Constants.VALID_BIRTHDAY_YEAR_2,
            Constants.VALID_BIRTHDAY_MONTH_2,
            Constants.VALID_BIRTHDAY_DAY_2,
            Constants.MALE,
            Constants.VALID_EMAIL_1,
            Constants.VALID_TEL_2
        )
        message = self.index.check_user_with_the_same_email_exists_error_message_appeared()
        self.assertTrue(message)
        self.assertFalse(user_2_added)

    def test_add_user_with_existing_tel(self):
        self.index.add_user(
            Constants.VALID_NAME_1,
            Constants.VALID_BIRTHDAY_YEAR_1,
            Constants.VALID_BIRTHDAY_MONTH_1,
            Constants.VALID_BIRTHDAY_DAY_1,
            Constants.MALE,
            Constants.VALID_EMAIL_1,
            Constants.VALID_TEL_1
        )
        user_1_added = self.index.check_user_in_the_table(
            Constants.VALID_NAME_1,
            Constants.VALID_BIRTHDAY_YEAR_1,
            Constants.VALID_BIRTHDAY_MONTH_1,
            Constants.VALID_BIRTHDAY_DAY_1,
            Constants.MALE,
            Constants.VALID_EMAIL_1,
            Constants.VALID_TEL_1
        )
        if not user_1_added:
            raise Exception
        self.index.add_user(
            Constants.VALID_NAME_2,
            Constants.VALID_BIRTHDAY_YEAR_2,
            Constants.VALID_BIRTHDAY_MONTH_2,
            Constants.VALID_BIRTHDAY_DAY_2,
            Constants.MALE,
            Constants.VALID_EMAIL_2,
            Constants.VALID_TEL_1
        )
        user_2_added = self.index.check_user_in_the_table(
            Constants.VALID_NAME_2,
            Constants.VALID_BIRTHDAY_YEAR_2,
            Constants.VALID_BIRTHDAY_MONTH_2,
            Constants.VALID_BIRTHDAY_DAY_2,
            Constants.MALE,
            Constants.VALID_EMAIL_2,
            Constants.VALID_TEL_1
        )
        message = self.index.check_user_with_the_same_tel_exists_error_message_appeared()
        self.assertTrue(message)
        self.assertFalse(user_2_added)

    def test_add_user_with_long_tel(self):
        self.index.add_user(
            Constants.VALID_NAME_1,
            Constants.VALID_BIRTHDAY_YEAR_1,
            Constants.VALID_BIRTHDAY_MONTH_1,
            Constants.VALID_BIRTHDAY_DAY_1,
            Constants.MALE,
            Constants.VALID_EMAIL_1,
            Constants.LONG_TEL
        )
        added = self.index.check_user_with_specified_email_in_the_table(Constants.VALID_EMAIL_1)
        message = self.index.check_long_telephone_error_message_appeared()
        self.assertFalse(added)
        self.assertTrue(message)

    def test_add_user_with_short_tel(self):
        self.index.add_user(
            Constants.VALID_NAME_1,
            Constants.VALID_BIRTHDAY_YEAR_1,
            Constants.VALID_BIRTHDAY_MONTH_1,
            Constants.VALID_BIRTHDAY_DAY_1,
            Constants.MALE,
            Constants.VALID_EMAIL_1,
            Constants.SHORT_TEL
        )
        added = self.index.check_user_with_specified_email_in_the_table(Constants.VALID_EMAIL_1)
        message = self.index.check_short_telephone_error_message_appeared()
        self.assertFalse(added)
        self.assertTrue(message)

    def test_add_user_with_invalid_tel(self):
        self.index.add_user(
            Constants.VALID_NAME_1,
            Constants.VALID_BIRTHDAY_YEAR_1,
            Constants.VALID_BIRTHDAY_MONTH_1,
            Constants.VALID_BIRTHDAY_DAY_1,
            Constants.MALE,
            Constants.VALID_EMAIL_1,
            Constants.INVALID_TEL
        )
        added = self.index.check_user_with_specified_email_in_the_table(Constants.VALID_EMAIL_1)
        message = self.index.check_invalid_telephone_error_message_appeared()

        self.assertFalse(added)
        self.assertTrue(message)

    def test_add_user_with_invalid_email(self):
        self.index.add_user(
            Constants.VALID_NAME_1,
            Constants.VALID_BIRTHDAY_YEAR_1,
            Constants.VALID_BIRTHDAY_MONTH_1,
            Constants.VALID_BIRTHDAY_DAY_1,
            Constants.MALE,
            Constants.INVALID_EMAIL,
            Constants.VALID_TEL_1
        )
        added = self.index.check_user_with_specified_email_in_the_table(Constants.VALID_EMAIL_1)
        message = self.index.check_invalid_email_error_message_appeared()

        self.assertFalse(added)
        self.assertTrue(message)

    def test_add_user_with_empty_email(self):
        self.index.add_user(
            Constants.VALID_NAME_1,
            Constants.VALID_BIRTHDAY_YEAR_1,
            Constants.VALID_BIRTHDAY_MONTH_1,
            Constants.VALID_BIRTHDAY_DAY_1,
            Constants.MALE,
            "",
            Constants.VALID_TEL_1
        )
        added = self.index.check_user_with_specified_email_in_the_table(Constants.VALID_EMAIL_1)
        message = self.index.check_empty_email_error_message_appeared()

        self.assertFalse(added)
        self.assertTrue(message)

    def test_add_user_with_empty_telephone(self):
        self.index.add_user(
            Constants.VALID_NAME_1,
            Constants.VALID_BIRTHDAY_YEAR_1,
            Constants.VALID_BIRTHDAY_MONTH_1,
            Constants.VALID_BIRTHDAY_DAY_1,
            Constants.MALE,
            Constants.VALID_EMAIL_1,
            ""
        )
        added = self.index.check_user_with_specified_email_in_the_table(Constants.VALID_EMAIL_1)
        message = self.index.check_empty_tel_error_message_appeared()
        self.assertFalse(added)
        self.assertTrue(message)