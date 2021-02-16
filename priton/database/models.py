import os
from urllib import parse as urlparse
from pony import orm

db = orm.Database()


class User(db.Entity):
    """User's table."""
    vk_id = orm.Required(int)
    age = orm.Required(int)
    photo = orm.Required(str)
    gender = orm.Required(int)
    whos = orm.Set('ViewHistory', reverse='who')
    whoms = orm.Set('ViewHistory', reverse='whom')


class Action(db.Entity):
    """List of available actions."""
    description = orm.Required(str)
    view_historys = orm.Set('ViewHistory')


class ViewHistory(db.Entity):
    """User's view history."""
    who = orm.Set(User, reverse='whos')
    whom = orm.Set(User, reverse='whoms')
    action = orm.Required(Action)


def get_db_credentials(source):
    """Create dict with credentials of database.

    Args:
        source: URL of db

    Returns:
        dict: Credentials
    """
    url = urlparse.urlparse(source)
    return {
        "user": url.username,
        "password": url.password,
        "host": url.hostname,
        "port": url.port,
        "database": url.path[1:],
    }


db.bind(provider="postgres", **get_db_credentials(os.getenv("DATABASE_URL")))
db.generate_mapping(create_tables=True)
