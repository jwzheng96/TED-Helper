"""empty message

Revision ID: f5786a9b6001
Revises: 
Create Date: 2021-04-11 09:58:49.582341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5786a9b6001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ted',
    sa.Column('id', sa.String(length=256), nullable=False),
    sa.Column('sentence_id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=256), nullable=True),
    sa.Column('ted_content', sa.Text(), nullable=True),
    sa.Column('author_name', sa.String(length=256), nullable=True),
    sa.Column('ted_title', sa.String(length=256), nullable=True),
    sa.Column('image', sa.String(length=256), nullable=True),
    sa.Column('add_timestamp', sa.String(length=256), nullable=True),
    sa.Column('filmed_timestamp', sa.String(length=256), nullable=True),
    sa.Column('slug', sa.String(length=256), nullable=True),
    sa.Column('published_timestamp', sa.String(length=256), nullable=True),
    sa.Column('languages', sa.String(length=256), nullable=True),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('media_pad', sa.Integer(), nullable=True),
    sa.Column('media_slug', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id', 'sentence_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ted')
    # ### end Alembic commands ###