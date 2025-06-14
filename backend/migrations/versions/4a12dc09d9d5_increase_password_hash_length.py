"""Increase password_hash length

Revision ID: 4a12dc09d9d5
Revises: 2385c91d6ef3
Create Date: 2025-06-06 01:09:52.766158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a12dc09d9d5'
down_revision = '2385c91d6ef3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=512),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=512),
               type_=sa.VARCHAR(length=128),
               existing_nullable=False)

    # ### end Alembic commands ###
