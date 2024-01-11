"""empty message

Revision ID: 0147a7d706f6
Revises: f5aeda64608a
Create Date: 2024-01-11 20:06:00.036145

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '0147a7d706f6'
down_revision: Union[str, None] = 'f5aeda64608a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cars', 'ReviewLink')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cars', sa.Column('ReviewLink', mysql.VARCHAR(length=255), nullable=True))
    # ### end Alembic commands ###
