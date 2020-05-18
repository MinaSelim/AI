import AStarNode
import numpy
   

def aStar(binaryGrid, starIndex, endIndex):
   startNode = AStarNode.Node(None, starIndex)
   endNode = AStarNode.Node(None, endIndex)

   openList = []
   closedList = []
   possibleMoves = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]

   openList.append(startNode)

   while len(openList) > 0:

      currentNode = openList[0]
      currentNodeIndex = 0

      i = 0

      #ToDo: maybe use a priority queue later if algo is too slow
      for i in range(len(openList)):
         if openList[i].f < currentNode.f:
            currentNode = openList[i]
            currentNodeIndex = i
      
      openList.pop(currentNodeIndex)
      closedList.append(currentNode)

      if currentNode.pos == endNode.pos:
         path = []
         node = currentNode
         while node != None:
            path.append(node)
            node = currentNode.parent
         return path
      
      childNodes = []
      for movement in possibleMoves:
         childPosition = (currentNode.pos[0] + movement[0], currentNode.pos[1]+movement[1])
         if not(positionIsValidAndTraversable(childPosition,binaryGrid)):
            continue
         
         childNode = AStarNode.Node(currentNode, childPosition)
         childNode.g = currentNode.g + 1 if abs(movement[0])+abs(movement[1]) == 1 else currentNode.g + 1.5
         childNodes.append(childNode)
         
      for childNode in childNodes:

         for closedNode in closedList:
            if childNode.pos == closedNode.pos:
               continue
         
         childNode.h = euclidianDistance(childNode.pos, endIndex)
         childNode.f = childNode.g + childNode.h

         for openNode in openList:
            if childNode.pos == openNode.pos and childNode.g > openNode.g:
               continue

         openList.append(childNode)
      


def positionIsValidAndTraversable(position, binaryGrid):
   nodeIsValid = not(position[0] < 0 or position[1] < 0 or position[0] >= (len(binaryGrid)) or  position[1] >= (len(binaryGrid[0])))
   nodeIsTraverable = (binaryGrid[position[0],position[1]]) == 0
   return nodeIsValid and nodeIsTraverable

def createBinaryGrid(grid, threshold):
   rowSize = len(grid)
   colSize = len(grid[0])
   binaryGrid = numpy.zeros((rowSize, colSize), dtype=int)
   for i in range(0,rowSize):
      for j in range(0,colSize):
         if grid[i,j] >= threshold:
            binaryGrid[i,j] = 1
   return binaryGrid

def manhattanDistance(position, endIndex):
   return abs(position[0] - endIndex[0]) + abs(position[1] - endIndex[1])


def euclidianDistance(position, endIndex):
   return numpy.sqrt((position[0] - endIndex[0])**2 + (position[1] - endIndex[1])**2)