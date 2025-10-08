from flask import Flask, render_template

app = Flask (__name__) 

@app.route("/")
def index():
    return render_template ("index1.html")

@app.route("/tiempo-nurburgring")
def tiempo():
    return render_template ("autos.html")

@app.route("/maravillas-del-mundo")
def maravillas():
    return render_template ("index1.html")

@app.route("/animales-exoticos")
def animales():
    return render_template ("index1.html")

@app.route("/acerca-de")
def acecade():
    return render_template ("index1.html")

if __name__ =='__main__':
    app.run(debug=True)