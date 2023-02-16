from blog.models import Article
from blog.queries import GetArticleByIDQuery, ListArticleQuery


def test_list_articles():
    Article(
        author="aashish@gmail.com", title="super duper", content="world"
    ).save()
    Article(
        author="aashish@gmail.com",
        title="another hello1",
        content="another world",
    ).save()

    query = ListArticleQuery()

    assert len(query.execute()) == 2


def test_get_article_by_id():
    article = Article(
        author="aashish@gmail.com", title="super123", content="hahahaha"
    ).save()

    query = GetArticleByIDQuery(id=article.id)

    assert query.execute().id == article.id
