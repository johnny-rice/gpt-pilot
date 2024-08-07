"""Add original description and template summary fields to specifications

Revision ID: c8905d4ce784
Revises: 08d71952ec2f
Create Date: 2024-07-25 19:24:23.808237

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "c8905d4ce784"
down_revision: Union[str, None] = "08d71952ec2f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("specifications", schema=None) as batch_op:
        batch_op.add_column(sa.Column("original_description", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("template_summary", sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("specifications", schema=None) as batch_op:
        batch_op.drop_column("template_summary")
        batch_op.drop_column("original_description")

    # ### end Alembic commands ###
