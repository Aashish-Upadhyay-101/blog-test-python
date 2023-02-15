from pydantic import BaseModel, EmailStr

from blog.models import Article, NotFound


class AlreadyExists(Exception):
    pass


class CreateArticleCommand(BaseModel):
    auther: EmailStr
    title: str
    content: str

    def execute(self) -> Article:
        try:
            Article.get_by_title(self.title)
            raise AlreadyExists
        except NotFound:
            pass

        article = Article(auther=self.auther, title=self.title, content=self.content)
        article.save()

        return article
