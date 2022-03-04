from flask import render_template, Flask

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    prof = prof.split()
    return render_template('simulator.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
