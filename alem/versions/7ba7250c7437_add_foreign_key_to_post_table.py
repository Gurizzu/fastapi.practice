"""add foreign key to post table

Revision ID: 7ba7250c7437
Revises: 913c2d019b9a
Create Date: 2022-09-22 11:49:26.509443

"""
from tkinter import CASCADE
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ba7250c7437'
down_revision = '913c2d019b9a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('post',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk',
                          source_table='post',
                          referent_table='users',
                          local_cols=['owner_id'],
                          remote_cols=['id'],
                          ondelete='CASCADE')



def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name='post')
    op.drop_column('post','owner_id')
    pass
