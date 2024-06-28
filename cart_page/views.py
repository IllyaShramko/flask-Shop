import flask, flask_login
from registration_page.models import User
from project.settings import DATABASE
from .models import Cart
from shop_page.models import Product
from project.flask_config import mail
import flask_mail
count_of_products= None
valuetf= None
def render_cart_page():
    global count_of_products, valuetf
    check_basket = False
    valuetf = True
    if flask.request.method == "POST":
        try:
            list_id_products = flask.request.cookies.get('products').split(' ')
            list_products = []
            list_same_id = []
            for id_product in list_id_products:
                for product in Product.query.all():
                    if id_product not in list_same_id:
                        if id_product == product.id:
                            list_products[-1].append(product.name)
                        list_same_id.append(id_product)
            count_of_products = [[]]
            for cart_product in list_products:
                for product in Product.query.all():
                    if cart_product == product.name:
                        if count_of_products != None:
                            count_of_products[product.id] += 1
                        else:
                            count_of_products[product.id].append(1)
                            count_of_products[product.id].append(product.name)
            text_message1 = f"Hello Admin. Your customer {flask.request.form['orderName']} {flask.request.form['orderSurname']} maked order, he's cart has:\n"
            for product in count_of_products:
                if text_message1.split(":")[-1] != "" or text_message1.split(":")[-1] != "":
                    text_message1 += ',' + product[0] + product[1]
                else:
                    text_message1 += product[0] + product[1]
            try:
                text_message = flask_mail.Message(
                    subject = text_message1,
                    recipients = ['123illya123123r@gmail.com'],
                    sender= flask.request.form['email']
                )
                mail.send(text_message)
            except:
                print("Анлак")
            new_product = Cart(
                name = flask.request.form['orderName'],
                surname = flask.request.form['orderSurname'],
                phone_number = flask.request.form['orderNumber'],
                email = flask.request.form['orderEmail'],
                city = flask.request.form['orderCity'],
                wishes = flask.request.form['orderWishes'],
                cart = flask.request.form[''],
                status = "in proccess",
            )
            DATABASE.session.add(new_product)
            DATABASE.session.commit() 

        except Exception as e:
            print(e)
    if flask.request.cookies:
        try:
            list_id_products = flask.request.cookies.get('products').split(' ')
            list_products = [[]]
            list_same_id = []
            # count_products = [[]]
            for id_product in list_id_products:
                for product in Product.query.all():

                    if id_product not in list_same_id:
                        if id_product == product.id:
                            list_products[-1].append(list_id_products.count(id_product))
                            list_products[-1].append(product.name)
                        list_same_id.append(id_product)
                        list_products.append([])
            check_basket = True
        except:
            list_products = [[0, "None"]]
        # count_of_products= 0
        
        is_admin = flask_login.current_user.is_admin
        return flask.render_template(
            template_name_or_list = "cart.html",
            products = list_products,
            check_basket = check_basket, 
            count_of_products = count_of_products,
            valuetf = valuetf,
            user = flask_login.current_user.login, is_admin = is_admin
        )
    else:
        return flask.render_template(template_name_or_list = "cart.html", check_basket = check_basket)
    