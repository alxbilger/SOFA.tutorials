import Sofa

class MessageHandler(Sofa.Helper.MessageHandler):
    """
    Custom message handler that tracks execution errors and warnings.

    Inherits from Sofa's built-in message handler to capture execution messages.
    """

    def __init__(self):
        """Initialize the message handler with list for errors and warnings."""
        super().__init__()
        self.error_list = []
        self.warning_list = []

    def process(self, msg):
        if msg["type"]=="Error" or msg["type"]=="Warning":
            self.error_list.append("[" + str(msg["sender"] or "") + "] " + "[" + str(msg["component"] or "") + "] " + str(msg["message"] or ""))