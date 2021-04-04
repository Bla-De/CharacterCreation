class Reward():
    def __init__(self,externalID,user):
        self.externalId = externalID
        self.redeemed = False
        self.valid = None
        self.user = user

    def __str__(self):
        return self.user