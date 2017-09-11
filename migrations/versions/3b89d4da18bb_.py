"""empty message

Revision ID: 3b89d4da18bb
Revises: 17b110e13938
Create Date: 2017-09-10 15:36:57.269160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b89d4da18bb'
down_revision = '17b110e13938'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('post_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'category', 'post', ['post_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'category', type_='foreignkey')
    op.drop_column('category', 'post_id')
    # ### end Alembic commands ###