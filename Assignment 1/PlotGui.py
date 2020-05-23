import numpy
import matplotlib
import matplotlib.pyplot as plt

def plotGraph(xStartingPoint, yStartingPoint, precision, grid, threshold, pathArr):

   rowSize = len(grid)
   colSize = len(grid[0])
   xEndingPoint = xStartingPoint + precision*rowSize
   yEndingPoint = yStartingPoint + precision*colSize

   pathArr = getPlotLines(xStartingPoint,yStartingPoint,precision,pathArr)
   text = "average: " + str(numpy.average(grid))+", std: " +str(numpy.std(grid))
   plt.text(-2,-2,text) 
   subplt = plt.subplot()
   subplt.plot((pathArr[0]),pathArr[1])

   extent = [xStartingPoint,xEndingPoint, yStartingPoint, yEndingPoint]
   plt.imshow(grid, origin='lower', extent=extent)
 
   plt.show()
   
def getPlotLines(xStartingPoint, yStartingPoint, precision, pathArr):

   pathXarrconverted = []
   pathYarrconverted = []

   for val in pathArr[0] :
      pathXarrconverted.append(xStartingPoint + val*precision)

   for val in pathArr[1] :
      pathYarrconverted.append(yStartingPoint + val*precision)
   
   return (pathXarrconverted, pathYarrconverted)

   
   




