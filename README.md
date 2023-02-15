# fastapi-async-sqlalchemy
Sample application uses FastAPI + async SQLAlchemy + Alembic + Uvicorn

## Quickstart
Install environment:
```shell
pipenv install
```

Update `.env` file, then init database:
```shell
alembic upgrade head
```

Run the application:
```shell
python3 run.py
```

---
<p align="center"><i>fastapi-async-sqlalchemy is <a href="https://github.com/quangpq/fastapi-async-sqlalchemy/blob/master/LICENSE">MIT licensed</a> code