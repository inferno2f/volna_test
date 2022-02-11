# volna_test
Тестовое задание

Простой API, созданный при помощи Django.\
Эндпойнт `orders/` принимает POST и GET запросы.\
Поиск осуществляется по параметру `id` (номер заказа).

Обязательные параметры для POST запроса: `customer_id` и `description`


## Квикстарт

Установите и активируйте виртуальное окружение

    $ python3 -m venv env
    $ source env/bin/activate
Установите зависимости

    $ pip install -r requirements.txt

Перейдите в директорию проекта

    $ cd volna_api/
Сделайте миграции

    $ python manage.py makemigrations
    $ python manage.py migrate

Для доступа к админке создайте суперюзера (опционально)

    $ python manage.py createsuperuser
Запустите проект на дев-сервере

    $ python manage.py runserver
