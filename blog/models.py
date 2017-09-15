# coding:utf-8
from . import db
from datetime import datetime

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    # 其他数据类型 http://flask-sqlalchemy.pocoo.org/2.1/models/?highlight=string
    name=db.Column(db.String(100))
    # 打印一个对象的时候会用对象里的__repr__函数进行格式化后再输出,__repr__一般会返回一个可以作为代码执行的字符串
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

    def __init__(self,title,body,modified_time,create_time=None):
        self.title=title
        self.body=body
        if create_time is None:
            self.create_time=datetime.utcnow()
        self.modified_time=modified_time

    def __repr__(self):
        return '<User %r>' % self.title


class Comment(db.Model):
    __tablename__ = 'Comment'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))
    context=db.Column(db.Text)
    create_time=db.Column(db.DateTime(),default=datetime.utcnow)

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    post = db.relationship(Post, backref=db.backref('comment_post', lazy='dynamic'))
    def __repr__(self):
        return '<User %r>' % self.title
