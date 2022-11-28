from flask import abort, flash, redirect, render_template, request

from . import app, db
from .constants import NOT_UNIQUE_LINK_MESSAGE, SHORT_ID_LENGTH
from .forms import URLForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=('GET', 'POST'))
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if not custom_id:
            custom_id = get_unique_short_id(SHORT_ID_LENGTH)
        else:
            if URLMap.query.filter_by(short=custom_id).first():
                flash(NOT_UNIQUE_LINK_MESSAGE.format(custom_id), 'error')
                return render_template('index.html', form=form)

        url_map = URLMap(
            original=form.original_link.data,
            short=custom_id,
        )
        db.session.add(url_map)
        db.session.commit()
        flash(request.root_url + url_map.short, 'short_link')
    return render_template('index.html', form=form)


@app.route('/<short_url>')
def original_url_redirect_view(short_url):
    url_map = URLMap.query.filter_by(short=short_url).first()
    if not url_map:
        abort(404)
    redirect_url = url_map.get_original_url()
    return redirect(redirect_url, code=302)
