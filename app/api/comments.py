from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db.session import get_db
from app.models import Post, Comment
from app.schemas.comment import CommentCreate, CommentUpdate, CommentOut

from app.api.auth import get_current_user
from app.models import Post, Comment, User

router = APIRouter(prefix="/posts/{post_id}/comments", tags=["comments"])

def _ensure_post_exists(db: Session, post_id: int) -> None:
    if not db.get(Post, post_id):
        raise HTTPException(status_code=404, detail="Post not found")
    
def create_comment(
    post_id: int,
    payload: CommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    _ensure_post_exists(db, post_id)
    comment = Comment(content=payload.content, post_id=post_id, owner_id=current_user.id)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

@router.post("", response_model=CommentOut, status_code=status.HTTP_201_CREATED)
def create_comment(post_id: int, payload: CommentCreate, db: Session = Depends(get_db)):
    _ensure_post_exists(db, post_id)

    comment = Comment(content=payload.content, post_id=post_id, owner_id=1)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

@router.get("", response_model=list[CommentOut])
def list_comments(post_id: int, db: Session = Depends(get_db)):
    _ensure_post_exists(db, post_id)

    stmt = select(Comment).where(Comment.post_id == post_id).order_by(Comment.id.asc())
    return db.scalars(stmt).all()

@router.put("/{comment_id}", response_model=CommentOut)
def update_comment(post_id: int, comment_id: int, payload: CommentUpdate, db: Session = Depends(get_db)):
    _ensure_post_exists(db, post_id)

    comment = db.get(Comment, comment_id)
    if not comment or comment.post_id != post_id:
        raise HTTPException(status_code=404, detail="Comment not found")

    comment.content = payload.content
    db.commit()
    db.refresh(comment)
    return comment

@router.delete("/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(post_id: int, comment_id: int, db: Session = Depends(get_db)):
    _ensure_post_exists(db, post_id)

    comment = db.get(Comment, comment_id)
    if not comment or comment.post_id != post_id:
        raise HTTPException(status_code=404, detail="Comment not found")

    db.delete(comment)
    db.commit()
    return
