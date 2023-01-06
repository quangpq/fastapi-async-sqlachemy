"""init

Revision ID: bfd263a54d5a
Revises: 
Create Date: 2022-04-14 15:05:35.172259

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'af5b6ea51d5c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'notes',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('title', sa.String(length=256), nullable=False),
        sa.Column('note', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade():
    op.drop_table('notes')
