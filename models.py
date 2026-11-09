from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db

class Admin(UserMixin, db.Model):
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash=db.Column(db.String(255), nullable=False)
    is_active_admin=db.Column(db.Boolean, default=True, nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    def set_password(self,p): self.password_hash=generate_password_hash(p)
    def check_password(self,p): return check_password_hash(self.password_hash,p)

class Booking(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    reference_id=db.Column(db.String(30), unique=True, nullable=False, index=True)
    name=db.Column(db.String(100), nullable=False)
    phone=db.Column(db.String(20), nullable=False)
    service=db.Column(db.String(100), nullable=False)
    appointment_date=db.Column(db.Date, nullable=False)
    appointment_time=db.Column(db.String(20), nullable=False)
    status=db.Column(db.String(50), default="Received", nullable=False)
    notes=db.Column(db.Text)
    created_at=db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

class Enquiry(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    phone=db.Column(db.String(20), nullable=False)
    service=db.Column(db.String(100), nullable=False)
    vehicle_number=db.Column(db.String(30))
    message=db.Column(db.Text)
    status=db.Column(db.String(30), default="New", nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
