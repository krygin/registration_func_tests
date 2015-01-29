__author__ = 'Ivan'


class ElementsCssSelectors(object):
    DELETE_PERSON_BUTTON = '#table_body .delete'
    ADD_PERSON_BUTTON = '#submit'
    NAME_INPUT = '#name'
    EMAIL_INPUT = '#email'
    BIRTHDAY_INPUT = '#birthday'
    TEL_INPUT = '#tel'
    GENDER_MALE_INPUT = '#gender_male'
    GENDER_FEMALE_INPUT = '#gender_female'
    TABLE_COLUMN_HEADERS = '#persons_table th'
    TABLE_ITEM = 'td'

    NAME_ERROR_MESSAGE_SPAN = '#name_error'
    EMAIL_ERROR_MESSAGE_SPAN = '#email_error'
    TEL_ERROR_MESSAGE_SPAN = '#tel_error'
    BIRTHDAY_ERROR_MESSAGE_SPAN = '#birthday_error'


class Constants(object):
    MONTHS = {
        1: 'Jan',
        2: 'Feb',
        3: 'Mar',
        4: 'Apr',
        5: 'May',
        6: 'Jun',
        7: 'Jul',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec'
    }
    MALE = 'M'
    FEMALE = 'F'
    VALID_NAME_1 = 'Krygin Ivan'
    VALID_BIRTHDAY_YEAR_1 = 1993
    VALID_BIRTHDAY_MONTH_1 = 04
    VALID_BIRTHDAY_DAY_1 = 28
    VALID_TEL_1 = '9037823414'
    VALID_EMAIL_1 = 'krygin.ia@gmail.com'

    VALID_NAME_2 = 'Petrov Alexandr'
    VALID_BIRTHDAY_YEAR_2 = 1979
    VALID_BIRTHDAY_MONTH_2 = 5
    VALID_BIRTHDAY_DAY_2 = 30
    VALID_TEL_2 = '4951111111'
    VALID_EMAIL_2 = 'example@mail.ru'

    BIRTHDAY_YEAR_IN_THE_FUTURE = 2099
    BIRTHDAY_MONTH_IN_THE_FUTURE = 12
    BIRTHDAY_DAY_IN_THE_FUTURE = 31

    LONG_NAME = "Very Very Very Very Very Very Very Very Very Very Very Very " \
                "Very Very Very Very Very Very Very Very Very Very Very Very " \
                "Very Very Very Very Very Very Very Very Very Very Long Name "

    INVALID_EMAIL = "InvalidEmail"
    SHORT_TEL = "123"
    LONG_TEL = "1234567890123"
    INVALID_TEL = "abcdefghij"