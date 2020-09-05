from blog import app, db
from blog.models import Article, Comment
from blog.forms import AddArticle, AddComment
from flask import render_template, redirect, url_for

@app.route('/')
def home():
    articles = Article.query.all()
    return render_template('home.html', articles = articles)


@app.route('/article/<int:article_id>', methods=['POST', 'GET'])
def article(article_id):
    form = AddComment()
    article = Article.query.get(article_id)

    #display comments
    comments = Comment.query.all()

    #Add comment
    if form.validate_on_submit():
        comment = Comment(title=form.comment_title.data, content = form.comment_content.data, article_id = article_id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('article', article_id = article_id))

    return render_template('article.html', article = article, form = form, comments = comments)
