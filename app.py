from typing import List
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import Session, select

from database import create_db_and_tables, engine
from models import Character, MagicType, Race
from dependencies import get_session
from schemas import (
    CharacterCreate, CharacterPublic, CharacterUpdate,
    RaceCreate, RacePublic, RaceUpdate,
    MagicTypeCreate, MagicTypePublic, MagicTypeUpdate
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(
    title = "API",
    lifespan=lifespan
)

# ------------ Character ----------------
# Post

@app.post("/characters/", response_model=CharacterPublic)
def create_character(
    character_data: CharacterCreate,
    db: Session = Depends(get_session)
):
    db_character = Character.model_validate(character_data)
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character

# read all - get

@app.get("/characters/", response_model=List[CharacterPublic])
def read_characters(db: Session = Depends(get_session)):
    results = db.exec(select(Character)).all()
    return results

# read one - get

@app.get("/characters/{character_id}", response_model=CharacterPublic)
def read_character(
    *,
    character_id: int,
    db: Session = Depends(get_session)
):
    character = db.get(Character, character_id)
    if not character:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Character Not Found")
    return character

# Update

@app.patch("/characters/{character_id}", response_model=CharacterPublic)
def update_character(
    *,
    character_id: int,
    character_update: CharacterUpdate,
    db: Session = Depends(get_session)
):
    db_character = db.get(Character, character_id)
    if not db_character:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Character Not Found")
    
    update_data = character_update.model_dump(exclude_unset=True)
    db_character.sqlmodel_update(update_data)

    db.add(db_character)
    db.commit()
    db.refresh(db_character)

    return db_character

# Delete

@app.delete("/characters/{character_id}")
def delete_character(
    *,
    character_id: int,
    db: Session = Depends(get_session)
):
    character = db.get(Character, character_id)
    if not character:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Character Not Found")
    
    db.delete(character)
    db.commit()

    return {"ok": True, "message": f"Character {character_id} deleted"}



# ------------ Race ----------------
# Post

@app.post("/races/", response_model=RacePublic)
def create_race(
    race_data: RaceCreate,
    db: Session = Depends(get_session)
):
    db_race = Race.model_validate(race_data)
    db.add(db_race)
    db.commit()
    db.refresh(db_race)
    return db_race

# read all - get

@app.get("/races/", response_model=List[RacePublic])
def read_races(db: Session = Depends(get_session)):
    results = db.exec(select(Race)).all()
    return results

# read one - get

@app.get("/races/{race_id}", response_model=RacePublic)
def read_race(
    *,
    race_id: int,
    db: Session = Depends(get_session)
):
    race = db.get(Race, race_id)
    if not race:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Race Not Found")
    return race

# Update

@app.patch("/races/{race_id}", response_model=RacePublic)
def update_race(
    *,
    race_id: int,
    race_update: RaceUpdate,
    db: Session = Depends(get_session)
):
    db_race = db.get(Race, race_id)
    if not db_race:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Race Not Found")
    
    update_data = race_update.model_dump(exclude_unset=True)
    db_race.sqlmodel_update(update_data)

    db.add(db_race)
    db.commit()
    db.refresh(db_race)

    return db_race

# Delete

@app.delete("/races/{race_id}")
def delete_race(
    *,
    race_id: int,
    db: Session = Depends(get_session)
):
    race = db.get(Race, race_id)
    if not race:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Race Not Found")
    
    db.delete(race)
    db.commit()

    return {"ok": True, "message": f"Character {race_id} deleted"}


# ------------ MagicType ----------------
# Post

@app.post("/magictypes/", response_model=MagicTypePublic)
def create_magictype(
    magictype_data: MagicTypeCreate,
    db: Session = Depends(get_session)
):
    db_magictype = MagicType.model_validate(magictype_data)
    db.add(db_magictype)
    db.commit()
    db.refresh(db_magictype)
    return db_magictype

# read all - get

@app.get("/magictypes/", response_model=List[MagicTypePublic])
def read_magictypes(db: Session = Depends(get_session)):
    results = db.exec(select(MagicType)).all()
    return results

# read one - get

@app.get("/magictypes/{magic_type_id}", response_model=MagicTypePublic)
def read_magictype(
    *,
    magic_type_id: int,
    db: Session = Depends(get_session)
):
    magictype = db.get(MagicType, magic_type_id)
    if not magictype:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Magic Type Not Found")
    return magictype

# Update

@app.patch("/magictypes/{magic_type_id}", response_model=MagicTypePublic)
def update_magictype(
    *,
    magic_type_id: int,
    magictype_update: MagicTypeUpdate,
    db: Session = Depends(get_session)
):
    db_magictype = db.get(MagicType, magic_type_id)
    if not db_magictype:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Magic Type Not Found")
    
    update_data = magictype_update.model_dump(exclude_unset=True)
    db_magictype.sqlmodel_update(update_data)

    db.add(db_magictype)
    db.commit()
    db.refresh(db_magictype)

    return db_magictype

# Delete

@app.delete("/magictypes/{magic_type_id}")
def delete_magic_type(
    *,
    magic_type_id: int,
    db: Session = Depends(get_session)
):
    magictype = db.get(MagicType, magic_type_id)
    if not magictype:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Magic Type Not Found")
    
    db.delete(magictype)
    db.commit()

    return {"ok": True, "message": f"Character {magic_type_id} deleted"}