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
def index():
    print(request.remote_addr)
    return render_template('index.html')


@main.route("/login")
def login():
    print(request.remote_addr)
    return render_template('register.html')


@main.route("/about")
def about():
    print(request.remote_addr)
    return render_template('about-us.html')


@main.route("/blog")
def blog():
    print(request.remote_addr)
    return render_template('blog.html')


@main.route("/cart")
def cart():
    print(request.remote_addr)
    return render_template('cart.html')


@main.route("/product")
def product():
    print(request.remote_addr)
    return render_template('product.html')


@main.route("/products")
def products():
    print(request.remote_addr)
    return render_template('products.html')


@main.route("/contact")
def contact():
    print(request.remote_addr)
    return render_template('contact-us.html')
