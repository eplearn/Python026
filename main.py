import sqlite3

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
            "name": str(request.values.get("name")) + " Ivanov",
            "email": str(request.values.get("email")),
            "phone": str(request.values.get("phone"))
        }

        cursor.execute(f"insert into customer (name, email, phone) "
                       f"values (\"{context['name']}\", \"{context['email']}\","
                       f" \"{context['phone']}\")")
        # Сохранение записи в б.д.:
        connection.commit()
        return render_template("users.html", **context)

    return render_template("users.html")


if __name__ == '__main__':
    app.run()
