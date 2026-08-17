from flask import Flask, render_template, request
from compounds import show_compounds
from analyzer import show_statistics, compare_compounds

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/compounds")
def compounds_page():
    data = show_compounds()
    return render_template("compounds.html", compounds=data)

@app.route("/statistics")
def statistics_page():
    stats = show_statistics()
    return render_template("statistics.html", stats=stats)

@app.route("/compare")
def compare_page():
    c1 = request.args.get("c1")
    c2 = request.args.get("c2")
    result = compare_compounds(c1, c2)
    return f"<pre>{result}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
