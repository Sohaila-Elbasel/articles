from blog import app, db
from blog.models import Article, Comment
from blog.forms import AddArticle, AddComment
from flask import render_template

@app.route('/')
def home():
    articles = Article.query.all()
    return render_template('home.html', articles = articles)


@app.route('/article/<int:article_id>')
def article(article_id):
    form = AddComment()
    article = Article.query.get(article_id)
    return render_template('article.html', article = article, form = form)
