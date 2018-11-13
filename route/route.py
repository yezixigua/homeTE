from flask import (
    render_template,
    request,
    redirect,
    session,
    url_for,
    Blueprint,
    make_response,
    send_from_directory,
)

main = Blueprint('index', __name__)


@main.route("/")
def hello_world():
    print(request.remote_addr)
    return render_template('index.html')