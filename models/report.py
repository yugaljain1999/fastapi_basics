import datetime
from typing import Optional
from models.location import Location
from pydantic import BaseModel

class ReportSubmit(BaseModel):
    description:str
    location:Location

class Report(ReportSubmit):
    id:str
    created_data:Optional[datetime.datetime]


