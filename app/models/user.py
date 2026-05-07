from app.core.extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255))
    role = db.Column(db.String(50), default='talent') # admin, talent, client
    
    # Professional Details
    profession = db.Column(db.String(150))
    years_experience = db.Column(db.Integer)
    leadership_experience = db.Column(db.Integer) # Years in leadership
    senior_mgmt_experience = db.Column(db.Integer) # Years in senior mgmt
    biggest_projects = db.Column(db.Text) # Summary of major projects
    
    # File Paths (Stored as strings pointing to the uploads folder)
    cv_filename = db.Column(db.String(255))
    nrc_filename = db.Column(db.String(255))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)