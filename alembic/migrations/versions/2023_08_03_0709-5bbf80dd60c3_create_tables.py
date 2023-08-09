"""create tables

Revision ID: 5bbf80dd60c3
Revises: 
Create Date: 2023-08-03 07:09:47.777603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5bbf80dd60c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    role = op.create_table('role',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('permissions', sa.JSON(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('registered_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('role_id', sa.Integer(), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('is_superuser', sa.Boolean(), nullable=False),
        sa.Column('is_verified', sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('domain_data',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('main_info', sa.JSON(), nullable=False),
        sa.Column('active_users', sa.JSON(), nullable=False),
        sa.Column('incoming_line', sa.JSON(), nullable=False),
        sa.Column('user_info', sa.JSON(), nullable=False),
        sa.Column('contacts_user', sa.JSON(), nullable=False),
        sa.Column('groups_user', sa.JSON(), nullable=False),
        sa.Column('group_info', sa.JSON(), nullable=False),
        sa.Column('users_in_group', sa.JSON(), nullable=False),
        sa.Column('names_id_ivr', sa.JSON(), nullable=False),
        sa.Column('ivr_params_events', sa.JSON(), nullable=False),
        sa.Column('route_info', sa.JSON(), nullable=False),
        sa.Column('route_settings', sa.JSON(), nullable=False),
        sa.PrimaryKeyConstraint('name')
    )
    op.bulk_insert(
        role,
            [{"id": 1, "name": "user", "permissions": None},
             {"id": 2, "name": "admin", "permissions": None},
             {"id": 3, "name": "root", "permissions": None}]
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('role')
    op.drop_table('domain_data')
    # ### end Alembic commands ###
