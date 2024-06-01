from database.database import db
from models.ArticleModel import Article

def getAllArticles():
    try:
        data = Article.query.all()
        return [article.toJSON() for article in data]
    except Exception as e:
        print(str(e))
        return None
 
def getArticleById(articleID):
    try:
        data = Article.query.filter_by(artID = articleID).first()
        return data.toJSON()
    except Exception as e:
        return None

def createArticle(data):
    try:
        article = Article(data.artTitle, data.artShortDescription, data.artContent, data.artAuthor, data.artDate)
        db.session.add(article)
        db.session.commit()
        return {"message": "Article created"}
    except Exception as e:
        return None

def updateArticle(articleID, data):
    try:
        article = Article.query.filter_by(artID = articleID).first()
        
        if article.artTitle != data.artTitle:
            article.artTitle = data.artTitle

        if article.artShortDescription != data.artShortDescription:
            article.artShortDescription = data.artShortDescription

        if article.artContent != data.artContent:
            article.artContent = data.artContent
        
        if article.artAuthor != data.artAuthor:
            article.artAuthor = data.artAuthor

        if article.artDate != data.artDate:
            article.artDate = data.artDate

        db.session.commit()
        return {"message": "Article updated"}
    except Exception as e:
        print(str(e))
        return None

def deleteArticle(articleID):
    try:
        article = Article.query.filter_by(artID = articleID).first()
        db.session.delete(article)
        db.session.commit()
        return {"message": "Article deleted"}
    except Exception as e:
        return None
