"""users table

Revision ID: ada2915857ef
Revises: 
Create Date: 2020-06-11 18:51:16.486599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ada2915857ef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pull_request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_pr', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('title_rus', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pull_request')
    # ### end Alembic commands ###