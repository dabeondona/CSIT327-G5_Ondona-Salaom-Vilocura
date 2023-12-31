"""Inital migration.

Revision ID: 043fd7b6b959
Revises: 
Create Date: 2023-12-22 23:26:29.737168

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '043fd7b6b959'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tbl_user')
    with op.batch_alter_table('appliances', schema=None) as batch_op:
        batch_op.add_column(sa.Column('appliance_quantity', sa.Integer(), nullable=True))

    with op.batch_alter_table('furniture', schema=None) as batch_op:
        batch_op.add_column(sa.Column('furniture_quantity', sa.Integer(), nullable=True))

    with op.batch_alter_table('shoes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('shoes_quantity', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('shoes', schema=None) as batch_op:
        batch_op.drop_column('shoes_quantity')

    with op.batch_alter_table('furniture', schema=None) as batch_op:
        batch_op.drop_column('furniture_quantity')

    with op.batch_alter_table('appliances', schema=None) as batch_op:
        batch_op.drop_column('appliance_quantity')

    op.create_table('tbl_user',
    sa.Column('id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=255), nullable=True),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
