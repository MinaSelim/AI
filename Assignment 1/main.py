import ShapeReader
import PlotGui
import numpy
import math
from datetime import datetime
import Astar

def convertCardinalPointToArrPoint (xStartingPoint, yStartingPoint, precision, point, grid):
   xdiff = point[0] - xStartingPoint 
   ydiff = point[1] - yStartingPoint

   x = math.floor(xdiff/precision)
   y = math.floor(ydiff/precision)
   return (x,y)

filename = "Shapes/crime_dt"
xStartingPoint = -73.59
xEndingPoint = -73.55
yStartingPoint = 45.49
yEndingPoint = 45.53
precision = 0.002
percentile = 50

print("please enter start latitude("+str(yStartingPoint)+"<=L<"+str(yEndingPoint) +"):")
sLat = float(input())
print("please enter start Longitude("+str(xStartingPoint)+"<=L<"+str(xEndingPoint) +"):")
sLong = float(input())
print("please enter end latitude("+str(yStartingPoint)+"<=L<"+str(yEndingPoint) +"):")
eLat = float(input())
print("please enter end Longitude("+str(xStartingPoint)+"<=L<"+str(xEndingPoint) +"):")
eLong = float(input())
print("please enter the percentile 0<=p<=100")
percentile = int(input())


grid = ShapeReader.getIntensityGridFromFileName(filename, xStartingPoint,
xEndingPoint, yStartingPoint, yEndingPoint, precision)

threshold = numpy.percentile(grid, percentile)
binaryGrid = Astar.createBinaryGrid(grid,threshold)


start = convertCardinalPointToArrPoint(xStartingPoint, yStartingPoint, precision, (sLong, sLat),grid)
end = convertCardinalPointToArrPoint(xStartingPoint, yStartingPoint, precision, (eLong, eLat),grid)

startTime = datetime.now()
path = Astar.aStar(binaryGrid,start,end)
endTime = datetime.now()- startTime

print("A* took the following amount of time in seconds: " + str(endTime.total_seconds()))

pathXarr = []
pathYarr = []

if not(path is None):
   for point in path :
      pathXarr.append(point[0]+0.5)
      pathYarr.append(point[1]+0.5)



pathArr = (pathXarr, pathYarr)
print(path)

PlotGui.plotGraph(xStartingPoint, yStartingPoint, precision, binaryGrid , threshold, pathArr,grid)
