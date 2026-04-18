import datetime as _dt
from typing import Optional

import pydantic as _pydantic

class _BaseContact(_pydantic.BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str

class Contact(_BaseContact):
    id: int
    date_created: _dt.datetime

    class Config:
        from_attributes = True

class CreateContact(_BaseContact):
    pass

class UpdateContact(_BaseContact):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
