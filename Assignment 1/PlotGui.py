import numpy
import matplotlib
import matplotlib.pyplot as plt

def plotGraph(xStartingPoint, yStartingPoint, precision, grid, threshold, pathArr,dataGrid):

   rowSize = len(grid)
   colSize = len(grid[0])
   xEndingPoint = xStartingPoint + precision*rowSize
   yEndingPoint = yStartingPoint + precision*colSize

   textStr = "average: " + str(numpy.average(dataGrid))+",\n std: " +str(numpy.std(dataGrid)) + ",\n threshold: "+ str(threshold)
   ax = plt.subplot()
   props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
   ax.text(0.05, 1.13, textStr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props)

   pathArr = getPlotLines(xStartingPoint,yStartingPoint,precision,pathArr)
 
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

   
   




