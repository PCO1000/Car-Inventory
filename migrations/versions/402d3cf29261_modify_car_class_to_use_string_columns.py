"""Modify Car class to use String columns

Revision ID: 402d3cf29261
Revises: b22943bc906b
Create Date: 2024-01-17 13:48:30.552648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '402d3cf29261'
down_revision = 'b22943bc906b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)
        batch_op.alter_column('year',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=4),
               existing_nullable=True)
        batch_op.alter_column('price',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.String(length=20),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.String(length=20),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
        batch_op.alter_column('year',
               existing_type=sa.String(length=4),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('id',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###
