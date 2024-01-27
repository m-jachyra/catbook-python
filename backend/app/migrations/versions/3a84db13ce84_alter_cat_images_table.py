"""alter_cat_images_table

Revision ID: 3a84db13ce84
Revises: d799addc41cf
Create Date: 2024-01-27 15:48:58.300592

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision: str = '3a84db13ce84'
down_revision: Union[str, None] = 'd799addc41cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cat_images', sa.Column('is_profile', sa.Boolean(), nullable=True, default=False))
    # ### end Alembic commands ###

    bind = op.get_bind()
    session = sa.orm.Session(bind=bind)
    session.execute(
        text("UPDATE cat_images SET is_profile=False")
    )
    session.commit()



def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cat_images', 'is_profile')
    # ### end Alembic commands ##