from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data/<int:num>')
def num(num):
    return render_template('two.html', data=num)


@app.route('/form', methods=['GET', 'POST'])
def form_data():
    if request.method == 'POST':
        context = {
            'login': request.form['login'],
            'password': request.form['password']
        }
        return render_template('form_data.html', **context)  # login = login, password = password
    else:
        return render_template('form_data.html')


if __name__ == '__main__':
    app.run(debug=True)
