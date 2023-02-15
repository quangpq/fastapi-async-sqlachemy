"""init

Revision ID: 3f1a809a5b78
Revises: 
Create Date: 2023-02-15 11:25:46.471294

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '3f1a809a5b78'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'notes',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('title', sa.String(length=256), nullable=False),
        sa.Column('note', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('notes')
