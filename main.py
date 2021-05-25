import fastapi 
import uvicorn

# Use starlette package which is basically builtin of fastapi

from starlette.requests import Request
from starlette.staticfiles import StaticFiles

# Import views and apis #
from views import home 
from api import weather

api = fastapi.FastAPI()
#templates = Jinja2Templates('templates')
# Use api routers to get access to templates and other apis


def configuration_api():
    api.mount('/static',StaticFiles(directory='static'),name='static')
    api.include_router(home.router)  
    api.include_router(weather.router)

def configure():
    configuration_api()

    

if __name__ == '__main__':
    configure()
    uvicorn.run(api,port= 8001,host = '127.0.0.1')
else:
    configure()