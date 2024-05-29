from flask import Blueprint, render_template
from .views.currency_view import convert_currency


def init_routes(app):
    bp = Blueprint('routes', __name__)

    @bp.route('/')
    def index():
        return render_template('index.html')

    bp.route('/convert', methods=['GET'])(convert_currency)
    app.register_blueprint(bp)
