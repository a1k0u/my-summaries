from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from app import db
from models import Post
from models import Tag
from .forms import PostEdit

posts = Blueprint("posts", __name__, template_folder="templates")


@posts.route("/", methods=["GET"])
def index():
    q = request.args.get("q")
    page = request.args.get("page")

    opened_page = int(page) if page and page.isdigit() else 1

    list_of_posts = (
        Post.query.filter(Post.title.contains(q) | Post.body.contains(q))
        if q
        else Post.query
    )

    pages = list_of_posts.paginate(page=opened_page, per_page=1)
    page_title = "Posts" if not q else f'Posts that contain "{q}"'
    webpage_title = "Index page"

    return render_template(
        "posts/posts.html",
        webpage_title=webpage_title,
        page_title=page_title,
        pages=pages,
    )


@posts.route("/create", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        new_post = Post(title=title, body=body)

        try:
            db.session.add(new_post)
            db.session.commit()
        except:
            ...

        return redirect(url_for("posts.index"))

    forms = PostEdit()
    return render_template(
        "posts/post_editor.html",
        editor_title="Create post",
        forms=forms,
        url=url_for("posts.create_post"),
    )


@posts.route("/<url>", methods=["GET"])
def post_content(url: str):
    post = Post.query.where(Post.url == url).first()
    return render_template("posts/post_content.html", post=post, tags=post.tags)


@posts.route("/tag/<url>", methods=["GET"])
def tag_content(url: str):
    tag = Tag.query.filter(Tag.url == url).first()
    page_title = f"Posts for '{tag.name}' tag"
    webpage_title = tag.name

    return render_template(
        "posts/posts.html",
        webpage_title=webpage_title,
        page_title=page_title,
        posts=tag.posts,
    )
