# Проект YaCut

Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

***

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/Esedess/yacut
```

```bash
cd yacut
```

Cоздать и активировать виртуальное окружение:

```bash
python -m venv env
```

```bash
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Наполнить .env по примеру .env_example.

Создать базу данных:

```bash
flask create_db
```

Запустить проект:

```bash
flask run
```
Перейти на http://localhost/ и пользоваться.

Так же в проекте есть API, спецификация находится в openapi.yml.

***

## Tech Stack

+ `Python` : <https://github.com/python>
+ `Flask` : <https://github.com/pallets/flask>
+ `Flask-SQLAlchemy Extension` : <https://github.com/pallets-eco/flask-sqlalchemy>
+ `Flask-WTF` : <https://github.com/wtforms/flask-wtf>
+ `Jinja2` : <https://github.com/pallets/jinja>
+ `Flask-Migrate` : <https://github.com/miguelgrinberg/Flask-Migrate>


***

## Авторы

- [@yandex-praktikum](https://github.com/yandex-praktikum)
- [@Esedess](https://github.com/Esedess)
