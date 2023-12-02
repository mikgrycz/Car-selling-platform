"""Db migration does it work

Revision ID: 90d198c415e6
Revises: cdf334b7ee3f
Create Date: 2023-12-03 00:09:53.739796

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '90d198c415e6'
down_revision: Union[str, None] = 'cdf334b7ee3f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
