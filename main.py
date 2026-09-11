from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('iniciar app')
    yield
    print('finalizar app')
    
app = FastAPI(title='Api Electores', lifespan=lifespan)

def main():
    print("Hello from rep-apis!")


if __name__ == "__main__":
    main()
