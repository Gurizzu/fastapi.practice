"""add few column to post table

Revision ID: bf81afaee8ab
Revises: 7ba7250c7437
Create Date: 2022-09-22 12:35:13.086802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf81afaee8ab'
down_revision = '7ba7250c7437'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('post',sa.Column(
        'published', sa.Boolean(), nullable=False,server_default= 'TRUE'),)
    op.add_column('post',
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()'),))
    
    pass


def downgrade() -> None:
    op.drop_column("post",'published')
    op.drop_column("post",'created_at')
    pass
