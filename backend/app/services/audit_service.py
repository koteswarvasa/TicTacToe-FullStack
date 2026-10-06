
import json

from datetime import datetime

from sqlalchemy.orm import Session

from app.models.audit_log import AuditLog


def create_audit_log(
    db: Session,
    source_schema_name: str,
    source_table_name: str,
    record_id: int,
    action_type: str,
    audit_by: str,
    old_data: dict | None = None,
    new_data: dict | None = None
):

    audit_record = AuditLog(

        source_schema_name=source_schema_name,

        source_table_name=source_table_name,

        record_id=record_id,

        action_type=action_type,

        old_data=(
            json.dumps(old_data)
            if old_data is not None
            else None
        ),

        new_data=(
            json.dumps(new_data)
            if new_data is not None
            else None
        ),

        audit_tstmp=datetime.now(),

        audit_by=audit_by
    )

    db.add(audit_record)

