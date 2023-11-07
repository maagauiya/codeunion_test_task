💸 CURRENCY APP
====


**🚀 Начало работы**
1. Установка зависимостей
Установите необходимые библиотеки с помощью <br>
```pip install -r requirements.txt```
**2. Настройка конфигурации**
Создайте файл .env в той же директории, что и ваш скрипт, и добавьте переменные: <br>
**examples** <br>
* ```SECRET_KEY=FDDJKDJW(*#)(@*@(#@*#)(@*#)(@*#()@``` <br>
* ```DEBUG=True```<br>


**🕓 CRON**
1. Каждый день в 10:00 будет запускаться задача по обновлению баз данных. <br>
Чтобы добавить задачу, выполните команду <br>
* ```python3 manage.py crontab show ```<br>
Список задач перечислен в settings.py
https://github.com/maagauiya/codeunion_test_task/blob/7b4353887f0d32a50d41b5783068fc5a7d02c467/project/settings.py#L98

**📟 CLI-COMMAND**
1. Команда для просмотра и обновления базы данных <br>
Выполните команду для просмотра <br>
* ```python3 manage.py currency_action --id 300```<br>
Response example:
Currency ID: 195, Name: JPY, Rate: 3.09, Published Date: 2023-11-07
Для обновления
* ```python3 manage.py currency_action --id 300 --value 22```<br>
Response example:
Currency JPY updated successfully with new value 2.0.


**🏋🏼‍♀️ REST API**
1. GET /currency <br>
* ```{{localhost}}/api/v1/currencies/currency```<br>
Response example:
```json
{
    "count": 39,
    "next": "http://127.0.0.1:8000/api/v1/currencies/currency/?page=2&per_page=3",
    "previous": null,
    "results": [
        {
            "id": 195,
            "name": "JPY",
            "rate": 2.0,
            "published_date": "2023-11-07"
        },
        {
            "id": 157,
            "name": "AUD",
            "rate": 300.6,
            "published_date": "2023-11-07"
        },
        {
            "id": 158,
            "name": "AZN",
            "rate": 272.84,
            "published_date": "2023-11-07"
        }
    ]
}
```
1. GET /currency (pagination) <br>
* ```{{localhost}}/api/v1/currencies/currency?page=1&per_page=2```<br>
Response example:
```json
{
    "count": 39,
    "next": "http://127.0.0.1:8000/api/v1/currencies/currency/?page=2&per_page=2",
    "previous": null,
    "results": [
        {
            "id": 195,
            "name": "JPY",
            "rate": 2.0,
            "published_date": "2023-11-07"
        },
        {
            "id": 157,
            "name": "AUD",
            "rate": 300.6,
            "published_date": "2023-11-07"
        }
    ]
}
```
1. GET /currency (filter) <br>
* ```{{localhost}}/api/v1/currencies/currency?name=AUD```<br>
Response example:
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 157,
            "name": "AUD",
            "rate": 300.6,
            "published_date": "2023-11-07"
        }
    ]
}
```

1. GET /currency (filter) <br>
* ```{{localhost}}/api/v1/currencies/currency?name=AUD```<br>
Response example:
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 157,
            "name": "AUD",
            "rate": 300.6,
            "published_date": "2023-11-07"
        }
    ]
}
```

1. GET /currency/{id} <br>
* ```{{localhost}}/api/v1/currencies/currency/195/```<br>
Response example:
```json
{
    "id": 195,
    "name": "JPY",
    "rate": 3.09,
    "published_date": "2023-11-07"
}
```





