from blog import db
from datetime import datetime

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.String, nullable = False)
    date_posted = db.Column(db.DateTime, default = datetime.utcnow)
    comments = db.relationship('Comment')
    category = db.Column(db.String(25), nullable = False)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.String, nullable = False)
    date_posted = db.Column(db.DateTime, default = datetime.utcnow)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
