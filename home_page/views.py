import flask, flask_login

from registration_page.models import User
def render_home_page():
    return flask.render_template(
        template_name_or_list= "home.html",
        is_auth = flask_login.current_user.is_authenticated,
        user = str(User.query.all()[0]).split("login: ")[1]
)