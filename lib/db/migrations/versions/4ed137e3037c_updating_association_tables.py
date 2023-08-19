"""updating association tables

Revision ID: 4ed137e3037c
Revises: 04a9f56ec62e
Create Date: 2023-08-19 15:59:12.349652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ed137e3037c'
down_revision = '04a9f56ec62e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trip_users',
    sa.Column('trip_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['trip_id'], ['trips.trip_id'], name=op.f('fk_trip_users_trip_id_trips')),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], name=op.f('fk_trip_users_user_id_users')),
    sa.PrimaryKeyConstraint('trip_id', 'user_id')
    )
    op.create_table('expense_trips',
    sa.Column('expense_id', sa.Integer(), nullable=False),
    sa.Column('trip_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['expense_id'], ['expenses.expense_id'], name=op.f('fk_expense_trips_expense_id_expenses')),
    sa.ForeignKeyConstraint(['trip_id'], ['trips.trip_id'], name=op.f('fk_expense_trips_trip_id_trips')),
    sa.PrimaryKeyConstraint('expense_id', 'trip_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('expense_trips')
    op.drop_table('trip_users')
    # ### end Alembic commands ###