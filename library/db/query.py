from sqlalchemy import select


class SelectQuery:
    def __init__(self, session):
        self._session = session
        self._statement = None

    def select(self, *args, **kw):
        self._statement = select(*args, **kw)
        return self
