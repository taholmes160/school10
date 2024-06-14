"""Increase password hash length again

Revision ID: 59d2fcba5747
Revises: 31f299fb3bea
Create Date: 2024-06-14 19:24:14.455152

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59d2fcba5747'
down_revision: Union[str, None] = '31f299fb3bea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.alter_column('users', 'password_hash', type_=sa.String(length=512))


def downgrade():
    op.alter_column('users', 'password_hash', type_=sa.String(length=64))