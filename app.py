from flask import Flask, render_template

app = Flask (__name__) 

@app.route("/")
def index():
    miembros =  ["Ramon Renteria","David Oaxaca","Jesús Nolasco"]
    return render_template ("index.html", creador="Oaxaca Orona David Adrián", nombres = miembros)

if __name__ =='__main__':
    app.run(debug=True)