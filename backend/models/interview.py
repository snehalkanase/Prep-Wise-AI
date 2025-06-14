from app import db
from datetime import datetime

class Interview(db.Model):
    id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    num_questions = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Add a relationship back to user
    user = db.relationship("User", backref="interviews")
