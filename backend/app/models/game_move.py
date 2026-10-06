
from sqlalchemy import (
    Column,
    BigInteger,
    String,
    DateTime,
    CHAR,
    ForeignKey,
    SmallInteger
)

from app.database import Base


class GameMove(Base):

    __tablename__ = "GAME_MOVE"

    __table_args__ = {
        "schema": "APP"
    }

    # Primary Key
    move_id = Column(
        "MOVE_ID",
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    # Foreign Keys
    game_id = Column(
        "GAME_ID",
        BigInteger,
        ForeignKey("APP.GAME.GAME_ID"),
        nullable=False
    )

    player_id = Column(
        "PLAYER_ID",
        BigInteger,
        ForeignKey("APP.PLAYER.PLAYER_ID"),
        nullable=False
    )

    # Move information
    player_symbol = Column(
        "PLAYER_SYMBOL",
        CHAR(1),
        nullable=False
    )

    row_no = Column(
        "ROW_NO",
        SmallInteger,
        nullable=False
    )

    col_no = Column(
        "COL_NO",
        SmallInteger,
        nullable=False
    )

    move_no = Column(
        "MOVE_NO",
        SmallInteger,
        nullable=False
    )

    # Audit columns
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
