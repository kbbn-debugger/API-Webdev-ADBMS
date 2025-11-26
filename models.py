from sqlmodel import Field, SQLModel
from typing import Optional, List



class Race(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    race: str = Field(index=True) # Human, Elf, Dwarf

class MagicType(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    magic: str = Field(index=True) # Arcane, Dark, Light, Elemental



class Character(SQLModel, table = True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: Optional[int]
    
    race_id: Optional[int] = Field(default=None, foreign_key="race.id")
    magic_type_id: Optional[int] = Field(default=None, foreign_key="magictype.id")