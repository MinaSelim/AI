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

   x = math.floor(xdiff/precision)
   y = math.floor(ydiff/precision)

   grid[y,x] +=  1
