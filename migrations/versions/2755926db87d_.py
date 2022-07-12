"""empty message

Revision ID: 2755926db87d
Revises: 52472622e757
Create Date: 2022-05-23 17:28:25.348166

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2755926db87d'
down_revision = '52472622e757'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('birth_year', sa.String(length=120), nullable=True),
    sa.Column('gender', sa.String(length=120), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('eye_color', sa.String(length=120), nullable=True),
    sa.Column('hair_color', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('fav_characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('character_id'),
    sa.UniqueConstraint('character_id'),
    sa.UniqueConstraint('user_id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('fav_planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fav_vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('vehichle_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('climate', sa.String(length=120), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('orbital_period', sa.Integer(), nullable=True),
    sa.Column('rotation_period', sa.Integer(), nullable=True),
    sa.Column('diameter', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('model', sa.String(length=120), nullable=False),
    sa.Column('manufacturer', sa.String(length=120), nullable=False),
    sa.Column('cost_in_credits', sa.Integer(), nullable=True),
    sa.Column('length', sa.Integer(), nullable=True),
    sa.Column('crew', sa.Integer(), nullable=True),
    sa.Column('passengers', sa.Integer(), nullable=True),
    sa.Column('cargo_capacity', sa.Integer(), nullable=True),
    sa.Column('vehicle_class', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('model'),
    sa.UniqueConstraint('model'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.add_column('user', sa.Column('username', sa.String(length=120), nullable=False))
    op.add_column('user', sa.Column('firstname', sa.String(length=120), nullable=False))
    op.add_column('user', sa.Column('lastname', sa.String(length=120), nullable=False))
    op.create_unique_constraint(None, 'user', ['username'])
    op.drop_column('user', 'password')
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('password', mysql.VARCHAR(length=80), nullable=False))
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'lastname')
    op.drop_column('user', 'firstname')
    op.drop_column('user', 'username')
    op.drop_table('vehicles')
    op.drop_table('planets')
    op.drop_table('fav_vehicles')
    op.drop_table('fav_planets')
    op.drop_table('fav_characters')
    op.drop_table('characters')
    # ### end Alembic commands ###