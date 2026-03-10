from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from database.model.BaseModel import BaseModel


class ArticleModel(BaseModel, DeclarativeBase):
    __tablename__ = "article"

    id: Mapped[int] = mapped_column(primary_key = True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(255))
    author: Mapped[str] = mapped_column(String(32))
    article_type: Mapped[str] = mapped_column(String(32))
    article_time: Mapped[str] = mapped_column(String(32))

    def __init__(self, title: str, description: str, author: str, article_type: str, article_time: str):
        super().__init__()
        self.title = title
        self.description = description
        self.author = author
        self.article_type = article_type
        self.article_time = article_time

    @staticmethod
    def create_model(title: str, description: str, author: str, article_type: str, article_time: str) -> "ArticleModel":
        return ArticleModel(
            title = title,
            description = description,
            author = author,
            article_type = article_type,
            article_time = article_time
        )










