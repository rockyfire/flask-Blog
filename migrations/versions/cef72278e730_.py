"""empty message

Revision ID: cef72278e730
Revises: 9a15871c3e18
Create Date: 2017-09-11 14:48:45.755409

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cef72278e730'
down_revision = '9a15871c3e18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag_post')
    op.add_column('post', sa.Column('tag_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'post', 'tag', ['tag_id'], ['id'])
    op.add_column('tag', sa.Column('post_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tag', 'post', ['post_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tag', type_='foreignkey')
    op.drop_column('tag', 'post_id')
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_column('post', 'tag_id')
    op.create_table('tag_post',
    sa.Column('tag_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('post_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], name='tag_post_ibfk_1'),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], name='tag_post_ibfk_2'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
