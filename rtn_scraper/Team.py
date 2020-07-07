class Gymnast(object):
    """Class modeling a gymnast"""

    def __init__(self, id, team_id, name, **kwargs):
        self.id = id
        self.team_id = team_id
        self.name = name

    def __str__(self):
        return '[%s] %s' % (self.id, self.name)

class Team(object):
    """Class modeling NCAA gymnastics team"""

    def __init__(self, id, name, **kwargs):
        self.id = id
        self.name = name
        self.roster = []

    def __str__(self):
        return '[%s] %s' % (self.id, self.name)

    def set_roster(self, roster):
        self.roster = roster