"""added Expense model

Revision ID: 4ec790c29763
Revises: e172cdcdbaaa
Create Date: 2023-08-19 12:27:48.570664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ec790c29763'
down_revision = 'e172cdcdbaaa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('expenses',
    sa.Column('expense_id', sa.Integer(), nullable=False),
    sa.Column('trip_id', sa.Integer(), nullable=True),
    sa.Column('cost_category', sa.String(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['trip_id'], ['trips.trip_id'], ),
    sa.PrimaryKeyConstraint('expense_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('expenses')
    # ### end Alembic commands ###