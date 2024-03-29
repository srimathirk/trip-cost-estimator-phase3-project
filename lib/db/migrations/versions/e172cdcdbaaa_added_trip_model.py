"""added Trip model

Revision ID: e172cdcdbaaa
Revises: 12659bbadc31
Create Date: 2023-08-19 12:24:25.020939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e172cdcdbaaa'
down_revision = '12659bbadc31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trips',
    sa.Column('trip_id', sa.Integer(), nullable=False),
    sa.Column('start_place', sa.String(), nullable=True),
    sa.Column('destination_place', sa.String(), nullable=True),
    sa.Column('gas_cost', sa.Float(), nullable=True),
    sa.Column('mileage', sa.Float(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('trip_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trips')
    # ### end Alembic commands ###
