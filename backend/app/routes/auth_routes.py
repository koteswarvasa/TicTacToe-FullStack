
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.player import Player
from app.schemas.player_schema import LoginRequest, LoginResponse
from app.services.password_service import verify_password
from app.services.audit_service import create_audit_log


router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)


@router.post("/login", response_model=LoginResponse)
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    # 1. Find player by username
    player = (
        db.query(Player)
        .filter(Player.username == login_data.username)
        .first()
    )

    # 2. Player does not exist
    if not player:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    # 3. Check whether player is active
    if not player.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Player account is inactive"
        )

    # 4. Verify password
    if not verify_password(
        login_data.password,
        player.password_hash
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    # 5. Update last login timestamp
    player.last_login_tstmp = datetime.now()
    player.updated_tstmp = datetime.now()
    player.updated_by = player.username

    # 6. Create LOGIN audit record
    login_audit_data = {
        "PLAYER_ID": player.player_id,
        "USERNAME": player.username
    }

    create_audit_log(
        db=db,
        source_schema_name="APP",
        source_table_name="PLAYER",
        record_id=player.player_id,
        action_type="LOGIN",
        audit_by=player.username,
        new_data=login_audit_data
    )

    # 7. Commit player update + audit together
    db.commit()

    return LoginResponse(
        player_id=player.player_id,
        username=player.username,
        first_nm=player.first_nm,
        last_nm=player.last_nm,
        message="Login successful"
    )

