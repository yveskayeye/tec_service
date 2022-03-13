from sqlalchemy import Column, ForeignKey, Integer, String, Boolean,DateTime

from ..db.database import Base


class Tech(Base):
    __tablename__ = "Techs"

    tech_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    name = Column(String)
    title = Column(String)
    jobs_responded = Column(Integer, default=0)
    is_superuser = Column(Boolean(), default=False)


class TechAdmin(Base):
    __tablename__ = "Tech_admins"

    id = Column(Integer, primary_key=True, index=True)
    date_created = Column(DateTime, index=True)
    tech_id = Column(Integer, ForeignKey("Tech.tech_id"))


class TechJob(Base):
    __tablename__ = "Tech_jobs"

    id = Column(Integer, primary_key=True, index=True)
    tech_id = Column(Integer, ForeignKey("Tech.tech_id"))
    assigned_by = Column(Integer, default=None)
    description = Column(String)
    date_created = Column(DateTime, index=True)
    