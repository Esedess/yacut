import os
import re

#Global
SHORT_ID_LENGTH = int(os.getenv('SHORT_ID_LENGTH', 6))
CUSTOM_ID_CHECK_RE = re.compile('[a-zA-Z0-9]+$')

#Forms
CHECK_RE_ERROR_MESSAGE = 'Указано недопустимое имя для короткой ссылки'
LENGTH_ERROR_MESSAGE = 'Вариант ссылки не должен превышать 16 символов.'

#Views
NOT_UNIQUE_LINK_MESSAGE = 'Имя {} уже занято!'

#Api_views
URL_CHECK_RE = re.compile(
    r'[A-Za-z0-9]+://[A-Za-z0-9%-_]+(/[A-Za-z0-9%-_])*(#|\\?)[A-Za-z0-9%-_&=]*'
)
REQUEST_NO_DATA_MESSAGE = 'Отсутствует тело запроса'
REQUEST_NO_URL_MESSAGE = '"url" является обязательным полем!'
REQUEST_INV_URL_MESSAGE = 'Указана не ссылка'
REQUEST_UNIQUE_CUSTOM_ID_MESSAGE = 'Имя "{}" уже занято.'
REQUEST_INV_CUSTOM_ID_MESSAGE = 'Указано недопустимое имя для короткой ссылки'
REQUEST_INV_SHORT_ID_MESSAGE = 'Указанный id не найден'