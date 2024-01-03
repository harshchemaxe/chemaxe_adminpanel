from flask import Flask
from admin.routes import admin_bp



app = Flask(__name__)



app.register_blueprint(admin_bp)



if __name__ == "__main__":
	app.run(host='127.0.0.1', port=8081, debug=True)