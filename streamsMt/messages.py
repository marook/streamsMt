
class EndMessage(object):
    pass

END_MESSAGE = EndMessage()

def isEndMessage(msg):
    return isinstance(msg, EndMessage)
