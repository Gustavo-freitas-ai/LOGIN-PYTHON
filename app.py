from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'login_system'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        user = request.form["user"]
        password = request.form["password"]

        cursor = mysql.connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE user=%s AND password=%s",
            (user, password)
        )

        result = cursor.fetchone()
        cursor.close()

        if result:
            return redirect("/next")
        else:
            return "Login inválido"

    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        user = request.form["user"]
        password = request.form["password"]

        cursor = mysql.connection.cursor()

        cursor.execute(
            "INSERT INTO users (user, password) VALUES (%s,%s)",
            (user, password)
        )

        mysql.connection.commit()
        cursor.close()

        return redirect("/")

    return render_template("register.html")


@app.route("/next")
def next():
    return render_template("next.html")


if __name__ == "__main__":
    app.run(debug=True)