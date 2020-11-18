# SmartDesign_test
### Установка
- Установить Python 3.8
- Запустить команду: pip install -r req.txt
- Запустить сервер с mongodb: docker run -d -p 27017:27017 mongo
- Запустить миграции Django: python manage.py migrate
### Curl запросы:
curl --silent --location --request POST 'http://127.0.0.1:8000/api/v1/products/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "params": [
        {
            "key": "Крыла",
            "value": "2"
        },
        {
            "key": "Шасси",
            "value": "Работает"
        }
    ],
    "name": "Самолёт ИЛ-2",
    "description": "Превосходный самолёт"
}'
