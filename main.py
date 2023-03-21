import uvicorn
from fastapi import FastAPI,Body
from schema import  User
#from config import setting
from DS import model



app= FastAPI()


@app.get("/{id}")

def index(id:int):
    return f"is id {id}  "

@app.get("/{id}")
def index(User):
    return model.getx()


if __name__=="__main__":
        # uvicorn.run('main:app',reload=settings.DEBUG_MODE,host=settings.DOMAIN,port=settings.PORT)
        uvicorn.run('main:app',reload=True,host="0.0.0.0",port=3000)

