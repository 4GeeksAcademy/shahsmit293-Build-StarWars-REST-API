"""empty message

Revision ID: 10e766edd218
Revises: 7e6096dc58ae
Create Date: 2023-10-06 12:08:19.323031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10e766edd218'
down_revision = '7e6096dc58ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('locations', schema=None) as batch_op:
        batch_op.drop_constraint('locations_type_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('locations', schema=None) as batch_op:
        batch_op.create_unique_constraint('locations_type_key', ['type'])

    # ### end Alembic commands ###
