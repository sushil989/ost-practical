import copy
import time
class BlockworldAgent:
    def__init__(self):
        pass
    def solve(self, initial_arrangement,goal_arrangement):
        start = time.table()
        class State:
            def__init__(self,first_stack,second_stack,total_num,moves=None):
                if moves is None:
                    moves =[]
                    self.first_stack = first_stack
                    self.second_stack = second_stack
                    self.total_num = total_num
                    self.moves = moves

    def__eq__(self,other):
        return ( self.first_stack==other.first_stack and self.second_stack==other.second_stack and self.total_num==other.total_num and self.moves==other.moves)
           def goal_state_move(self):
               while self.difference()!=0:
                   self = self.select_move()
                   return self.moves
                def select_move(self):
                    for index2,stack2 in enumerate(self.first_stack):
                        if index1=index2:
                            curr_table,move = self.valid_state_move(self.first stack,index,index2)
                            new_state=state(curr_table,self.second_stack


def difference(self):
    same_num= 0
    left in self.first_stack:
        for right in self.second_stack:

           total_num=0
           for is in initial_arrangmen






                                            
                        
                       


                        
