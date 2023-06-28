class Logger:

    def __init__(self):
        self.older_messages = collections.defaultdict(int)
        self.new_messages = collections.defaultdict(int)
        self.oldest_message_time = 0
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if timestamp >= self.oldest_message_time + 10:
            self.older_messages = self.new_messages
            self.new_messages = {}
            self.oldest_message_time = timestamp

        if message in self.new_messages:
            return False
        if message in self.older_messages and timestamp < self.older_messages[message] + 10:
            return False
        self.new_messages[message] = timestamp
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)