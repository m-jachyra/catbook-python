"""Add tables

Revision ID: d799addc41cf
Revises: 
Create Date: 2023-12-28 22:54:53.078010

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd799addc41cf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('breeds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_breeds_id'), 'breeds', ['id'], unique=False)
    op.create_index(op.f('ix_breeds_name'), 'breeds', ['name'], unique=False)
    op.create_table('storage_files',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_storage_files_id'), 'storage_files', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('roles', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('cats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('breed_id', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['breed_id'], ['breeds.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cats_id'), 'cats', ['id'], unique=False)
    op.create_index(op.f('ix_cats_name'), 'cats', ['name'], unique=False)
    op.create_table('cat_images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('cat_id', sa.Integer(), nullable=True),
    sa.Column('storage_file_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cat_id'], ['cats.id'], ),
    sa.ForeignKeyConstraint(['storage_file_id'], ['storage_files.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cat_images_id'), 'cat_images', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cat_images_id'), table_name='cat_images')
    op.drop_table('cat_images')
    op.drop_index(op.f('ix_cats_name'), table_name='cats')
    op.drop_index(op.f('ix_cats_id'), table_name='cats')
    op.drop_table('cats')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_storage_files_id'), table_name='storage_files')
    op.drop_table('storage_files')
    op.drop_index(op.f('ix_breeds_name'), table_name='breeds')
    op.drop_index(op.f('ix_breeds_id'), table_name='breeds')
    op.drop_table('breeds')
    # ### end Alembic commands ###
