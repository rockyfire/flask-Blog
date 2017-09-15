from flask import  render_template,redirect,url_for
from . import main
from ..models import Tag,Post,Category
import markdown
from ..forms import AddPostForm,CommentForm
from datetime import datetime
from .. import db

@main.route('/')
def index():
    post_list=Post.query.order_by("create_time desc").all()
    category_list=Category.query.all()
    return render_template('index.html',post_list=post_list,category_list=category_list)

@main.route('/category/<pk>')
def category(pk):
    cate=Category.query.get_or_404(pk)
    post_list=cate.post_category
    return render_template('index.html',post_list=post_list)

@main.route('/post/<pk>')
def detail(pk):
    post=Post.query.get_or_404(pk)
    comment_list = post.comment_post
    post.body=markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    form=CommentForm()
    return render_template('main/detail.html',post=post,comment_list=comment_list,form=form)


@main.route('/add',methods=['GET','POST'])
def add_post():
    form = AddPostForm()
    if form.validate_on_submit():
        p=Post(
            form.title.data,
            form.body.data,
            datetime.utcnow(),
        )
        p.category_id=form.category.data
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('main/add.html',form=form)