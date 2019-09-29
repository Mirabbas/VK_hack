from playhouse.migrate import *

from database import *




def migrate0(migrator):
    """Миграция с версии <5.0 до 5.0"""

    migrate(
        migrator.add_column(BotStatus._meta.db_table, 'mail_data', TextField(default='')),
        migrator.drop_column(BotStatus._meta.db_table, 'name'),
    )

def migrate1(migrator):
    """Миграция с версии 5.0 до 6.0"""

    migrate(
        migrator.drop_column(BotStatus._meta.db_table, 'last_top'),
        migrator.drop_column(BotStatus._meta.db_table, 'mail_data'),
        migrator.drop_column(User._meta.db_table, 'do_not_disturb'),
        migrator.drop_column(User._meta.db_table, 'memory'),
        migrator.add_column(User._meta.db_table, 'chatter_id', peewee.TextField(null=True)),
        migrator.add_column(User._meta.db_table, 'status', peewee.TextField(default="")),
        migrator.add_column(User._meta.db_table, 'status_locked_message', peewee.TextField(null=True)),
    )

if __name__ == '__main__':
    if database:
        if DATABASE_DRIVER == "mysql":
            migrator = SqliteMigrator(database)

        elif DATABASE_DRIVER == "postgresql":
            migrator = PostgresqlMigrator(database)
        else:
            hues.error("Can't migrate database!")

        with database.transaction():

            migrate1(migrator)
