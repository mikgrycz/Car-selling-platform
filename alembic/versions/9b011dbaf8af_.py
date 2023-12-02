"""empty message

Revision ID: 9b011dbaf8af
Revises: 148af66357b5
Create Date: 2023-12-02 23:45:39.062509

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b011dbaf8af'
down_revision: Union[str, None] = '148af66357b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
