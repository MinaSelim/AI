import numpy
import matplotlib
import matplotlib.pyplot as plt

def plotGraph(xStartingPoint, yStartingPoint, precision, grid, threshold):

   rowSize = len(grid)
   colSize = len(grid[0])
   xEndingPoint = xStartingPoint + precision*rowSize
   yEndingPoint = yStartingPoint + precision*colSize

   text = "average: " + str(numpy.average(grid))+", std: " +str(numpy.std(grid))
   plt.text(-2,-2,text)

   extent = [xStartingPoint,xEndingPoint, yStartingPoint, yEndingPoint]
   plt.imshow(grid, origin='lower', extent=extent)
   plt.show()



