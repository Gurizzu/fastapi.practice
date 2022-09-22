"""add content to post table

Revision ID: e7fdfc7d00c6
Revises: 313dec096421
Create Date: 2022-09-22 11:19:40.226074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7fdfc7d00c6'
down_revision = '313dec096421'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('post', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('post', 'content')
    pass
