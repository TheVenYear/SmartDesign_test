# SmartDesign_test
## Установка
- Установить Python 3.8
- Запустить команду: pip install -r req.txt
- Запустить сервер с mongodb: docker run -d -p 27017:27017 mongo
- Запустить миграции Django: python manage.py migrate
- Запустить сам Django: python manage.py runserver
## Curl запросы:
### Создание 1 товара:
Запрос:
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
Ответ с сервера:
```json
{
    "id": 1,
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
}
```
### Создание 2 товара:
Запрос:
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
            "value": "Apple"
        }
    ],
    "name": "Телефон Apple IPhone 13",
    "description": "Превосходный аппарат, произведённый где-то в Китае(разработанный в Америке)"
}'
```
Ответ с сервера:
```json
{
    "id": 2,
    "params": [
        {
            "key": "Категория",
            "value": "Телефоны"
        },
        {
            "key": "Производитель",
            "value": "Apple"
        }
    ],
    "name": "Телефон Apple IPhone 13",
    "description": "Превосходный аппарат, произведённый где-то в Китае(разработанный в Америке)"
}
```
### Создание 3 товара:
Запрос:
```
curl --silent --location --request POST 'http://127.0.0.1:8000/api/v1/products/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "params": [
        {
            "key": "Категория",
            "value": "Стиральные машинки"
        },
        {
            "key": "Производитель",
            "value": "Bosch"
        },
        {
            "key": "Барабан",
            "value": "есть"
        }
    ],
    "name": "Крутая стиральная машинка",
    "description": "
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud                 exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla               pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
}'
```
Ответ с сервера:
```json
{
    "id": 3,
    "params": [
        {
            "key": "Категория",
            "value": "Стиральные машинки"
        },
        {
            "key": "Производитель",
            "value": "Bosch"
        }
    ],
    "name": "Крутая стиральная машинка",
    "description": "
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud                 exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla               pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
}
```

