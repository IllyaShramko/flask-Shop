import flask
from registration_page.models import User

def render_cart_page():
    if flask.request.cookies:
        list_id_products = flask.request.cookies.get('products').split(' ')

        list_products = [[]]
        list_same_id = []
        # count_products = [[]]
        for id_product in list_id_products:
            list_products[-1].append(list_id_products.count(id_product))
            if id_product not in list_same_id:
                if id_product == "1":
                    list_products[-1].append("iPhone")
                elif id_product == "2":
                    list_products[-1].append("Vivo")
                list_same_id.append(id_product)
                list_products.append([])
                
                # list_products[-1] = count_products 
                       
        return flask.render_template(template_name_or_list = "cart.html", products = list_products)
    else:
        return flask.render_template(template_name_or_list = "cart.html")