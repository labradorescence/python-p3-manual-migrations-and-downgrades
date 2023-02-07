"""Renaming column from email to address

Revision ID: 6e7c38cf00aa
Revises: 791279dd0760
Create Date: 2023-02-07 16:28:55.132854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e7c38cf00aa'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'email', new_column_name='address')


def downgrade() -> None:
    pass
