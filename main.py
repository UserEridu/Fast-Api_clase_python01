from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

def main():
    print("Hello from rep-apis!")


if __name__ == "__main__":
    main()
