
from sqlalchemy import (
    Column,
    BigInteger,
    String,
    DateTime,
    Text
)

from app.database import Base


class AuditLog(Base):

    __tablename__ = "AUDIT_LOG"

    __table_args__ = {
        "schema": "AUDIT"
    }

    audit_id = Column(
        "AUDIT_ID",
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    source_schema_name = Column(
        "SOURCE_SCHEMA_NAME",
        String(100),
        nullable=False
    )

    source_table_name = Column(
        "SOURCE_TABLE_NAME",
        String(100),
        nullable=False
    )

    record_id = Column(
        "RECORD_ID",
        BigInteger,
        nullable=False
    )

    action_type = Column(
        "ACTION_TYPE",
        String(20),
        nullable=False
    )

    old_data = Column(
        "OLD_DATA",
        Text,
        nullable=True
    )

    new_data = Column(
        "NEW_DATA",
        Text,
        nullable=True
    )

    audit_tstmp = Column(
        "AUDIT_TSTMP",
        DateTime,
        nullable=False
    )

    audit_by = Column(
        "AUDIT_BY",
        String(100),
        nullable=False
    )
