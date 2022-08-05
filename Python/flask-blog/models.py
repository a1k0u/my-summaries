from app import db
from datetime import datetime

import re


def urlify(name: str) -> str:
    return re.sub(r"[^\w+]", "_", name)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.url = urlify(self.title)

    def __repr__(self):
        return f"<Post {self.id=}, {self.title=}>"


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    url = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.url = urlify(self.name)

    def __repr__(self):
        return f"<Tag {self.id=}, {self.name=}>"


if __name__ == "__main__":
    from app import db
    db.create_all()
