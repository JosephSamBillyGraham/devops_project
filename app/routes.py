from flask import render_template, session, redirect, url_for

def register_routes(app):
    instruments = [
        {"id": 1, "name": "Guitar", "price": 500, "image": "guitar.jpg"},
        {"id": 2, "name": "Drum Set", "price": 1200, "image": "drums.jpg"},
        {"id": 3, "name": "Keyboard", "price": 700, "image": "keyboard.jpg"},
    ]

    @app.route("/")
    def home():
        return render_template("index.html", instruments=instruments)

    @app.route("/add_to_cart/<int:item_id>")
    def add_to_cart(item_id):
        item = next((i for i in instruments if i["id"] == item_id), None)
        if not item:
            return redirect(url_for("home"))

        cart = session.get("cart", [])
        cart.append(item)
        session["cart"] = cart
        return redirect(url_for("cart"))

    @app.route("/cart")
    def cart():
        cart = session.get("cart", [])
        total = sum(item["price"] for item in cart)
        return render_template("cart.html", cart=cart, total=total)

    @app.route("/remove_from_cart/<int:item_id>")
    def remove_from_cart(item_id):
        cart = session.get("cart", [])
        cart = [item for item in cart if item["id"] != item_id]
        session["cart"] = cart
        return redirect(url_for("cart"))
