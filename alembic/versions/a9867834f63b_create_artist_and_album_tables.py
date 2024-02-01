"""create artist and album tables

Revision ID: a9867834f63b
Revises:
Create Date: 2022-06-01 10:56:47.116322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a9867834f63b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "artists",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Unicode(255)),
    )
    op.create_table(
        "albums",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Unicode(255)),
        sa.Column("artist_id", sa.Integer, sa.ForeignKey("artists.id")),
    )


def downgrade() -> None:
    op.drop_table("albums")
    op.drop_table("artists")
