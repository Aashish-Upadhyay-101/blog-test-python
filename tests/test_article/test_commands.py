import pytest

from blog.commands import AlreadyExists, CreateArticleCommand
from blog.models import Article


def test_create_article():
    cmd = CreateArticleCommand(
        auther="aashish@gmail.com",
        title="My New Article",
        content="Hello, world!",
    )

    article = cmd.execute()

    db_article = Article.get_by_id(article.id)

    assert db_article.id == article.id
    assert db_article.auther == article.auther
    assert db_article.title == article.title
    assert db_article.content == article.content


def test_create_article_already_exists():
    Article(
        auther="aashish@gmail.com", title="New one", content="Hello, new world"
    ).save()

    cmd = CreateArticleCommand(
        auther="aashish@gmail.com", title="New one", content="Hello, world!"
    )

    with pytest.raises(AlreadyExists):
        cmd.execute()
