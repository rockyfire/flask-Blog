from flask_wtf import  FlaskForm
from wtforms import StringField,SubmitField,DateField,IntegerField,TextAreaField,SelectMultipleField,TextField
from wtforms.validators import Required,Email
from blog.models import Category,Post,Tag,Comment

class AddPostForm(FlaskForm):
    title=StringField('文章标题',validators=[Required()])
    body=TextAreaField('文章内容',validators=[Required()])
    create_time=DateField("创建日期")
    modified_time=DateField("修改日期")
    category=SelectMultipleField('类型',coerce=int)
    def __init__(self):
        super(AddPostForm, self).__init__()
        self.category.choices=[(c.id,c.name) for c in Category.query.order_by('id')]

class CommentForm(FlaskForm):
    name = StringField('评论者', validators=[Required()])
    email = StringField('评论者电子邮件', validators=[Email()])
    context = TextField('评论内容',validators=[Required()])
    # submit=SubmitField('Submit')
