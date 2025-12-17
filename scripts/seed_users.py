from sqlalchemy import select
from app.db.session import SessionLocal
from app.models import User

def get_or_create(db, email: str, is_admin: bool):
    u = db.scalar(select(User).where(User.email == email))
    if u:
        return u
    u = User(email=email, hashed_password="not-used", is_admin=is_admin)
    db.add(u)
    db.commit()
    db.refresh(u)
    return u

def main():
    db = SessionLocal()
    try:
        u1 = get_or_create(db, "user@example.com", False)
        u2 = get_or_create(db, "admin@example.com", True)
        print("user:", u1.id, u1.email, u1.is_admin)
        print("admin:", u2.id, u2.email, u2.is_admin)
    finally:
        db.close()

if __name__ == "__main__":
    main()
