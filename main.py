from flask import Flask, render_template

app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    context = {'number': 1029}
    return render_template("index.html", **context)


if __name__ == '__main__':
    app.run()
