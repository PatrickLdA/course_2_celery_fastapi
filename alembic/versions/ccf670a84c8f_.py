"""empty message

Revision ID: ccf670a84c8f
Revises: af642f223db5
Create Date: 2025-03-17 22:48:58.972910

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ccf670a84c8f'
down_revision: Union[str, None] = 'af642f223db5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
