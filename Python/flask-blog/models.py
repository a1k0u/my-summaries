from app import db
from datetime import datetime

import re


def urlify(name: str) -> str:
    return re.sub(r"[^\w+]", "_", name)


post_tags = db.Table(
    "post_tags",
    db.Column("post_id", db.Integer, db.ForeignKey("post.id")),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id")),
)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.now())
    tags = db.relationship(
        "Tag", secondary=post_tags, backref=db.backref("posts", lazy="dynamic")
    )

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
    db.create_all()
