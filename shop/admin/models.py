from shop import db, app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(180))
    profile = db.Column(db.String(80), default='profile.jpg')
    
    def __repr__(self):
        return '<User %r>' % self.username
    
with app.app_context():
    db.create_all()
    