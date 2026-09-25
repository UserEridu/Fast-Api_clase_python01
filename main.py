from contextlib import asynccontextmanager
from fastapi import FastAPI
from packages.routers.electores import routers as rutas
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('iniciar app')
    yield #funcion iterable#
    print('finalizar app')
    
app = FastAPI(title='Api Electores', lifespan=lifespan)
app.include_router(rutas)


def main():
    #print("Hello from rep-apis!")
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)


if __name__ == "__main__":
    main()
