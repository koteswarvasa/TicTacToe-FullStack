
from datetime import datetime

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.player import Player

from app.schemas.player_schema import (
    PlayerCreate,
    PlayerResponse
)

from app.services.audit_service import (
    create_audit_log
)

from app.services.password_service import (
    hash_password
)


router = APIRouter(
    prefix="/api/players",
    tags=["Players"]
)


@router.post(
    "",
    response_model=PlayerResponse
)
def create_player(
    player_data: PlayerCreate,
    db: Session = Depends(get_db)
):

    # ==========================================
    # Check Username
    # ==========================================

    existing_username = (
        db.query(Player)
        .filter(
            Player.username ==
            player_data.username
        )
        .first()
    )

    if existing_username:

        raise HTTPException(
            status_code=409,
            detail="Username already exists"
        )


    # ==========================================
    # Check Email
    # ==========================================

    existing_email = (
        db.query(Player)
        .filter(
            Player.email ==
            player_data.email
        )
        .first()
    )

    if existing_email:

        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )


    # ==========================================
    # Create Player
    # ==========================================

    new_player = Player(

        username=player_data.username,

        email=player_data.email,

        password_hash=hash_password(
            player_data.password
        ),

        first_nm=player_data.first_nm,

        last_nm=player_data.last_nm,

        is_active=True,

        created_tstmp=datetime.now(),

        created_by=player_data.username
    )


    db.add(new_player)


    # Get generated PLAYER_ID
    db.flush()


    # ==========================================
    # Audit Data
    # ==========================================

    new_player_data = {

        "PLAYER_ID":
            new_player.player_id,

        "USERNAME":
            new_player.username,

        "EMAIL":
            new_player.email,

        "FIRST_NM":
            new_player.first_nm,

        "LAST_NM":
            new_player.last_nm,

        "IS_ACTIVE":
            new_player.is_active
    }


    # ==========================================
    # Create Audit Record
    # ==========================================

    create_audit_log(

        db=db,

        source_schema_name="APP",

        source_table_name="PLAYER",

        record_id=new_player.player_id,

        action_type="INSERT",

        audit_by=player_data.username,

        new_data=new_player_data
    )


    # ==========================================
    # Commit Transaction
    # ==========================================

    db.commit()

    db.refresh(new_player)


    return new_player
