from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from .constants import (CHECK_RE_ERROR_MESSAGE, CUSTOM_ID_CHECK_RE,
                        LENGTH_ERROR_MESSAGE)


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=(DataRequired(message='Обязательное поле'),
                    Length(1, 256))
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=(Optional(), Length(1, 16, message=LENGTH_ERROR_MESSAGE),
                    Regexp(CUSTOM_ID_CHECK_RE, message=CHECK_RE_ERROR_MESSAGE))
    )
    submit = SubmitField('Создать')
