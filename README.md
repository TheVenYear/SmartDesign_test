# SmartDesign_test
## Установка
- Установить Python 3.8
- Запустить команду: pip install -r req.txt
- Запустить сервер с mongodb: docker run -d -p 27017:27017 mongo
- Запустить миграции Django: python manage.py migrate
## Curl запросы:
###Создание 1 товара:
```
curl --silent --location --request POST 'http://127.0.0.1:8000/api/v1/products/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "params": [
        {
            "key": "Категория",
            "value": "Телефоны"
        },
        {
            "key": "Производитель",
            "value": "Xiaomi"
        }
    ],
    "name": "Телефон Xiaomi Redmi note 22",
    "description": "Превосходный аппарат, произведённый где-то в Китае"
}'
```
