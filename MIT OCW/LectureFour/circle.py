#THIS SOURCE CODE IS ASSOCIATED WITH CHAPTER 4.5 MODULES IN INTRO TO COMPSCI USING PYTHON
#IN THIS FILE WE WILL GO OVER DETAILS ABOUT MODULES AND USING THEM FROM FILE TO FILE 

pi = 3.14159

def area(radius):
  return pi*(radius*2)

def circumference(radius):
  return 2*pi*radius

def spherSurface(radius):
  return 4.0*area(radius)

def sphereVolume(radius):
  return (4.0/3.0)*pi*(radius**3)
