"""create table user

Revision ID: 33b5d642293f
Revises: 
Create Date: 2022-05-28 12:57:52.021061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33b5d642293f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    create table users(id serial primary key not null,
    name varchar not null,
    password varchar not null,
    phone varchar not null)
    """)
    pass


def downgrade():
    op.execute("""
    drop table users
    """)
    pass
