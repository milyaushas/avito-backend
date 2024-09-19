from fastapi import FastAPI
from src.routers import api_router
import os
from src.service import TenderManagerService

# SERVER_ADDRESS = os.environ['SERVER_ADDRESS'] #адрес и порт, который будет слушать HTTP сервер при запуске. Пример: 0.0.0.0:8080.

#POSTGRES_CONN = os.environ['POSTGRES_CONN']  # URL-строка для подключения к PostgreSQL в формате postgres://{username}:{password}@{host}:{5432}/{dbname}.



# POSTGRES_JDBC_URL = os.environ['POSTGRES_JDBC_URL'] #JDBC-строка для подключения к PostgreSQL в формате jdbc:postgresql://{host}:{port}/{dbname}.

# POSTGRES_USERNAME = os.environ['POSTGRES_USERNAME'] #имя пользователя для подключения к PostgreSQL.

# POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD'] #пароль для подключения к PostgreSQL.

# POSTGRES_HOST = os.environ['POSTGRES_HOST'] #хост для подключения к PostgreSQL (например, localhost).

# POSTGRES_PORT = os.environ['POSTGRES_PORT'] #порт для подключения к PostgreSQL (например, 5432).

# POSTGRES_DATABASE = os.environ['POSTGRES_DATABASE']  #имя базы данных PostgreSQL, которую будет использовать приложение.


app = FastAPI(
    title="TenderAPI",
    docs_url="/docs",
    description="Сервис для управления тендерами"
)

app.include_router(api_router)
