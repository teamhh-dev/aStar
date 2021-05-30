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
        self.a_star=True
        self.greedy=False
        self.misplaced=True
        self.manhattan=False


    def findBlankTile(self)->int:

        for i in range(len(self.start_state)):
            if self.start_state[i]==0:
                return i

    def moveUp(self,check=False):

        if check:
            if (self.blank_tile-self.row_count) in range(self.length):
                # print("Up Move Check")
                tempCurrentState=deepcopy(self.current_state)
                tempBlankTile=deepcopy(self.blank_tile)
                self.current_state[self.blank_tile-self.row_count],self.current_state[self.blank_tile]=self.current_state[self.blank_tile],self.current_state[self.blank_tile-self.row_count]
                # print(self.current_state)

                self.blank_tile=self.blank_tile-self.row_count
                if self.a_star and self.misplaced:
                    heruistic=self.calculateMisplacedTiles()+self.current_level+1
                elif self.a_star and self.manhattan:
                    heruistic=self.calculateManhattan()
                elif self.greedy and self.misplaced:
                    heruistic=self.calculateMisplacedTiles()
                elif self.greedy and self.manhattan:
                    heruistic=self.calculateManhattan()

                # self.current_level=self.current_level+1
                self.current_state=tempCurrentState
                self.blank_tile=tempBlankTile

                return {"movePossible":True,"heruistic":heruistic}
            else:
                return {"movePossible":False,"heruistic":-1}

        if (self.blank_tile-self.row_count) in range(self.length):
            # print("Up Move")
            self.current_state[self.blank_tile-self.row_count],self.current_state[self.blank_tile]=self.current_state[self.blank_tile],self.current_state[self.blank_tile-self.row_count]
            # print(self.current_state)
            self.blank_tile=self.blank_tile-self.row_count
            self.current_level=self.current_level+1
            return True
        else:
            return False

    def moveDown(self,check=False):
        if check:

            if (self.blank_tile+self.row_count) in range(self.length):
                # print("Down Move Check")
                tempCurrentState=deepcopy(self.current_state)
                tempBlankTile=deepcopy(self.blank_tile)
                self.current_state[self.blank_tile+self.row_count],self.current_state[self.blank_tile]=self.current_state[self.blank_tile],self.current_state[self.blank_tile+self.row_count]
                # print(self.current_state)
                self.blank_tile=self.blank_tile+self.row_count
                if self.a_star and self.misplaced:
                    heruistic=self.calculateMisplacedTiles()+self.current_level+1
                elif self.a_star and self.manhattan:
                    heruistic=self.calculateManhattan()
                elif self.greedy and self.misplaced:
                    heruistic=self.calculateMisplacedTiles()
                elif self.greedy and self.manhattan:
                    heruistic=self.calculateManhattan()
                # self.current_level=self.current_level+1
                self.current_state=tempCurrentState
                self.blank_tile=tempBlankTile

                return {"movePossible":True,"heruistic":heruistic}
            else:
                return {"movePossible":False,"heruistic":-1}


        if (self.blank_tile+self.row_count) in range(self.length):
            # print("Down Move")
            self.current_state[self.blank_tile+self.row_count],self.current_state[self.blank_tile]=self.current_state[self.blank_tile],self.current_state[self.blank_tile+self.row_count]
            # print(self.current_state)
            self.blank_tile=self.blank_tile+self.row_count
            self.current_level=self.current_level+1
            return True
        else:
            return False

    def moveRight(self,check=False):
        if check:
            if not (self.blank_tile+1)%self.row_count==0:
                # print("Right Move Check")
                tempCurrentState=deepcopy(self.current_state)
                tempBlankTile=deepcopy(self.blank_tile)
                self.current_state[self.blank_tile+1],self.current_state[self.blank_tile]=self.current_state[self.blank_tile],self.current_state[self.blank_tile+1]
                # print(self.current_state)
                self.blank_tile=self.blank_tile+1
                if self.a_star and self.misplaced:
                    heruistic=self.calculateMisplacedTiles()+self.current_level+1
                elif self.a_star and self.manhattan:
                    heruistic=self.calculateManhattan()
                elif self.greedy and self.misplaced:
                    heruistic=self.calculateMisplacedTiles()
                elif self.greedy and self.manhattan:
                    heruistic=self.calculateManhattan()
                # print(heruistic)
                # self.current_level=self.current_level+1
                self.current_state=tempCurrentState
                self.blank_tile=tempBlankTile

                return {"movePossible":True,"heruistic":heruistic}
            else:
                return {"movePossible":False,"heruistic":-1}
        
        if not (self.blank_tile+1)%self.row_count==0 :
            # print("Right Move")
            self.current_state[self.blank_tile+1],self.current_state[self.blank_tile]=self.current_state[self.blank_tile],self.current_state[self.blank_tile+1]
            # print(self.current_state)
            self.blank_tile=self.blank_tile+1
            self.current_level=self.current_level+1
            return True
        else:
            return False

    def moveLeft(self,check=False):

        if check:
            if math.floor((self.blank_tile-1)/self.row_count)==math.floor((self.blank_tile)/self.row_count):
                # print("Left Move Check")
                tempCurrentState=deepcopy(self.current_state)
                tempBlankTile=deepcopy(self.blank_tile)
                self.current_state[self.blank_tile-1],self.current_state[self.blank_tile]=self.current_state[self.blank_tile],self.current_state[self.blank_tile-1]
                # print(self.current_state)
                self.blank_tile=self.blank_tile-1
                if self.a_star and self.misplaced:
                    heruistic=self.calculateMisplacedTiles()+self.current_level+1
                elif self.a_star and self.manhattan:
                    heruistic=self.calculateManhattan()
                elif self.greedy and self.misplaced:
                    heruistic=self.calculateMisplacedTiles()
                elif self.greedy and self.manhattan:
                    heruistic=self.calculateManhattan()
                # self.current_level=self.current_level+1
                self.current_state=tempCurrentState
                self.blank_tile=tempBlankTile

                return {"movePossible":True,"heruistic":heruistic}
            else:
                return {"movePossible":False,"heruistic":-1}

        if math.floor((self.blank_tile-1)/self.row_count)==math.floor((self.blank_tile)/self.row_count):
            # print("Left Move")
            self.current_state[self.blank_tile-1],self.current_state[self.blank_tile]=self.current_state[self.blank_tile],self.current_state[self.blank_tile-1]
            # print(self.current_state)
            self.blank_tile=self.blank_tile-1
            self.current_level=self.current_level+1
            return True
        else:
            return False
    def calculateManhattan(self):
        manDict=0
        goal=self.goal_state
        for i in range(self.row_count):
            for j in range(self.row_count):
                if not self.current_state[self.row_count*i+j]==self.goal_state[self.row_count*i+j]:
                    for k in range(self.row_count):
                        for l in range(self.row_count):
                            if self.current_state[self.row_count*i+j]==self.goal_state[self.row_count*k+l]:
                                manDict+=(abs(i-k)+abs(l-j))

        return manDict
    def calculateMisplacedTiles(self)->int:
        count=0
        for i in range(self.length):
            if not self.current_state[i]==self.goal_state[i]:
                count=count+1
        return count
    def getOptimalMove(self):
        upMove=self.moveUp(True)

        downMove=self.moveDown(True)
        rightMove=self.moveRight(True)
        leftMove=self.moveLeft(True)

        moves=[upMove,downMove,rightMove,leftMove]

        for move in moves:
            # print(move)
            if not move["movePossible"]:
                moves.remove(move)

        # print(moves) 
        minimun=moves[0]["heruistic"]
        for move in moves:
            if move["heruistic"]<minimun:
                minimun=move["heruistic"]
        # print(minimun)
        if upMove["heruistic"]==minimun:
            return "Up"
        if downMove["heruistic"]==minimun:
            return "Down"
        if leftMove["heruistic"]==minimun:
            return "Left"
        if rightMove["heruistic"]==minimun:
            return "Right"

    def runA_StarOrGreedy(self):
        if self.current_state==self.goal_state:
            return
        move=self.getOptimalMove()
        if move=="Up":
            self.moveUp()
            self.runA_StarOrGreedy()
            print("Up->",end="")
        if move=="Down":
            self.moveDown()
            self.runA_StarOrGreedy()
            print("Down->",end="")


        if move=="Right":
            self.moveRight()
            self.runA_StarOrGreedy()
            print("Right->",end="")

        if move=="Left":
            self.moveLeft()
            self.runA_Star()
            print("Left->",end="")

    def runAlogorithms(self):
        try:
            self.a_star=True
            self.greedy=False
            self.misplaced=True
            self.manhattan=False

            self.current_level=0
            self.current_state=deepcopy(self.start_state)
            self.blank_tile=self.findBlankTile()
            print("A* with no. Of misplaced tiles:",end="")

            self.runA_StarOrGreedy()
            print("Cost=",self.current_level,end="")
        except Exception as e:
            print("Solution Not Found!")
        finally:
            print()
        try:
            self.a_star=True
            self.greedy=False
            self.misplaced=False
            self.manhattan=True

            self.current_level=0
            self.current_state=deepcopy(self.start_state)
            self.blank_tile=self.findBlankTile()
            print("A* with no. Of Manhattan Distance:",end="")
            self.runA_StarOrGreedy()
            print("Cost=",self.current_level,end="")
        except Exception as e:
            print("Solution Not Found!")
        finally:
            print()
        try:
            self.a_star=False
            self.greedy=True
            self.misplaced=True
            self.manhattan=False

            self.current_level=0
            self.current_state=deepcopy(self.start_state)
            self.blank_tile=self.findBlankTile()

            print("Greedy search with no. Of misplaced tiles:",end="")
            self.runA_StarOrGreedy()
            print("Cost=",self.current_level,end="")
        except Exception as e:
            print("Solution Not Found!")
        finally:
            print()
        try:
            self.a_star=False
            self.greedy=True
            self.misplaced=False
            self.manhattan=True

            self.current_level=0
            self.current_state=self.start_state
            self.blank_tile=self.findBlankTile()

            print("Greedy search with Manhattan distance: ",end="")
            self.runA_StarOrGreedy()
            print("Cost=",self.current_level,end="")
        except Exception as e:
            print("Solution Not Found!")
        finally:
            print()

p=Puzzle(start_state=[1,2,3,0,4,6,7,5,8],goal_state=[1,2,3,4,5,6,7,8,0])



p.runAlogorithms()



