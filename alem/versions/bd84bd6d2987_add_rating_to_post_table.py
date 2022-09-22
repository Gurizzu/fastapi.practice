"""add rating to post table

Revision ID: bd84bd6d2987
Revises: bf81afaee8ab
Create Date: 2022-09-22 12:51:36.427283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd84bd6d2987'
down_revision = 'bf81afaee8ab'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('post',
                  sa.Column('rating',sa.Integer, nullable=True, server_default='0'))
    pass


def downgrade() -> None:
    pass
