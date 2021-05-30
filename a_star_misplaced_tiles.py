import math
from copy import deepcopy

class Puzzle:
    def __init__(self,start_state:list,goal_state:list):
        
        self.start_state=start_state
        self.current_state=deepcopy(self.start_state)
        self.goal_state=goal_state
        self.blank_tile=self.findBlankTile()
        self.length=len(self.start_state)
        self.row_count=math.floor(math.sqrt(self.length))
        self.current_level=0

    def findBlankTile(self)->int:

        for i in range(len(self.start_state)):
            if self.start_state[i]==0:
                return i

    def moveUp(self,check=False):

        if check:
            if (self.blank_tile-self.row_count) in range(self.length):
                print("Up Move Check")
                tempCurrentState=deepcopy(self.current_state)
                tempBlankTile=deepcopy(self.blank_tile)
                self.current_state[self.blank_tile-self.row_count],self.current_state[self.blank_tile]=self.current_state[self.blank_tile],self.current_state[self.blank_tile-self.row_count]
                print(self.current_state)
                self.blank_tile=self.blank_tile-self.row_count
                heruistic=self.calculateMisplacedTiles()
                # self.current_level=self.current_level+1
                self.current_level=tempCurrentState
                self.blank_tile=tempBlankTile

                return {"movePossible":True,"heruistic":heruistic}
            else:
                return {"movePossible":False,"heruistic":-1}

        if (self.blank_tile-self.row_count) in range(self.length):
            print("Up Move")
            self.current_state[self.blank_tile-self.row_count],self.current_state[self.blank_tile]=self.current_state[self.blank_tile],self.current_state[self.blank_tile-self.row_count]
            print(self.current_state)
            self.blank_tile=self.blank_tile-self.row_count
            self.current_level=self.current_level+1
            return True
        else:
            return False

    def moveDown(self,check=False):
        if check:
            if (self.blank_tile+self.row_count) in range(self.length):
                print("Down Move Check")
                tempCurrentState=deepcopy(self.current_state)
                tempBlankTile=deepcopy(self.blank_tile)
                self.current_state[self.blank_tile+self.row_count],self.current_state[self.blank_tile]=self.current_state[self.blank_tile],self.current_state[self.blank_tile+self.row_count]
                print(self.current_state)
                self.blank_tile=self.blank_tile+self.row_count
                heruistic=self.calculateMisplacedTiles()
                # self.current_level=self.current_level+1
                self.current_level=tempCurrentState
                self.blank_tile=tempBlankTile

                return {"movePossible":True,"heruistic":heruistic}
            else:
                return {"movePossible":False,"heruistic":-1}


        if (self.blank_tile+self.row_count) in range(self.length):
            print("Down Move")
            self.current_state[self.blank_tile+self.row_count],self.current_state[self.blank_tile]=self.current_state[self.blank_tile],self.current_state[self.blank_tile+self.row_count]
            print(self.current_state)
            self.blank_tile=self.blank_tile+self.row_count
            self.current_level=self.current_level+1
            return True
        else:
            return False

    def moveRight(self,check=False):
        if check:
            if not (self.blank_tile+1)%self.row_count==0:
                print("Right Move Check")
                tempCurrentState=deepcopy(self.current_state)
                tempBlankTile=deepcopy(self.blank_tile)
                self.current_state[self.blank_tile+1],self.current_state[self.blank_tile]=self.current_state[self.blank_tile],self.current_state[self.blank_tile+1]
                print(self.current_state)
                self.blank_tile=self.blank_tile+1
                heruistic=self.calculateMisplacedTiles()
                # self.current_level=self.current_level+1
                self.current_level=tempCurrentState
                self.blank_tile=tempBlankTile

                return {"movePossible":True,"heruistic":heruistic}
            else:
                return {"movePossible":False,"heruistic":-1}
        
        if not (self.blank_tile+1)%self.row_count==0 :
            print("Right Move")
            self.current_state[self.blank_tile+1],self.current_state[self.blank_tile]=self.current_state[self.blank_tile],self.current_state[self.blank_tile+1]
            print(self.current_state)
            self.blank_tile=self.blank_tile+1
            self.current_level=self.current_level+1
            return True
        else:
            return False

    def moveLeft(self,check=False):

        if check:
            if math.floor((self.blank_tile-1)/self.row_count)==math.floor((self.blank_tile)/self.row_count):
                print("Left Move Check")
                tempCurrentState=deepcopy(self.current_state)
                tempBlankTile=deepcopy(self.blank_tile)
                self.current_state[self.blank_tile-1],self.current_state[self.blank_tile]=self.current_state[self.blank_tile],self.current_state[self.blank_tile-1]
                print(self.current_state)
                self.blank_tile=self.blank_tile-1
                heruistic=self.calculateMisplacedTiles()
                # self.current_level=self.current_level+1
                self.current_level=tempCurrentState
                self.blank_tile=tempBlankTile

                return {"movePossible":True,"heruistic":heruistic}
            else:
                return {"movePossible":False,"heruistic":-1}

        if math.floor((self.blank_tile-1)/self.row_count)==math.floor((self.blank_tile)/self.row_count):
            print("Left Move")
            self.current_state[self.blank_tile-1],self.current_state[self.blank_tile]=self.current_state[self.blank_tile],self.current_state[self.blank_tile-1]
            print(self.current_state)
            self.blank_tile=self.blank_tile-1
            self.current_level=self.current_level+1
            return True
        else:
            return False

    def calculateMisplacedTiles(self)->int:
        count=0
        for i in range(self.length):
            if not self.current_state[i]==self.goal_state[i]:
                count=count+1
        return count

    def runA_Star(self):
        move=self.moveLeft(check=True)
        if move["movePossible"]:
             print(self.current_state,self.blank_tile,move["heruistic"],self.current_state,self.blank_tile)
        else:
            print(move)

p=Puzzle([1,2,3,0,4,6,7,5,8],[1,2,3,4,5,6,7,8,0])


# print(p.moveDown(),p.calculateMisplacedTiles(),p.blank_tile)

p.runA_Star()




