import entities

#I moved my creature/light configuration to the entities file




case_example=[0,0]
case_example[0]=( entities.creature_configuration( 10, 5, 20, True, 'red' ),
             entities.creature_configuration( 10, 4, 6, False,),
             entities.light_configuration( 5, speed=5 , random=True ) )

case_example[1] = ( entities.creature_configuration(15, color='blue'),
             entities.creature_configuration( 5, False, 10, 5),
             entities.light_configuration( 5, 8 ))

#Creature setup is (count, speed, space, attract, color , position)
#Light setup is (count, speed, random, color)

