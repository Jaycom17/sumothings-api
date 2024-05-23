from models.ArticleModel import ArticleModel

def articleMiddleWare(Article):
    try:
        return ArticleModel(Article["artID"], Article["artTitle"], Article["artShortDescription"], Article["artContent"], Article["artAuthor"], Article["artDate"])
    except KeyError as e:
        return None
