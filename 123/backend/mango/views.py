from datetime import timedelta
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from beanie import PydanticObjectId

from .documents import User, Post
from .models import UserOut, Comment
from authent.auth import get_password_hash, authenticate_user, create_access_token, get_current_user
from .config import settings
from typing import List


router = APIRouter(prefix="")


@router.post("/register/", status_code=201, response_model=UserOut)
async def register_user(user_data: User):
    user_data.password = get_password_hash(user_data.password)
    return await user_data.save()


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token}

@router.get("/me", response_model=UserOut)
async def get_user_data(current_user: User = Depends(get_current_user)):
    return current_user

@router.post("/me/post")
async def create_post(post_data: Post, current_user: User = Depends(get_current_user)):
    post_data.create_by = str(current_user.id)
    return await post_data.sava()

@router.post("/create/comment/{post_id}",status_code=201)
async def create_comment(post_id: str, comment_data: Comment, currnet_user: User = Depends(get_current_user)):
    post = await Post.find_one(Post.id == PydanticObjectId(post_id))
    comment_data.user_id = str(currnet_user,id)
    post.comments.append(comment_data) 
    return await post.sava()
"""
@router.post("/delete/post")
async def delete_post(post_data: Post, current_user: User = Depends(get_current_user)):
    post = await Post.find_one(Post.id == PydanticObjectId(post_id))
    if currnet_user.id == user_id:
        

@router.post("/delete/comment")
"""