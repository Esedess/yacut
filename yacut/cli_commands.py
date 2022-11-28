import click

from . import app, db


@app.cli.command('create_db')
def create_db():
    """Функция создания базы данных."""
    db.create_all()
    click.echo('База данных создана')


@app.cli.command('drop_db')
def drop_db():
    """Функция удаления таблиц базы данных."""
    db.drop_all()
    click.echo('Таблицы базы данных удалены')