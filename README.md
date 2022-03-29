# Manager Assistant

## Installation
Для начала вам необходимо склонировать этот репозиторий:
```
git clone https://github.com/SuddenDEITY/manager-assistant <ВАША ПАПКА>
```
Установить docker и docker-compose.

Запустить контейнер:
```
docker-compose up --build (можете добавить -d чтобы запустить контейнер в dedicated моде(не обязательно))
```
Теперь необходимо создать миграции:
```
docker-compose exec web python3 manage.py makemigrations
```
Затем выполнить их:
```
docker-compose exec web python3 manage.py migrate
```
В конце необходимо загрузить данные(об оборудовании и тд):
```
docker-compose exec web python3 loaddata data.json
```
На всякий случай перезапускаем контейнер:
```
docker-compose down
docker-compose up
```
Админ панель доступна по ссылке /admin, логин:admin пароль:admin.
