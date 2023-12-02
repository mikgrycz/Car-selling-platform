"""empty message

Revision ID: 006902561866
Revises: 1ae51166d614
Create Date: 2023-12-03 00:06:39.412302

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '006902561866'
down_revision: Union[str, None] = '1ae51166d614'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
