from sqlalchemy.orm import Session

from app.database.models import ResearchSession, User


def create_user(
    db: Session,
    name: str,
    email: str
):
    user = User(
        name=name,
        email=email
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_users(db: Session):
    return db.query(User).all()


def create_research_session(
    db: Session,
    query: str,
    response: str | None = None
):
    session = ResearchSession(
        query=query,
        response=response
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    return session