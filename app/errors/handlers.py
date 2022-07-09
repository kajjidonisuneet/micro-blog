from flask import render_template
from app import db 
from app.errors import bp

@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404 # the secound parameter is the status code of the page, default is 200 hence it was not added for other pages

@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500 