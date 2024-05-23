from database.database import db
import uuid
import datetime

class ArticleModel:
    def __init__(self, artTitle: str, artShortDescription: str, artContent: str, artAuthor: str, artDate: datetime):
        self.artTitle = artTitle
        self.artShortDescription = artShortDescription
        self.artContent = artContent
        self.artAuthor = artAuthor
        self.artDate = artDate

class Article(db.Model):
     __tablename__ = 'article'
     artID = db.Column(db.String(128), primary_key=True)
     artTitle = db.Column(db.String(128), nullable=False)
     artShortDescription= db.Column(db.Text, nulleable=False)
     artContent = db.Column(db.Text, nulleable=False)
     artAuthor = db.Column(db.String(128), nullable=False)
     artDate = db.Column(db.Date, nulleable=False)

     def __init__(self, artTitle: str, artShortDescription: str, artContent: str, artAuthor: str, artDate: datetime):
        self.artID = uuid.uuid4().hex
        self.artTitle = artTitle
        self.artShortDescription = artShortDescription
        self.artContent = artContent
        self.artAuthor = artAuthor
        self.artDate = artDate

     def toJSON(self):
        return {
            "artID": self.artID, 
            "artTitle": self.artTitle,
            "artShortDescription": self.artShortDescription,
            "artContent": self.artContent,
            "artAuthor": self.artAuthor,
            "artDate": self.artDate
        }



    
    
