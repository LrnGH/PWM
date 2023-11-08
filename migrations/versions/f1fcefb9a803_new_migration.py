"""New Migration

Revision ID: f1fcefb9a803
Revises: 
Create Date: 2023-11-05 17:13:53.466802

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f1fcefb9a803'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('Users',
         sa.Column( 'id', sa.Integer, primary_key=True, autoincrement=True),
         sa.Column('name', sa.String, nullable=False),
         sa.Column('number', sa.String, nullable=False)
    )
     
    op.create_table('Messages',
         sa.Column( 'id', sa.Integer, primary_key=True, autoincrement=True),
         sa.Column('Message', sa.String, nullable=False),
    )
    

def downgrade():
    op.drop_table('Users')
    op.drop_table('Messages')
