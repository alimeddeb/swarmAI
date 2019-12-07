#------------------------------------------------------------------------------
#-----------------------   Importing


import entities
import collision
import TestConfiguration
import turtle as t
from random import *



#------------------------------------------------------------------------------
#-----------------------   Classes

class Arena:

    def __init__(self, configuration_example):
        self.configuration=configuration_example


    #drawing grid and initializing creature values
    def arena_intialize(self):
        self.InitializeGraphics()
        self.initialize_creatures()
        self.bounds=entities.wall()
        


    #Drawing the creatures
    def initialize_creatures(self):
        for group in self.configuration:
            group.draw()




    def update(self):
        #function that updates the screen with new graphics
        bounds=self.bounds
        t.clearstamps()
        wall=entities.wall()
        #reversed the list to start with the light
        for group in reversed(self.configuration):
            if isinstance(group, entities.creature_configuration):
                #do this if it's a creature
                group.move()
                group.check_wall_colision(bounds)
                group.draw()
                group.keep_space()
                group.find_closest_light(self.configuration[-1] , group.attract)
            else:
                #do this if it's a light
                group.move()
                group.check_random()
                group.check_wall_colision(bounds)
                group.draw()
                    
        

                     
    
    def InitializeGraphics(self):
        #Function draws the outer box
        t.speed(0)
        t.setup( width = 1000, height = 650, startx = None, starty = None)
        t.hideturtle()
        t.pu()
        walls=entities.wall()
        t.fd(walls.x)
        t.setheading(90)
        t.pd()
        t.fd(walls.y)
        for i in range(2):
            t.lt(90)
            t.fd(2*walls.x)
            t.lt(90)
            t.fd(2*walls.y)








#-------------------------------------------------------------------------
#------------ Main Program Body

def main():
    arena=Arena(TestConfiguration.case_example[0]) #can change 0 to a 1 // check TestConfiguration file for more settings
    arena.arena_intialize()
    try:
        while True:
            arena.update()
    except KeyboardInterrupt:
       print('Done swarming.')




#-------------------------------------------------------------------------
#------------ Executing the Simulation

if __name__=='__main__' :
  main()
























