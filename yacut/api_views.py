import re

from flask import jsonify, request

from . import app, db
from .constants import (CUSTOM_ID_CHECK_RE, REQUEST_INV_CUSTOM_ID_MESSAGE,
                        REQUEST_INV_SHORT_ID_MESSAGE, REQUEST_INV_URL_MESSAGE,
                        REQUEST_NO_DATA_MESSAGE, REQUEST_NO_URL_MESSAGE,
                        REQUEST_UNIQUE_CUSTOM_ID_MESSAGE, URL_CHECK_RE)
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/', methods=('POST',))
def add_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(REQUEST_NO_DATA_MESSAGE)

    url = data.get('url')
    custom_id = data.get('custom_id')

    if not url:
        raise InvalidAPIUsage(REQUEST_NO_URL_MESSAGE)
    if not re.match(URL_CHECK_RE, url):
        raise InvalidAPIUsage(REQUEST_INV_URL_MESSAGE)

    if custom_id:
        if len(custom_id) > 16:
            raise InvalidAPIUsage(REQUEST_INV_CUSTOM_ID_MESSAGE, 400)
        if URLMap.query.filter_by(short=custom_id).first() is not None:
            raise InvalidAPIUsage(
                REQUEST_UNIQUE_CUSTOM_ID_MESSAGE.format(custom_id)
            )
        if not re.match(CUSTOM_ID_CHECK_RE, custom_id):
            raise InvalidAPIUsage(REQUEST_INV_CUSTOM_ID_MESSAGE)

    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()

    return jsonify(url_map.to_dict(request.root_url)), 201


@app.route('/api/id/<short_id>/', methods=('GET',))
def get_url(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is None:
        raise InvalidAPIUsage(REQUEST_INV_SHORT_ID_MESSAGE, 404)
    return jsonify({'url': url_map.get_original_url()}), 200
