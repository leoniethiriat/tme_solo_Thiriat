from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
from soccersimulator.utils import Vector2D
from soccersimulator import settings


class MyState(object):
    def __init__(self, state, idteam, idplayer):
        self.state = state
        self.idt = idteam
        self.idp = idplayer
    @property
    def equipierleplusproche(self):
        dist = 500
        idx = 0
        for (idt,idp) in self.state.players:
            if idt != self.idt: 
                continue
            if idp != self.idp:
                continue
            if self.my_position.distance(self.state.player_state(idt,idp).position)<dist:
                idx = idp
                dist = self.my_position.distance(self.state.player_state(idt,idp).position)
                pos = self.state.player_state(idt,idp).position
        return pos
    
    @property
    def my_position(self):
        return self.state.player_state(self.idt, self.idp).position
    
    def ball_position(self):
        return self.state.ball.position
        
    def pos_sonbut(self):
        if self.idt==1:
            return Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2)
        else:
            return Vector2D(0,settings.GAME_HEIGHT/2)
    def pos_monbut(self):
        if self.idt==2:
            return Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2)
        else:
            return Vector2D(0,settings.GAME_HEIGHT/2)
            
    def ennemieleplusproche(self):
        dist = 500
        idx = 0
        for (idt,idp) in self.state.players:
            if idt == self.idt: 
                continue
            if idp != self.idp:
                continue
            if self.my_position.distance(self.state.player_state(idt,idp).position)<dist:
                idx = idp
                dist = self.my_position.distance(self.state.player_state(idt,idp).position)
        if idt == 1:
            return (2,idx)
        else: return (1, idx)
        
    def procheduballon(self):
        if self.my_position.distance(self.ball_position())>(settings.PLAYER_RADIUS+settings.BALL_RADIUS):
            return False
        return True
    
    def prochedugoal(self):
        if self.my_position.distance(self.ball_position())>(settings.PLAYER_RADIUS+settings.BALL_RADIUS)*20:
            return False
        return True

    def danslescages(self):
        if self.my_position.distance(self.pos_monbut())>(settings.PLAYER_RADIUS+settings.BALL_RADIUS):
            return False
        return True
    
    #champ de defense        
    def estdanscdd(self):
        if idt == 1:
            return my_position<=37.5
        return my_position<=112.5
        