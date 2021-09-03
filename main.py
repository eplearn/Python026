from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text, nullable=False)
    time = db.Column(db.String(30), nullable=False)


def get_date_and_time():
    return datetime.now().strftime('%d-%m-%Y %H:%M:%S')


@app.route('/', methods=['GET', 'POST'])
def index():
    tasks = Task.query.all()

    if request.method == 'POST':
        try:
            id = int(request.form['id'])
            Task.query.filter_by(id=id).delete()
            db.session.commit()
        except:
            return 'Что-то сломалось'
        return redirect(request.url)
    else:
        return render_template('main.html', data=tasks)


@app.route('/create_task', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        if not name or not description:
            return render_template('create_task.html', error='Введите данные нормально!')

        task = Task(name=name, description=description, time=get_date_and_time())

        try:
            db.session.add(task)
            db.session.commit()
            return redirect('/create_task')
        except:
            return 'Что-то сломалось'
    else:
        return render_template('create_task.html')


if __name__ == '__main__':
    app.run(debug=True)
