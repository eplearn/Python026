import sqlite3
# from crypt import methods

from Tools.scripts.make_ctype import method
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template')


# connection = sqlite3.connect("shop.sqlite")
# cursor = connection.cursor()
# cursor.execute("select * from customer")
# result = cursor.fetchall()
# print(result)

# Формирование записи в б.д.:
# cursor.execute("insert into customer (name, email, phone) values ('Vasya', '123e@gmail.com', '+123456789')")
# Печать результата запроса:
# cursor.execute("select * from customer")
# result = cursor.fetchall()
# print(result)
# Сохранение записи в б.д.:
# connection.commit()


@app.route('/')
def index():
    context = {'number': 1029}
    return render_template("index.html", **context)


@app.route('/users', methods=["GET", "POST"])
def userAdd():
    connection = sqlite3.connect("shop.sqlite")
    cursor = connection.cursor()
    if request.method == 'POST':
        # Проверка на None при использовании GET запросов.
        # if request.args.get("name") is not None \
        #         and request.args.get("email") is not None \
        #         and request.args.get("phone") is not None:

        context = {
            "name": str(request.form.get("name")) + " Ivanov",
            "email": str(request.form.get("email")),
            "phone": str(request.form.get("phone"))
        }

        cursor.execute(f"insert into customer (name, email, phone) "
                       f"values (\"{context['name']}\", \"{context['email']}\","
                       f" \"{context['phone']}\")")
        # Сохранение записи в б.д.:
        connection.commit()
        return render_template("users.html", **context)

    return render_template("users.html")


@app.route('/product', methods=['GET', 'POST'])
def add_product():
    connection = sqlite3.connect("shop.sqlite", isolation_level=None)
    cursor = connection.cursor()
    if request.method == 'POST':
        data = {
            "name": str(request.form.get("name")),
            "description": str(request.form.get("description")),
            "price": str(request.form.get("price"))
        }
        create_record(cursor, data)
        return render_template("add_product.html", **data)
    return render_template('add_product.html')


def create_record(cursor, data):
    cursor.execute(
        f"insert into product (name, description, price) "
        f"values (\"{data['name']}\", \"{data['description']}\","
        f" \"{data['price']}\")"
    )


if __name__ == '__main__':
    app.run()
