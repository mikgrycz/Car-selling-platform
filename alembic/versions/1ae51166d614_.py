"""empty message

Revision ID: 1ae51166d614
Revises: 25d5790c2c91
Create Date: 2023-12-03 00:05:43.688159

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ae51166d614'
down_revision: Union[str, None] = '25d5790c2c91'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
