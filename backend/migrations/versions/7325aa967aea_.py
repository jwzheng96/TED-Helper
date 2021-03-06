"""empty message

Revision ID: 7325aa967aea
Revises: f5786a9b6001
Create Date: 2021-04-17 11:42:52.097130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7325aa967aea'
down_revision = 'f5786a9b6001'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ted', sa.Column('total_content', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ted', 'total_content')
    # ### end Alembic commands ###
