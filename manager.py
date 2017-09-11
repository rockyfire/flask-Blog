#!/user/bin/env python

import os
from blog import create_blog,db
from blog.models import *

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


blog=create_blog(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(blog)
migrate = Migrate(blog,db)

def make_shell_context():
    return dict(blog=blog,db=db,
                # User=User,Role=Role
                Category=Category,Tag=Tag,
                Post=Post
                )
manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    # blog.run(Debug=True)
    manager.run()