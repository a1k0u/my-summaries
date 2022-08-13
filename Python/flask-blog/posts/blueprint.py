from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from models import Post
from models import Tag

posts = Blueprint("posts", __name__, template_folder="templates")


@posts.route("/", methods=["GET"])
def index():
    q = request.args.get("q")
    list_of_posts = (
        Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
        if q
        else Post.query.all()
    )
    page_title = "Posts" if not q else f'Posts that contain "{q}"'
    webpage_title = "Index page"

    return render_template(
        "posts/posts.html",
        webpage_title=webpage_title,
        page_title=page_title,
        posts=list_of_posts,
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
