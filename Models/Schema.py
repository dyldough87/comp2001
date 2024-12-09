from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Trail(db.Model):
    __tablename__ = 'trails'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    difficulty = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Trail {self.name}>"
