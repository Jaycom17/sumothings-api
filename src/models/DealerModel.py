class Dealer:
    def __init__(self, deaID: str, deaFullName: str, deaEmail:str, deaPhone:str, deaCedula:str):
        self.deaID = deaID
        self.deaFullName = deaFullName
        self.deaEmail = deaEmail
        self.deaPhone = deaPhone
        self.deaCedula = deaCedula

    def toJSON(self):
        return {
            "deaID": self.deaID,
            "deaFullName": self.deaFullName,
            "deaEmail": self.deaEmail,
            "deaPhone": self.deaPhone,
            "deaCedula": self.deaCedula
        }