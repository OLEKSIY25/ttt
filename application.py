from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/fun", methods=["GET"])
def kankul():
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    sym=a+b
    riz=a-b
    dob=a*b
    chas=a/b
    return render_template("index.html", a=a, b=b, sym=sym, riz=riz, dob=dob, chas=chas)
