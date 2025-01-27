"""empty message

Revision ID: 0b53a897459d
Revises: 2755926db87d
Create Date: 2022-05-23 17:52:14.561069

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0b53a897459d'
down_revision = '2755926db87d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('fav_characters', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('fav_characters', 'character_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.drop_index('character_id', table_name='fav_characters')
    op.drop_index('character_id_2', table_name='fav_characters')
    op.drop_index('user_id', table_name='fav_characters')
    op.drop_index('user_id_2', table_name='fav_characters')
    op.create_foreign_key(None, 'fav_characters', 'user', ['user_id'], ['id'])
    op.create_foreign_key(None, 'fav_characters', 'characters', ['character_id'], ['id'])
    op.alter_column('fav_planets', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('fav_planets', 'planet_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.create_foreign_key(None, 'fav_planets', 'planets', ['planet_id'], ['id'])
    op.create_foreign_key(None, 'fav_planets', 'user', ['user_id'], ['id'])
    op.add_column('fav_vehicles', sa.Column('vehicle_id', sa.Integer(), nullable=True))
    op.alter_column('fav_vehicles', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.create_foreign_key(None, 'fav_vehicles', 'vehicles', ['vehicle_id'], ['id'])
    op.create_foreign_key(None, 'fav_vehicles', 'user', ['user_id'], ['id'])
    op.drop_column('fav_vehicles', 'vehichle_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('fav_vehicles', sa.Column('vehichle_id', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'fav_vehicles', type_='foreignkey')
    op.drop_constraint(None, 'fav_vehicles', type_='foreignkey')
    op.alter_column('fav_vehicles', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.drop_column('fav_vehicles', 'vehicle_id')
    op.drop_constraint(None, 'fav_planets', type_='foreignkey')
    op.drop_constraint(None, 'fav_planets', type_='foreignkey')
    op.alter_column('fav_planets', 'planet_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('fav_planets', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.drop_constraint(None, 'fav_characters', type_='foreignkey')
    op.drop_constraint(None, 'fav_characters', type_='foreignkey')
    op.create_index('user_id_2', 'fav_characters', ['user_id'], unique=False)
    op.create_index('user_id', 'fav_characters', ['user_id'], unique=False)
    op.create_index('character_id_2', 'fav_characters', ['character_id'], unique=False)
    op.create_index('character_id', 'fav_characters', ['character_id'], unique=False)
    op.alter_column('fav_characters', 'character_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('fav_characters', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
