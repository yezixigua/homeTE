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
from db.model import User

# main = Blueprint('index', __name__)
# 需要查一下原本的参数index是什么意思
main = Blueprint('', __name__)
User.init_data()


@main.route("/")
def index():
    print(request.remote_addr)
    return render_template('index.html')


@main.route("/login", methods=['POST', 'GET'])
def login():
    print(request.remote_addr)
    # get 方法访问，说明是主页连接过来，返回login页面
    if request.method == 'GET':
        return render_template('login.html')
    # 如果是POST方法访问过来，说明是当前页面提交的登录请求
    if request.method == 'POST':
        print(request)
        print(request.form)
        name = request.form.get('name')
        password = request.form.get('password')
        valid_user = User.is_valid_user(name, password)
        if valid_user:
            return render_template('controler.html')
        else:
            return '错误登录'
        # return render_template(url_for('.index'))


@main.route("/register", methods=['POST', 'GET'])
def register():
    print(request.remote_addr)
    # get 方法访问，说明是主页连接过来，返回login页面
    if request.method == 'GET':
        return render_template('register.html')
    # 如果是POST方法访问过来，说明是当前页面提交的登录请求
    if request.method == 'POST':
        print(request)
        print(request.form)
        name = request.form.get('username')
        phone = request.form.get('user-phone')
        email = request.form.get('user-email')
        password = request.form.get('user-pwd')
        new_user = User(name=name, pwd=password, email=email, phone=phone)
        new_user.add()
        return render_template('login.html')


@main.route("/controler")
def controler():
    print(request.remote_addr)
    return render_template('controler.html')


@main.route("/elements")
def elements():
    print(request.remote_addr)
    return render_template('ui-elements.html')


@main.route("/chart")
def chart():
    print(request.remote_addr)
    return render_template('chart.html')


@main.route("/panel")
def panel():
    print(request.remote_addr)
    return render_template('tab-panel.html')


@main.route("/table")
def table():
    print(request.remote_addr)
    return render_template('table.html')


@main.route("/form")
def form():
    print(request.remote_addr)
    return render_template('form.html')


@main.route("/contact")
def contact():
    print(request.remote_addr)
    return render_template('contact-us.html')
