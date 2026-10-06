
from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Boolean,
    DateTime
)

from app.database import Base


class Player(Base):

    __tablename__ = "PLAYER"
    __table_args__ = {
        "schema": "APP"
    }

    # Primary Key
    player_id = Column(
        "PLAYER_ID",
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    # User information
    username = Column(
        "USERNAME",
        String(50),
        unique=True,
        nullable=False
    )

    email = Column(
        "EMAIL",
        String(150),
        unique=True,
        nullable=False
    )

    password_hash = Column(
        "PASSWORD_HASH",
        String(500),
        nullable=True
    )

    first_nm = Column(
        "FIRST_NM",
        String(100),
        nullable=True
    )

    last_nm = Column(
        "LAST_NM",
        String(100),
        nullable=True
    )

    # Audit columns
    is_active = Column(
        "IS_ACTIVE",
        Boolean,
        nullable=False
    )

    created_tstmp = Column(
        "CREATED_TSTMP",
        DateTime,
        nullable=False
    )

    created_by = Column(
        "CREATED_BY",
        String(100),
        nullable=False
    )

    updated_tstmp = Column(
        "UPDATED_TSTMP",
        DateTime,
        nullable=True
    )

    updated_by = Column(
        "UPDATED_BY",
        String(100),
        nullable=True
    )
