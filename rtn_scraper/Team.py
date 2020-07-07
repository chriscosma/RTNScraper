class MeetScore(object):
    '''Class modeling a meet'''

    def __init__(self, date, **kwargs):
        self.date = date

        if 'fx' in kwargs:
            self.fx = kwargs['fx']
        if 'ph' in kwargs:
            self.ph = kwargs['ph']
        if 'sr' in kwargs:
            self.sr = kwargs['sr']
        if 'vt' in kwargs:
            self.vt = kwargs['vt']
        if 'pb' in kwargs:
            self.pb = kwargs['pb']
        if 'hb' in kwargs:
            self.hb = kwargs['hb']
        if 'aa' in kwargs:
            self.aa = kwargs['aa']

class Gymnast(object):
    """Class modeling a gymnast"""

    def __init__(self, id, team_id, name, **kwargs):
        self.id = id
        self.team_id = team_id
        self.name = name
        self.meets = []

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