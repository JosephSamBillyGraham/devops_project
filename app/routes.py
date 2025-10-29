from flask import render_template, request, redirect, url_for

def register_routes(app):
    instruments = [
        {"name": "Guitar", "price": "$500", "image": "guitar.jpg"},
        {"name": "Drum Set", "price": "$1200", "image": "drums.jpg"},
        {"name": "Keyboard", "price": "$700", "image": "keyboard.jpg"},
    ]

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/products")
    def products():
        return render_template("products.html", instruments=instruments)

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/contact", methods=["GET", "POST"])
    def contact():
        if request.method == "POST":
            name = request.form.get("name")
            message = request.form.get("message")
            # In a real app, you’d send email or save to DB
            print(f"New contact: {name} - {message}")
            return redirect(url_for("home"))
        return render_template("contact.html")
