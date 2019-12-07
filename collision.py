import math

def Velocity(angle, length):
  x = length*math.cos(angle)
  y = length*math.sin(angle)
  return Vector(x,y)

class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.angle = math.atan2(y,x)

# ---------------------------------------------------------------
# ---------------------------------------------------------------
# The stationary would be a wall or another creature.
# Code can be adjusted for 2 moving creatures, but not necessary
def DetermineNewHeading( creature, stationary, speed ):
  
  # Determine the point of collision, which also defines the angle
  collision = Vector( stationary[0]-creature[0], \
                      stationary[1]-creature[1] )

  # Define the tangent to the point of collision
  collision_tangent = Vector( stationary[1]-creature[1], \
                              -(stationary[0]-creature[0]))

  # Normalize the tangent making it length 1
  tangent_length = (collision_tangent.x**2 + collision_tangent.y**2)**0.5
  normal_tangent = Vector( collision_tangent.x/tangent_length, \
                           collision_tangent.y/tangent_length)

  # relative velocity = robot because stationary circle has 0 velocity
  # See flatredball to modify code for 2 moving objects

  rel_velocity = Velocity(creature[2] , speed)


  # Determine the velocity vector along the tangent
  length = rel_velocity.x*normal_tangent.x + rel_velocity.y*normal_tangent.y
  tangent_velocity = Vector( normal_tangent.x*length, normal_tangent.y*length)

  # Determine the velocity vector perpendicular to the tangent
  perpendicular = Vector(rel_velocity.x-tangent_velocity.x, \
                         rel_velocity.y-tangent_velocity.y )

  # New Heading
  # This is for robot only. See flatredball to move both entities
  new_heading = Vector( (rel_velocity.x-2*perpendicular.x), \
                        (rel_velocity.y-2*perpendicular.y))
  #print (new_heading.angle)
  return math.degrees(new_heading.angle)

