"""New Migration

Revision ID: d35361c5023a
Revises: f1fcefb9a803
Create Date: 2023-11-07 23:55:24.733659

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd35361c5023a'
down_revision: Union[str, None] = 'f1fcefb9a803'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Messages',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Message', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Messages')
    # ### end Alembic commands ###
