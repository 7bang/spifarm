from flask import Blueprint, url_for
from werkzeug.utils import redirect
from spifarm.models import Question

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/hello")
def hello():
    return "hello,pybo!?!"


@bp.route("/")
def index():
    return redirect(url_for('question._list'))
