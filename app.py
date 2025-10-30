from flask import Flask , render_template, request , session
app = Flask(__name__)

@app.route('/base')
def inicio():
    return render_template('base.html')


@app.route('/base',methods=["GET", "POST"])
def calculadora():
    if request.method == "POST":
        gras = request.form.get("grasas")
        pro = request.form.get("proteinas")
        car = request.form.get("carbohidratos")
        session['alimentos_clasificados']
    return render_template("base.html" , prote = pro , carbo = car , gra = gras)

@app.route("/clasificador", methods=["GET", "POST"])
def nose():
    return render_template("clasificador.html")



if __name__ == '__main__':
    app.run(debug=True)