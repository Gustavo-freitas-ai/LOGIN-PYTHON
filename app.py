from flask import Flask, render_template, request, redirect

app = Flask(__name__)

user_ = "user"
password_ = "password"


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        user = request.form["user"]
        senha_digitada = request.form["password"]

        if user == user_ and senha_digitada == password_:
            return redirect("/next")
        else:
            return "Login inválido"

    return render_template("index.html")


@app.route("/next")
def next():
    return render_template("next.html")


app.run(debug=True)