from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from database import create_tables, delete_tables
from route import task_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('База очищена')
    await create_tables()
    print('База готова к работе')
    yield
    print('Выключение')


app = FastAPI(lifespan=lifespan, tags=['Таски'])
app.include_router(task_router)

if __name__ == '__main__':
    config = uvicorn.Config(app, port=8080)
    server = uvicorn.Server(config)
    server.run()
