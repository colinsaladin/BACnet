class Person:
    name
    id
    feed
    followlist

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.feed = None
        self.followList = None
        # feed und followlist über sync holen

    def __init__(self, id, name, feed):
        self.id = id
        self.name = name
        self.feed = feed
        self.followlist = dict()

    def follow(self, id, name):
        self.followlist[id] = Person(id, name)
        # event in feed

    def unfollow(self, id):
        self.followlist.pop(id)

    def getFollowList(self):
        return self.followlist
