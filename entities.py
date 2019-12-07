#------------------------------------------------------------------------------
#-----------------------   Importing


from random import *
import turtle as t
import math as m
import collision
t.speed(0)
t.hideturtle()
t.tracer(0, 0)


#------------------------------------------------------------------------------
#-----------------------   Classes

class entity:
    #this is the main class from which everything is dervied
    def __init__(self, count, speed, color):
        self.speed=speed
        self.count=count
        self.color=color
        self.population=[]
        self.shape=None

    def populate(self):
        #Function that fills ant type of entities with its individuals
        for population_number in range(self.count):

            #an individual has [Xcoordinate , Ycor , angle , color ]
            individual=[randint(-430,430), randint(-280,280), randint(0,359) , self.color]
            # adding the individual to the population list
            self.population.append(individual)

    def draw(self):
        #function that draws the indivudals from a population
        for individual in self.population:
            t.pu()
            t.goto(individual[0], individual[1])
            t.setheading(individual[2])
            t.shape(self.shape)
            t.color(self.color)
            t.stamp()
        t.update()

    def move(self):
        #Function that moves
        for individual in self.population:
            t.goto(individual[0], individual[1])
            t.setheading(individual[2])
            t.fd(self.speed)
            # [0] refers to X  [1] refers to Y
            individual[0]=t.xcor()
            individual[1]=t.ycor()

    def check_wall_colision(self,wall):
        #function checks 
        for individual in self.population:
            #initializing variables
            bounds=[wall.x , wall.y]
            individualX=individual[0]
            individualY=individual[1]

            #verifying if the individual is out of bounds
            if abs(individualX)-2 > abs(wall.x) or abs(individualY)-2 > abs(wall.y):
                new_heading = collision.DetermineNewHeading( individual, bounds, self.speed )

                #changing angle to bounce off 
                individual[2]=new_heading

                #checking if individual leaves area and correcting it
                if individualX < -wall.x :
                    individualX=-wall.x
                    
                elif individualX > wall.x:
                    individualX=wall.x

                if individualY <-wall.y :
                    individualY=-wall.y

                elif individualY >wall.y :
                    individualY=wall.y 

                #re-updating the X and Y of the individual
                individual[0]=individualX
                individual[1]=individualY


    # --- Couldn't get this to work ---
    def bouncing_entities(self, other_entity):
        #Function makes 2 touching entities bounce
        for individual in self.population:
            for other_individual in other_entity.population:

                if individual[0]==other_individual[0] and individual[1]==other_individual[1]:
                    old_cord=[individual[0],individual[1]]
                    old_cord[0]+=1
                    old_cord[1]+=1
                    individual[2]=collision.DetermineNewHeading( individual, old_cord, self.speed )




class creature_configuration(entity):
    #this class holds all the creatures

    def __init__(self, count, speed=3, space=10, attract=True, color='black'):
        super().__init__(count, speed, color)
        self.space=space
        self.attract=attract
        self.color=color
        self.shape='arrow'
        super().populate()

    def keep_space(self):
        for individual in self.population:
            for Cindividual in self.population: #Cindividual is the compared individual
            # [0] refers to the X coordinate /  [1] refers to the Y coordinate

            #calclating the distance between the individual and the other one
                distance=m.hypot(Cindividual[0] - individual[0], Cindividual[1] - individual[1])

            #checking if the creatures are too close
                if distance>0 and distance <= self.space:
                    angle_difference=m.degrees(m.atan2(Cindividual[0] - individual[0], Cindividual[1] - individual[1]))
                    individual[2]+= angle_difference/self.speed
                    Cindividual[2]-= angle_difference/self.speed
                    
                    
                
            



    def find_closest_light(self, light_configuration, attract):
        #functions searches for closest light
        for individual in self.population:
            min_dist=m.inf
            for light_individual in light_configuration.population:
                distance=m.hypot(light_individual[0] - individual[0], light_individual[1] - individual[1])
                #check if there's an even closer light
                if distance <= min_dist:
                    min_dist = distance
                    closest_light=light_individual
                    # changing the individual's heading depending on its attract nature
                    angle_difference=m.degrees(m.atan2(light_individual[0] - individual[0], light_individual[1] - individual[1]))
                                
                    # changing the individual's heading depending on its attract nature
                    if attract==True:
                        individual[2]+=0.1*angle_difference*1/self.speed

                    if attract==False:              
                        individual[2]-=0.1*angle_difference*1/self.speed

        



class light_configuration(entity):
    #this class holds all lights
    def __init__(self, count, speed=5, random=False, color='yellow'):
        super().__init__(count, speed, color)
        self.random=random
        self.population=[]
        self.shape='circle'
        super().populate()
        #super().draw()

        

    def check_random(self):
        #function randomly changes light's heading 
        if self.random==True:
            for individual in self.population:
                randomizer=randint(0,1000)
                # 0.2% chance of changing heading
                if randomizer < 2:
                    individual[2]=randint(0,359)

            
                



class wall(entity):
    #this class contains the wall's boundaries coordinates
    def __init__(self, count=1, speed=0, color='black'):
        super().__init__(count, speed, color)
        self.x=450
        self.y=300





    
