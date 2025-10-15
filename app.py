from flask import Flask, render_template, request

app = Flask (__name__) 

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

@app.route("/inicia-sesion")
def sesion():
    return render_template ("inicia.html")

if __name__ =='__main__':
    app.run(debug=True)