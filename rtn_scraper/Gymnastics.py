from enum import Enum

class Event(Enum):
    FloorExercise = 'fx'
    PommelHorse = 'ph'
    StillRings = 'sr'
    Vault = 'vt'
    ParallelBars = 'pb'
    HighBar = 'hb'
    AllAround = 'aa'
    UnevenBars = 'ub'
    BalanceBeam = 'bb'

class GymnastMeetResults(object):
    '''Class modeling a gymnast's meet results.
    Constructor contract:
        @param
            date: the date of the meet
            meet_desc: a description of the meet
            gymnast_id: the gymnast's RTN id
            (optional) fx, ph, sr, vt, pb, hb, aa, ub, bb: tuple of (event score, youtube url for event)
    '''

    def __init__(self, date, meet_desc, gymnast_id, **kwargs):
        self.date = date
        self.meet_description = meet_desc
        self.gymnast_id = gymnast_id
        self.results = dict()
        self.youtube_urls = dict()

        for x in Event:
            if x.value in kwargs:
                self.results[x] = float(kwargs[x.value][0])
                self.youtube_urls[x] = kwargs[x.value][1]

    def __str__(self):
        rep = '('

        for x in list(Event)[:-1]:
            rep += x.value + ': ' + self.results[x] + ', '

        rep += list(Event)[-1].value + ': ' + self.results[list(Event)[-1]] + ')'

        return rep

class Gymnast(object):
    """Class modeling a gymnast"""

    def __init__(self, gymnast_id, team_id, name, **kwargs):
        self.gymnast_id = gymnast_id
        self.team_id = team_id
        self.name = name
        self.meets = []

        if 'events' in kwargs:
            self.events = kwargs['events']

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
    x = GymnastResults()