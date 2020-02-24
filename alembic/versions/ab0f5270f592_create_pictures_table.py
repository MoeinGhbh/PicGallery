"""Create pictures table

Revision ID: ab0f5270f592
Revises: 
Create Date: 2020-02-23 01:41:10.671444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab0f5270f592'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'pictures',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('pic', sa.Text, nullable=False),
        sa.Column('date_time', sa.DateTime, nullable=False),
    )


def downgrade():
    op.drop_table('pictures')
