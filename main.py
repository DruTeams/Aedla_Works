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
    


#Series Aedla-World

@app.route('/your_name', methods=['GET','POST'])
def your_name():
    if request.method == 'POST':
        return ""
    else:
        return render_template('series/Your_Name.html')



@app.route('/Seishun_Buta_Yarō_wa_Yumemiru_Shōjo_no_Yume_wo_Minai')
def Seishun_Buta_Yarō_wa_Yumemiru_Shōjo_no_Yume_wo_Minai():
    if request.method == 'POST':
        return ""
    else:
        return render_template('series/Seishun_Buta_Yarō_wa_Yumemiru_Shōjo_no_Yume_wo_Minai.html')



@app.route('/Saekano_The_Movie', methods=['GET','POST'])
def saekano_the_movie():
    if request.method == 'POST':
        return ""
    else:
        return render_template('series/Saekano_The_Movie.html')







if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
