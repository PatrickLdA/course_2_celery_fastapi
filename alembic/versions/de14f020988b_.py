"""empty message

Revision ID: de14f020988b
Revises: 6ba0b78497fb
Create Date: 2025-03-17 22:34:52.164392

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de14f020988b'
down_revision: Union[str, None] = '6ba0b78497fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
