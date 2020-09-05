from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class AddComment(FlaskForm):
    comment_title = StringField('Title', validators = [DataRequired(), Length(min=1, max=85)])
    comment_content = TextAreaField('Content', validators = [DataRequired(), Length(min=1)])
    comment_submit = SubmitField('Comment')

class AddArticle(FlaskForm):
    article_title = StringField('Title', validators = [DataRequired(), Length(min=1, max=85)])
    article_content = TextAreaField('Content', validators = [DataRequired(), Length(min=1)])
    article_category = StringField('Category', validators = [DataRequired(), Length(min=1)])
    article_submit = SubmitField('Add Article')
