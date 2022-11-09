##############################
####---------APAGAR--------###
from jogos import *
class JogoBT_27(Game):
    
    def _init(self):
        self.to_move = 1;
        utility = 0; #????
        board = {"a1" : 'W', "b1" : 'W', "c1" : 'W', "d1" : 'W', "e1" : 'W', "f1" : 'W', "g1" : 'W', "h1" : 'W',
                 "a2" : 'W', "b2" : 'W', "c2" : 'W', "d2" : 'W', "e2" : 'W', "f2" : 'W', "g2" : 'W', "h2" : 'W',
                 "a8" : 'B', "b8" : 'B', "c8" : 'B', "d8" : 'B', "e8" : 'B', "f8" : 'B', "g8" : 'B', "h8" : 'B',
                 "a7" : 'B', "b7" : 'B', "c7" : 'B', "d7" : 'B', "e7" : 'B', "f7" : 'B', "g7" : 'B', "h7" : 'B'};
        moves = ['a2-a3', 'a2-b3', 'b2-a3', 'b2-b3', 'b2-c3', 'c2-b3', 'c2-c3',
                 'c2-d3', 'd2-c3', 'd2-d3', 'd2-e3', 'e2-d3', 'e2-e3', 'e2-f3',
                 'f2-e3', 'f2-f3', 'f2-g3', 'g2-f3', 'g2-g3', 'g2-h3', 'h2-g3',
                 'h2-h3'];
        self.initial = GameState(1, utility, board, moves);

    def actions(self, state):
        return;
    
    def result(self, state, move):
        return;
    
    def display(self, state):
        print();
            