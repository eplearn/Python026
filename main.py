from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from cloudipsp import Api, Checkout

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return str(self.name)

# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/data/<int:num>')
# def num(num):
#     return render_template('two.html', data=num)
#
#
# @app.route('/form', methods=['GET', 'POST'])
# def form_data():
#     if request.method == 'POST':
#         context = {
#             'login': request.form['login'],
#             'password': request.form['password']
#         }
#         return render_template('form_data.html', **context)  # login = login, password = password
#     else:
#         return render_template('form_data.html')

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', data=products)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']

        product = Product(name=name, description=description, price=price)

        try:
            db.session.add(product)
            db.session.commit()
            return redirect('/create')
        except:
            return 'Что-то сломалось'
    else:
        return render_template('create.html')


@app.route('/buy/<int:id>')
def buy_product(id):
    product = Product.query.get(id)

    # merchant_id, secret_key <- after registration
    # merchant_id, secret_key from file (security)
    api = Api(merchant_id=1396424,
              secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "RUB",
        "amount": str(product.price) + '00'
    }
    url = checkout.url(data).get('checkout_url')

    return redirect(url)


@app.route('/delete/<int:id>')
def delete_product(id):
    Product.query.filter(Product.id == id).delete()
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
