from typing import Optional
from sqlmodel import SQLModel

# Character

class CharacterCreate(SQLModel):
    name: str
    age: Optional[int] = None
    race_id: int
    magic_type_id: int

class CharacterPublic(SQLModel):
    id: int
    name: str
    age: Optional[int] = None
    race_id: int
    magic_type_id: int

class CharacterUpdate(SQLModel):
    name: Optional[str] = None
    age: Optional[int] = None
    race_id: Optional[int] = None
    magic_type_id: Optional[int] = None


# Race

class RaceCreate(SQLModel):
    race: str

class RacePublic(SQLModel):
    id: int
    race: str

class RaceUpdate(SQLModel):
    race: Optional[str] = None

# Magic Type

class MagicTypeCreate(SQLModel):
    magic: str

class MagicTypePublic(SQLModel):
    id: int
    magic: str

class MagicTypeUpdate(SQLModel):
    magic: Optional[str] = None