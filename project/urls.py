from .settings import project
import home_page, registration_page, login_page, shop_page

home_page.home_page.add_url_rule(
    rule = "/",
    view_func = home_page.render_home_page,
    methods = ["GET", "POST"]
)
project.register_blueprint(
    blueprint = home_page.home_page
)
registration_page.register_page.add_url_rule(
    rule= "/registration/",
    view_func= registration_page.render_registration,
    methods = ["GET", "POST"]
)
project.register_blueprint(blueprint= registration_page.register_page)

login_page.login_page.add_url_rule(
    rule= "/login/",
    view_func= login_page.render_login_page,
    methods = ["GET", "POST"]
)
project.register_blueprint(blueprint= login_page.login_page)

shop_page.shop_page.add_url_rule(
    rule= "/shop/",
    view_func= shop_page.render_shop_page,
    methods = ["GET", "POST"]
)
project.register_blueprint(blueprint= shop_page.shop_page)
