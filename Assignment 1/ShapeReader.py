import shapefile
import numpy
import math

def getIntensityGridFromFileName(fileName, xStartingPoint,
xEndingPoint, yStartingPoint, yEndingPoint, precision):
   shapes = getShapesFromShapeFile(fileName)
   grid = getGridFromShapes(xStartingPoint,xEndingPoint,yStartingPoint, yEndingPoint, precision)
   for shape in shapes:
      addPointToArray(xStartingPoint, yStartingPoint, precision, shape.points[0], grid)
   
   return grid


   
def getShapesFromShapeFile(fileName):
   sf = shapefile.Reader(fileName)
   shapes = sf.shapes()
   return shapes

def getGridFromShapes(xStartingPoint,xEndingPoint, 
yStartingPoint, yEndingPoint, precision):
   rowSize = int(calculateNumberOfSteps(xStartingPoint, xEndingPoint, precision))
   columnSize = int(calculateNumberOfSteps(yStartingPoint, yEndingPoint, precision))
   grid = numpy.zeros((rowSize, columnSize), dtype=int)
   return grid

def calculateNumberOfSteps(startingPoint, endingPoint, precision):
   diff = startingPoint - endingPoint
   numberOfJumps = abs(diff/precision)
   x = math.ceil(round(numberOfJumps, 6))
   return x

def addPointToArray(xStartingPoint, yStartingPoint, precision, point, grid):
   xdiff = point[0] - xStartingPoint 
   ydiff = point[1] - yStartingPoint
   if point[0] > -73.55-0.002 and point[1]>45.53-0.002 :
      print(1)
   x = math.floor(xdiff/precision)
   y = math.floor(ydiff/precision)
   if x == 19 and y == 19:
      print(2)

   grid[x,y] +=  1
