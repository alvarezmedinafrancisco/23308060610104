from flask import Flask , render_template, request , session
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('base.html')


@app.route('/base',methods=["GET", "POST"])
def calculadora():
    if request.method == "GET":
        grasas = request.form.get("grasas")
        proteinas = request.form.get("proteinas")
        carbohidratos = request.form.get("carbohidratos")
        return render_template('base.html')
    
    
@app.route("/clasificador", methods=["GET", "POST"])
def clasificador():
    if request.method =="POST":
        grasas = request.form.get("grasas")
        proteinas = request.form.get("proteinas")
        carbohidratos = request.form.get("carbohidratos")
        grasas == grasas*9
        proteinas == proteinas*4
        carbohidratos == carbohidratos*4
        session['alimentos_clasificados']
    return render_template("clasificador.html")



if __name__ == '__main__':
    app.run(debug=True)