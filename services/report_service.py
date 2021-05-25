import datetime
from typing import List
import uuid
from models.location import Location
from models.report import Report
__reports:List[Report] = []

async def get_reports()->List[Report]:
    return list(__reports)

async def add_report(description:str,location:Location)->Report:
    
    now = datetime.datetime.now()
    report = Report(id = str(uuid.uuid4()) , description=description,location=location,created_data=now)
    __reports.append(report) # save list of objects 
    __reports.sort(key = lambda r: r.created_data,reverse=True) # latest report to get first using get_reports() function
    return report

