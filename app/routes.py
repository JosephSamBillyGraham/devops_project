from flask import render_template

def register_routes(app):
    @app.route("/")
    def home():
        instruments = [
            {"name": "Guitar", "price": "$500"},
            {"name": "Drum Set", "price": "$1200"},
            {"name": "Keyboard", "price": "$700"},
        ]
        return render_template("index.html", instruments=instruments)
