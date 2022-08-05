"""empty message

Revision ID: 8e8f06a7dfef
Revises: b3877bac16e6
Create Date: 2022-08-05 19:58:05.370071

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8e8f06a7dfef'
down_revision = 'b3877bac16e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_tags')
    op.drop_table('tag')
    op.drop_table('post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('post_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('url', sa.VARCHAR(length=140), autoincrement=False, nullable=True),
    sa.Column('body', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='post_pkey'),
    sa.UniqueConstraint('url', name='post_url_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('tag',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('tag_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('url', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='tag_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('post_tags',
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tag_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], name='post_tags_post_id_fkey'),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], name='post_tags_tag_id_fkey')
    )
    # ### end Alembic commands ###
