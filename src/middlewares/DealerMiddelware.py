from models.DealerModel import Dealer

def dealerMiddleWare(dealer):
    try:
        return Dealer(dealer["deaID"], dealer["deaFullName"], dealer["deaEmail"], dealer["deaPhone"], dealer["deaCedula"])
    except KeyError as e:
        return None