from priton.database import models
from pony import orm


@orm.db_session  # for work with db. Connect or create a new session
def add(who, whom, action):
    """For ViewHistory. Create a new action."""
    return models.ViewHistory(who=who, whom=whom, action=action)


def get_history_of_likes(whom):
    """Get history of user's likes"""
    return orm.select(vh for vh in models.ViewHistory if vh.who == whom and vh.action == "like")
