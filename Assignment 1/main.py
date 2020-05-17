import ShapeReader
import PlotGui
import numpy

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

PlotGui.plotGraph(xStartingPoint, yStartingPoint, precision, grid, threshold)
