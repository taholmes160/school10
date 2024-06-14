"""Increase password hash length

Revision ID: 31f299fb3bea
Revises: 10d6a1e6a3a6
Create Date: 2024-06-14 18:47:04.943408

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '31f299fb3bea'
down_revision: Union[str, None] = '10d6a1e6a3a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.alter_column('users', 'password_hash', type_=sa.String(length=128))


def downgrade():
    op.alter_column('users', 'password_hash', type_=sa.String(length=64))
