import Sofa

class MessageHandler(Sofa.Helper.MessageHandler):
    """
    Custom message handler that tracks execution errors and warnings.

    Inherits from Sofa's built-in message handler to capture execution messages.
    """

    def __init__(self):
        """Initialize the message handler with counters for errors and warnings."""
        super().__init__()
        self.num_errors = 0
        self.num_warnings = 0

    def process(self, msg):
        if msg["type"]=="Error":
            self.num_errors += 1
        elif msg["type"]=="Warning":
            self.num_warnings += 1