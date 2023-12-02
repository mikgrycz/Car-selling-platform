"""Db migration does it work

Revision ID: ec38c641c51a
Revises: 90d198c415e6
Create Date: 2023-12-03 00:10:41.263469

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec38c641c51a'
down_revision: Union[str, None] = '90d198c415e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
