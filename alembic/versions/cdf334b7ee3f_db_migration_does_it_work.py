"""Db migration does it work

Revision ID: cdf334b7ee3f
Revises: 006902561866
Create Date: 2023-12-03 00:08:10.590590

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cdf334b7ee3f'
down_revision: Union[str, None] = '006902561866'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
