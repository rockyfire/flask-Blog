from flask import  render_template,redirect,url_for
from . import comment
from ..models import Tag,Post,Category,Comment
import markdown
from ..forms import CommentForm
from datetime import datetime
from .. import db

@comment.route('/post/<post_pk>',methods=['GET','POST'])
def post_comment(post_pk):
    post=Post.query.get_or_404(post_pk)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment()
        comment.name=form.name.data
        comment.email=form.email.data
        comment.context=form.context.data
        comment.post_id=post_pk
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.index'))
    return redirect('main/detail.html')
