from pydantic import BaseModel


class TechInfo(BaseModel):
    name: str
    title: str
    jobs_assigned: int
    jobs_responded: int
    assigned_by: str


class TechAdminInfo(BaseModel):
    name: str
    title: str
    jobs_assigned: int
    jobs_responded: int
    assigned_by: str



class TechAdmin(BaseModel):
    tech_id: int
    title: str