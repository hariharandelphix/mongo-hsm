#
# Copyright (c) 2023 by Delphix. All rights reserved.
#

"""create all tables

Revision ID: 5205ff2ec1bb
Revises:
Create Date: 2023-07-06 17:28:33.873950

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "1"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "connector",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user", sa.Text(length=25), nullable=False),
        sa.Column("password", sa.Text(length=25), nullable=False),
        sa.Column("jdbc_url", sa.Text(), nullable=False),
        sa.Column("certificate_key_file", sa.Text(), nullable=True),
        sa.Column("tls_ca_file", sa.Text(), nullable=True),
        sa.Column("ssl", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "data_set",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("data", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "source_data",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("data", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "source_data_info",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("data", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "unload_process",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("data", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "unload_process_data_info",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("data", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("unload_process_data_info")
    op.drop_table("unload_process")
    op.drop_table("source_data_info")
    op.drop_table("source_data")
    op.drop_table("data_set")
    op.drop_table("connector")
    # ### end Alembic commands ###
