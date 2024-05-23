# FastAPI + SQLModel + Alembic

Sample FastAPI project that uses async SQLAlchemy, SQLModel, Postgres, Poetry and Alembic.
<br />
<br />
Alembic migrations command:
```sh
alembic upgrade head
```
Healthcheck endpoint: 
```
<proto>://<address>/ping
```
Add a song:

```sh
curl -d '{"name":"Hate by Design", "artist":"Killswitch Engage", "year":"2016"}' -H "Content-Type: application/json" -X POST <proto>://<address>/songs
```

Get all songs:
```sh
curl -X GET <proto>://<address>/songs
```
