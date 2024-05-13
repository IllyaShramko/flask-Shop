import flask, flask_login

from registration_page.models import User
value = 0
value_tf = False
def render_shop_page():
    global value_tf, value
    if flask.request.method == "POST":
        value += 1
        if not value_tf:
            value_tf = True
            




    return flask.render_template(
        template_name_or_list= "shop.html",
        user = str(User.query.all()[0]).split("login: ")[1],
        value1 = value,
        valuetf = value_tf
    )