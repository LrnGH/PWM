"""inicial

Revision ID: a1836596a30f
Revises: 
Create Date: 2023-11-03 21:25:33.637602

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1836596a30f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('Users',
         sa.Column( 'id', sa.Integer, primary_key=True, autoincrement=True),
         sa.Column('name', sa.String, nullable=False),
         sa.Column('number', sa.Integer, nullable=False)
    )
    

def downgrade():
    op.drop_table('Users')
