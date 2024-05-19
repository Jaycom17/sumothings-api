from models.DealerModel import DealerModel

def dealerMiddleWare(dealer):
    try:
        return DealerModel(dealer["deaFullName"], dealer["deaEmail"], dealer["deaPhone"], dealer["deaCedula"])
    except KeyError as e:
        return None