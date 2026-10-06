
from sqlalchemy import (
    Column,
    BigInteger,
    String,
    DateTime,
    CHAR,
    ForeignKey
)

from app.database import Base


class Game(Base):

    __tablename__ = "GAME"

    __table_args__ = {
        "schema": "APP"
    }

    # Primary Key
    game_id = Column(
        "GAME_ID",
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    # Players
    player_x_id = Column(
        "PLAYER_X_ID",
        BigInteger,
        ForeignKey("APP.PLAYER.PLAYER_ID"),
        nullable=False
    )

    player_o_id = Column(
        "PLAYER_O_ID",
        BigInteger,
        ForeignKey("APP.PLAYER.PLAYER_ID"),
        nullable=False
    )

    # Game information
    current_player = Column(
        "CURRENT_PLAYER",
        CHAR(1),
        nullable=False
    )

    game_status = Column(
        "GAME_STATUS",
        String(20),
        nullable=False
    )

    winner = Column(
        "WINNER",
        CHAR(1),
        nullable=True
    )

    # Timestamps
    start_tstmp = Column(
        "START_TSTMP",
        DateTime,
        nullable=False
    )

    end_tstmp = Column(
        "END_TSTMP",
        DateTime,
        nullable=True
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
