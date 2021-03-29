"""empty message

Revision ID: 7633d8fe5c8d
Revises: 0b750a01325f
Create Date: 2021-03-26 18:42:18.597866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7633d8fe5c8d'
down_revision = '0b750a01325f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('users_username_key', 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_username_key', 'users', type_='unique')
    # ### end Alembic commands ###