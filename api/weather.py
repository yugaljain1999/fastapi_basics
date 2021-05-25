from models.report import Report
from typing import Optional
import fastapi 
from fastapi import Depends
from typing import Optional
import models
from typing import List
from models.report import Report,ReportSubmit
from services import weather_service
from models.location import Location
from services.report_service import get_reports,add_report
router = fastapi.APIRouter()

@router.get('/api/weather/{city}')
async def weather(loc:Location = Depends() , units:Optional[str]='metric'): # arguments value is changeable    
    report = await weather_service.get_weather_report(loc.city,loc.state,loc.country,units)
    print(report)
    return report

# Add report data api to post and get data 

@router.get('/api/reports',name='all_reports')
async def get_report()->List[Report]:
    return await get_reports()

@router.post('/api/reports',name='add_report',status_code=201)
async def post_report(report_submit:ReportSubmit)->Report:
    desc = report_submit.description
    loc = report_submit.location
    return await add_report(desc,loc)
    


