# coding:utf-8
from . import db
from datetime import datetime

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    # 其他数据类型 http://flask-sqlalchemy.pocoo.org/2.1/models/?highlight=string
    name=db.Column(db.String(100))
    def __repr__(self):
        return '<User %r>' % self.name


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    def __repr__(self):
        return '<User %r>' % self.name

tag_post=db.Table('tag_post',
                  db.Column('tag_id',db.Integer,db.ForeignKey('tag.id')),
                  db.Column('post_id',db.Integer,db.ForeignKey('post.id')),
                  )

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(70))
    body=db.Column(db.Text)
    create_time=db.Column(db.DateTime)
    modified_time=db.Column(db.DateTime)
    excerpt=db.Column(db.String(200),nullable=True)

    category_id=db.Column(db.Integer,db.ForeignKey('category.id'),nullable=False)
    category=db.relationship(Category,backref=db.backref('post_category',lazy='dynamic'))

    tag=db.relationship(Tag,secondary=tag_post,
                        backref=db.backref("post_tag",lazy='dynamic'))

    def __init__(self,title,body,modified_time,category,create_time=None):
        self.title=title
        self.body=body
        if create_time is None:
            self.create_time=datetime.utcnow()
        self.modified_time=modified_time
        self.category=category

    def __repr__(self):
        return '<User %r>' % self.title

    def get_recent_posts(num=5):
        return Post.query.all().order_by('-created_time')[:num]















