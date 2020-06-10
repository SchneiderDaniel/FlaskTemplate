from flask import render_template, request, redirect, url_for, send_from_directory, flash, Blueprint, current_app
from webapp.main.forms import KeywordForm
from webapp import db
import os
from webapp.models import Keyword

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(current_app.root_path, 'static'), 'resources/img/favicon.ico', mimetype='image/vnd.microsoft.icon')


@main.route('/keywords', methods=['GET', 'POST'])
def keywords():
    form = KeywordForm()
    if form.validate_on_submit():
        keyword = Keyword(keyword = form.keyword.data)
        db.session.add(keyword)
        db.session.commit()
        flash(f'Thanks, we have added the keyword to the database', 'success')
        return redirect(url_for('main.index'))

    return render_template('keyword.html', form=form)