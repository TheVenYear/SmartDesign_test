# SmartDesign_test
## Установка
- Установить Python 3.8
- Запустить команду: pip install -r req.txt
- Запустить сервер с mongodb: docker run -d -p 27017:27017 mongo
- Запустить миграции Django: python manage.py migrate
- Запустить сам Django: python manage.py runserver
## Curl запросы:
### Создание товара:
```
curl --location --request POST 'http://127.0.0.1:8000/api/v1/products/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "params": [
        {
            "key": "{ключ}",
            "value": "{значение}"
        },
        {
            "key": "{ключ}",
            "value": "{значение}"
        }
    ],
    "name": "{название}",
    "description": "{описание}"
}'
```
### Вывод всех товаров:
```
curl --location --request GET 'http://127.0.0.1:8000/api/v1/products/'
```
### Вывод конкретного товара:
```
curl --location --request GET 'http://127.0.0.1:8000/api/v1/products/{id товара}'
```
### Вывод отфильтрованного товара:
Query параметры:
- name
- key
- value

Пример:
```
curl --location --request GET 'http://127.0.0.1:8000/api/v1/products/?key={ключ}&value={значенте}&name={название}'
```
