from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask (__name__) 

app.config['SECRET_KEY']="OODAAXRTBTOPSOPM"

@app.route("/")
def index():
    return render_template ("index1.html")

@app.route("/tiempo-nurburgring")
def tiempo():
    return render_template ("autos.html")

@app.route("/maravillas-del-mundo")
def maravillas():
    return render_template ("maravillas.html")

@app.route("/animales-exoticos")
def animales():
    return render_template ("animales.html")

@app.route("/acerca-de")
def acecade():
    return render_template ("acercade.html")

@app.route("/registrate")
def registro():
    return render_template ("registro.html")

@app.route("/registrame", method =("GET","POST"))
def registrame():
    error = None
    if request.method == "POST":
        nombrecompleto = request.form["name"]
        apellido = request.form["apellido"]
        email = request.form["email"]
        contraseña = request.form["Contraseña"]
        confirmarcontra = request.form["confirmarcontra"]
        fecha_de_nacimiento = request.form["Dia"]
        gener = request.form["genero"]
        
        if contraseña != confirmarcontra:
            error = "La contraseña no coincide"
        if error != None:
            flash(error)
            return  render_template("registro.html")
        else:
            flash(f"¡Resgistro exitoso para el usuario:{nombrecompleto}!")
            return render_template("index1.html")

@app.route("/inicia-sesion")
def sesion():
    return render_template ("inicia.html")

if __name__ =='__main__':
    app.run(debug=True)