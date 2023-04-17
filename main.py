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



@app.route('/Fire-Works', methods=['GET','POST'])
def Fire_Works():
    if request.method == 'POST':
        return ""
    else:
        return render_template ('series/Fire_Works.html')



@app.route('/K-On', methods=['GET','POST'])
def K_On():
    if request.method == 'POST':
        return ""
    else:
        return render_template ('series/K-On_The_Movie.html')



@app.route('/Hello-World', methods=['GET','POST'])
def Hello_World():
    if request.method == 'POST':
        return ""
    else:
        return render_template ('series/Hello_World.html')



@app.route('/Kimi_no_Suizou_wo_Tabetai', methods=['GET','POST'])
def Kimi_no_Suizou_wo_Tabetai():
    if request.method == 'POST':
        return ""
    else:
        return render_template ('series/Kimi_no_Suizou_wo_Tabetai.html')



@app.route('/A_Silent_Voice', methods=['GET','POST'])
def A_Silent_Voice():
    if request.method == 'POST':
        return ""
    else:
        return render_template ('series/A_Silent_Voice.html')



@app.route('/Weathering_With_You', methods=['GET','POST'])
def Weathering_With_You():
    if request.method == 'POST':
        return ""
    else:
        return render_template ('series/Weathering_With_You.html')



@app.route('/The_Garden_Of_Words', methods=['GET','POST'])
def The_Garden_Of_Words():
    if request.method == 'POST':
        return ""
    else:
        return render_template ('series/The_Garden_Of_Words.html')



@app.route('/Five_Centimeters_Per_Second', methods=['GET','POST'])
def Five_Centimeters_Per_Second():
    if request.method == 'POST':
        return ""
    else:
        return render_template ('series/Five_Centimeters_Per_Second.html')
    
    The_Anthemofthe_Heart.html

@app.route('/The_Anthemofthe_Heart', methods=['GET','POST'])
def The_Anthemofthe_Heart():
    if request.method == 'POST':
        return ""
    else:
        return render_template ('series/The_Anthemofthe_Heart.html')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
