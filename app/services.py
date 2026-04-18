from typing import TYPE_CHECKING, List

import app.database as _database
import app.models as _models
import app.schemas as _schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def create_contact(
        contact: _schemas.CreateContact, db: "Session"
) -> _schemas.Contact:
    contact = _models.Contact(**contact.model_dump())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return _schemas.Contact.model_validate(contact, from_attributes=True)

async def get_all_contacts(
        db: "Session"
) -> List[_schemas.Contact]:
    contacts = db.query(_models.Contact).all()
    return list(map(_schemas.Contact.model_validate, contacts))

async def get_contact(
        contact_id: int,
        db: "Session"
):
    contact = db.query(_models.Contact).filter(_models.Contact.id == contact_id).first()
    return contact

async def delete_contact(
        contact: _models.Contact,
        db: "Session"
):
    db.delete(contact)
    db.commit()

async def update_contact(
        contact_data: _schemas.UpdateContact,
        contact: _models.Contact,
        db: "Session"
) -> _schemas.Contact:
    if contact_data.first_name:
        contact.first_name = contact_data.first_name
    if contact_data.last_name:
        contact.last_name = contact_data.last_name
    if contact_data.email:
        contact.email = contact_data.email
    if contact_data.phone_number:
        contact.phone_number = contact_data.phone_number
    db.commit()
    db.refresh(contact)
    return _schemas.Contact.model_validate(contact, from_attributes=True)