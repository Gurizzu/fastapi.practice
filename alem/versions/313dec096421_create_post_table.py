"""create post table

Revision ID: 313dec096421
Revises: 
Create Date: 2022-09-22 10:47:07.932053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '313dec096421'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('post', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    


def downgrade() -> None:
    op.drop_table('post')
