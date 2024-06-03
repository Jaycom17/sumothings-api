from models.ClientModel import Client

def clientMiddleWare(client):
    try:
        return Client(client["cliFullName"], client["cliEmail"], client["cliPassword"], client["cliPhone"], client["cliAddress"], client["cliNIT"], client["cliCompanyName"], client["cliCity"], client["cliPostalCode"], client["cliCedula"])
    except KeyError as e:
        return None