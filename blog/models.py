import os
import sqlite3
import uuid
from typing import List

from pydantic import BaseModel, EmailStr, Field


class NotFound(Exception):
    pass


class Article(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    auther: EmailStr
    title: str
    content: str

    @classmethod
    def get_by_id(cls, article_id: str):
        con = sqlite3.connect(os.getenv("DATABASE_NAME", "database.db"))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM article where id=?", (article_id,))

        record = cur.fetchone()

        if record is None:
            raise NotFound("The article does not exist.")

        article = cls(**record)
        con.close()

        return article

    @classmethod
    def get_by_title(cls, article_title: str):
        con = sqlite3.connect(os.getenv("DATABASE_NAME", "database.db"))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM article where title=?", (article_title,))

        record = cur.fetchone()

        if record is None:
            raise NotFound("The article does not exist.")

        article = cls(**record)
        con.close()

        return article

    @classmethod
    def list_all_articles(cls) -> List["Article"]:
        con = sqlite3.connect(os.getenv("DATABASE_NAME", "database.db"))
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM article")

        records = cur.fetchall()

        if records is None:
            raise NotFound("The article does not")

        articles = [cls(**record) for record in records]
        con.close()

        return articles

    def save(self) -> "Article":
        with sqlite3.connect(os.getenv("DATABASE_NAME", "database.db")) as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO article (id, auther, title, content) VALUES (?, ?, ?, ?)",
                (self.id, self.auther, self.title, self.content),
            )
            con.commit()

        return self

    @classmethod
    def create_table(cls, database_name="database.db"):
        con = sqlite3.connect(database_name)

        con.execute(
            "CREATE TABLE IF NOT EXISTS article (id TEXT, auther TEXT, title TEXT, content TEXT"
        )
        con.close()
