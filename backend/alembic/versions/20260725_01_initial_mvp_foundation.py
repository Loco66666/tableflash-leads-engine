"""Create the initial TFLE MVP database foundation.

Revision ID: 20260725_01
Revises:
Create Date: 2026-07-25
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = "20260725_01"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

user_role = postgresql.ENUM("admin", "commercial", "analyst", name="user_role")


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("full_name", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("role", user_role, nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )

    op.create_table(
        "restaurants",
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("address", sa.Text(), nullable=True),
        sa.Column("city", sa.String(length=120), nullable=True),
        sa.Column("postal_code", sa.String(length=20), nullable=True),
        sa.Column("phone", sa.String(length=32), nullable=True),
        sa.Column("email", sa.String(length=320), nullable=True),
        sa.Column("website", sa.Text(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_restaurants_name", "restaurants", ["name"], unique=False)
    op.create_index("ix_restaurants_city", "restaurants", ["city"], unique=False)

    op.create_table(
        "leads",
        sa.Column("restaurant_id", sa.Uuid(), nullable=False),
        sa.Column("assigned_user_id", sa.Uuid(), nullable=True),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["assigned_user_id"], ["users.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["restaurant_id"], ["restaurants.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("restaurant_id"),
    )
    op.create_index("ix_leads_assigned_user_id", "leads", ["assigned_user_id"], unique=False)
    op.create_index("ix_leads_status", "leads", ["status"], unique=False)

    op.create_table(
        "interactions",
        sa.Column("lead_id", sa.Uuid(), nullable=False),
        sa.Column("interaction_type", sa.String(length=50), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("occurred_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["lead_id"], ["leads.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_interactions_lead_id", "interactions", ["lead_id"], unique=False)
    op.create_index("ix_interactions_interaction_type", "interactions", ["interaction_type"], unique=False)
    op.create_index("ix_interactions_occurred_at", "interactions", ["occurred_at"], unique=False)

    op.create_table(
        "sources",
        sa.Column("restaurant_id", sa.Uuid(), nullable=False),
        sa.Column("source_type", sa.String(length=100), nullable=False),
        sa.Column("source_url", sa.Text(), nullable=True),
        sa.Column("confidence", sa.Integer(), nullable=True),
        sa.Column("collected_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["restaurant_id"], ["restaurants.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_sources_restaurant_id", "sources", ["restaurant_id"], unique=False)
    op.create_index("ix_sources_source_type", "sources", ["source_type"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_sources_source_type", table_name="sources")
    op.drop_index("ix_sources_restaurant_id", table_name="sources")
    op.drop_table("sources")
    op.drop_index("ix_interactions_occurred_at", table_name="interactions")
    op.drop_index("ix_interactions_interaction_type", table_name="interactions")
    op.drop_index("ix_interactions_lead_id", table_name="interactions")
    op.drop_table("interactions")
    op.drop_index("ix_leads_status", table_name="leads")
    op.drop_index("ix_leads_assigned_user_id", table_name="leads")
    op.drop_table("leads")
    op.drop_index("ix_restaurants_city", table_name="restaurants")
    op.drop_index("ix_restaurants_name", table_name="restaurants")
    op.drop_table("restaurants")
    op.drop_table("users")
    user_role.drop(op.get_bind(), checkfirst=True)
