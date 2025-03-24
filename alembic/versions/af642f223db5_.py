"""empty message

Revision ID: af642f223db5
Revises: 3979f388bd4c
Create Date: 2025-03-17 22:46:37.514331

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af642f223db5'
down_revision: Union[str, None] = '3979f388bd4c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
