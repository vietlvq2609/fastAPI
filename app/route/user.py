from os import name
from urllib import response
from fastapi import APIRouter, Depends
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.schemas.user import UserInCreate, UserInResponse, UserInLogin
from app.models.user import User
from app.ultis import password

router = APIRouter()

@router.post("/")
def create_user(
    user_data: UserInCreate,
    db: Session = Depends(get_db)
):
    query = db.query(User).filter(User.name == user_data.name).first()

    if query:
        return 'user existed'
    else:
        new_user = User(
            name=user_data.name,
            password=password.hash(user_data.password),
            phone=user_data.phone  
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

@router.post("/login")
def login(
    user_login: UserInLogin,
    db: Session = Depends(get_db)
):
    query = db.query(User).filter(User.phone == user_login.phone).first()
    if query:
        check = password.verify(user_login.password, query.password)
        if check == True:
            return "dang nhap thanh cong"
        else: 
            return "sai mat khau"
    else:
        return "deo co tai khoan cua ban :)"


@router.get("/")
def get_all_user(
    db: Session = Depends(get_db)
):
    query = db.query(User).all()
    return query

@router.get("/{id}", response_model=UserInResponse)
def get_user_by_id(
    id: int,
    db: Session = Depends(get_db)
):
    query = db.query(User).filter(User.id == id).first()
    if query:
        return query
    else:
        return "deo co"

@router.put("/{id}")
def update_user_by_id(
    user_data: UserInCreate,
    id: int,
    db: Session = Depends(get_db)
):
    query = db.query(User).filter(User.id == id)
    user = query.first()
    if user is None:
        return "deo co tk ma doi update"
    else:
        user_data.password = password.hash(user_data.password)
        query.update(
            user_data.dict()
        )
        db.commit()
        return query.first()

@router.delete("/{id}")
def delete_user_by_id(
    id: int,
    db: Session = Depends(get_db)
):
    query = db.query(User).filter(User.id == id)
    user = query.first()
    if user:
        query.delete()
        return f"daxoa thanh cong user {user.name}"
    else:
        return "deo co lay gi xoa"