from flask import Flask , jsonify, request

from psycopg2.extras import RealDictCursor
from database import init_db
from routes.products import products








init_db()

app=Flask(__name__)

app.register_blueprint(products, url_prefix="/products")




@app.route("/")
@app.route("/<path:path>")
def serve_front_end():
    return app.send_static_file("index.html")

@app.route("/health")
def health():
    return jsonify({"message": "Server Online"})


if __name__ == "__main__":
    app.run(debug=True)


