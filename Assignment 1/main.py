import ShapeReader
import PlotGui
import numpy
import Astar

filename = "Shapes/crime_dt"
xStartingPoint = -73.59
xEndingPoint = -73.55
yStartingPoint = 45.49
yEndingPoint = 45.53
precision = 0.002
percentile = 50


grid = ShapeReader.getIntensityGridFromFileName(filename, xStartingPoint,
xEndingPoint, yStartingPoint, yEndingPoint, precision)

threshold = numpy.percentile(grid, percentile)
binaryGrid = Astar.createBinaryGrid(grid,threshold)
print(binaryGrid)
pos = [(0,0),(0,1)]

path = Astar.aStar(binaryGrid,(0,0),(19,0))

pathXarr = []
pathYarr = []

for point in path :
   pathXarr.append(point[0]+0.5)
   pathYarr.append(point[1]+0.5)

pathArr = (pathXarr, pathYarr)
print(path)

PlotGui.plotGraph(xStartingPoint, yStartingPoint, precision, binaryGrid , threshold, pathArr)
