from flask import Flask, request, render_template
import os

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/contacto', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        return ""
    else:
        return render_template('Contact.html')
    


@app.route('/your_name', methods=['GET','POST'])
def your_name():
    if request.method == 'POST':
        return ""
    else:
        return render_template('series/Your_Name.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
