import os
from flask import Flask
from dotenv import load_dotenv
from config import Config
from extensions import db, login_manager, csrf
from models import Admin


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    from routes.main import main_bp
    from routes.auth import auth_bp
    from routes.admin import admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(Admin, int(user_id))

    @app.cli.command("init-db")
    def init_db():
        db.create_all()
        print("Database tables created.")

    @app.cli.command("create-admin")
    def create_admin():
        email = os.getenv("ADMIN_EMAIL")
        password = os.getenv("ADMIN_PASSWORD")
        if not email or not password:
            print("Set ADMIN_EMAIL and ADMIN_PASSWORD in .env")
            return

        admin = Admin.query.filter_by(email=email.lower()).first()
        if not admin:
            admin = Admin(email=email.lower())
            db.session.add(admin)

        admin.set_password(password)
        db.session.commit()
        print("Admin ready:", email)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG") == "1")
