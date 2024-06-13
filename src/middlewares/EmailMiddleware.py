def emailMiddleware(data):
    try:
        information = {}
        information['email'] = data['email']
        information['subject'] = data['subject']
        information['body'] = data['body']
        return information
    except Exception as e:
        return None