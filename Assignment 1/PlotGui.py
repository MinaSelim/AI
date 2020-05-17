import numpy
import matplotlib
import matplotlib.pyplot as plt

def plotGraph(xStartingPoint, yStartingPoint, precision, grid, threshold):
  # print(grid)
   binaryGrid = createBinaryGrid(grid, threshold)
  # print(binaryGrid)
   rowSize = len(grid)
   colSize = len(grid[0])
   xEndingPoint = xStartingPoint + precision*rowSize
   yEndingPoint = yStartingPoint + precision*colSize

   text = "average: " + str(numpy.average(grid))+", std: " +str(numpy.std(grid))
   plt.text(-2,-2,text)

   extent = [xStartingPoint,xEndingPoint, yStartingPoint, yEndingPoint]
   plt.imshow(grid, origin='lower', extent=extent)
   plt.show()


def createBinaryGrid(grid, threshold):
   rowSize = len(grid)
   colSize = len(grid[0])
   binaryGrid = numpy.zeros((rowSize, colSize), dtype=int)
   for i in range(0,rowSize):
      for j in range(0,colSize):
         if grid[i,j] >= threshold:
            binaryGrid[i,j] = 1
   return binaryGrid

