from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, Boolean, String, TIMESTAMP, ForeignKey, JSON


metadata = MetaData()


role = Table(
    "role",
    metadata,
    
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON)
)


user = Table(
    "user",
    metadata,

    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey(role.c.id)),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified",Boolean, default=False, nullable=False)
)


domain_data = Table(
    "domain_data",
    metadata,
    
    Column("name", String, primary_key=True),
    Column("main_info", JSON, nullable=False),
    Column("active_users", JSON, nullable=False),
    Column("incoming_line", JSON, nullable=False),
    Column("user_info", JSON, nullable=False),
    Column("contacts_user", JSON, nullable=False),
    Column("groups_user", JSON, nullable=False),
    Column("group_info", JSON, nullable=False),
    Column("users_in_group", JSON, nullable=False),
    Column("names_id_ivr", JSON, nullable=False),
    Column("ivr_params_events", JSON, nullable=False),
    Column("route_info", JSON, nullable=False),
    Column("route_settings", JSON, nullable=False)
)
