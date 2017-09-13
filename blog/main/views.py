from flask import  render_template

from . import main
from ..models import Tag,Post,Category
import markdown

@main.route('/')
def index():
    post_list=Post.query.all()
    return render_template('index.html',post_list=post_list)

@main.route('/post/<pk>')
def detail(pk):
    post=Post.query.get_or_404(pk)
    post.body=markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render_template('main/detail.html',post=post)




