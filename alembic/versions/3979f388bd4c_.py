"""empty message

Revision ID: 3979f388bd4c
Revises: de14f020988b
Create Date: 2025-03-17 22:36:47.301492

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3979f388bd4c'
down_revision: Union[str, None] = 'de14f020988b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
