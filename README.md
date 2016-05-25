# rest-api
いろいろお試し中
```
git clone https://github.com/muk-ai/rest-api.git
cd rest-api
docker-compose build
docker-compose up -d
```

# migration
スキーマを変更した際の、migration自動生成
```
docker-compose exec falcon alembic revision --autogenerate -m "hogehoge"
```
migration
```
docker-compose exec falcon alembic upgrade +1
docker-compose exec falcon alembic downgrade -1
docker-compose exec falcon alembic upgrade head #最新にする
```
