"""Add email & password columns to User

Revision ID: f7fa586dae1e
Revises: f3e0ad57311d
Create Date: 2020-03-13 17:37:26.432167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7fa586dae1e'
down_revision = 'f3e0ad57311d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=32), nullable=False))
    op.add_column('user', sa.Column('password', sa.String(length=128), nullable=False))
    op.create_unique_constraint(None, 'user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'password')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
