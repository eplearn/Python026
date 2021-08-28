from flask import Flask, render_template
from datetime import datetime
from tabulate import tabulate


app = Flask(__name__)


def get_date_and_time():
    return datetime.now().strftime('%d-%m-%Y %H:%M:%S')


def get_prog_day():
    current_datetime = datetime.now().year
    if current_datetime % 400 == 0:
        return f'12.09{current_datetime}'
    else:
        return f'13-09-{current_datetime}'


def get_mul_table(n):
    arr_outer = []
    for i in range(1, n+1):
        arr_inner = []
        for j in range(1, n+1):
            arr_inner.append(i * j)
        arr_outer.append(arr_inner)
    return tabulate(arr_outer, tablefmt="html")


@app.route('/')
def index():
    return render_template('index.html', date=get_date_and_time(), prog_day=get_prog_day(), table=get_mul_table(10))


if __name__ == '__main__':
    app.run(debug=True)
