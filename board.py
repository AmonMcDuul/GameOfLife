#board
from cell import Cell
from random import randint

class Board:
    def __init__(self , rows , columns):
        self._rows = rows
        self._columns = columns   
        self._grid = [[Cell() for column_cells in range(self._columns)] for rij_cells in range(self._rows)]
        self._generateBoard()

    def drawBoard(self):
        print('\n'*2)
        for rij in self._grid:
            for column in rij:
                print (column.getPrintCharacter(),end='')
            print ()

    def _generateBoard(self):
        for rij in self._grid:
            for column in rij:
                changeNumber = randint(0,2)
                if changeNumber == 1:
                    column.setAlive()

    def neighbour(self, checkRij , checkColumn):
        searchMin = -1
        searchMax = 2

        neighbourList = []
        for rij in range(searchMin,searchMax):
            for column in range(searchMin,searchMax):
                neighbourRij = checkRij + rij
                neighbourColumn = checkColumn + column 
                goodNeighbour = True
                if (neighbourRij) == checkRij and (neighbourColumn) == checkColumn:
                    goodNeighbour = False
                if (neighbourRij) < 0 or (neighbourRij) >= self._rows:
                    goodNeighbour = False
                if (neighbourColumn) < 0 or (neighbourColumn) >= self._columns:
                    goodNeighbour = False
                if goodNeighbour:
                    neighbourList.append(self._grid[neighbourRij][neighbourColumn])
        return neighbourList  

    #update board
    def updateBoard(self):
        print ('\n''\n''updated board')
        alive = []
        killed = []

        for rij in range(len(self._grid)):
            for column in range(len(self._grid[rij])):
                neighbour = self.neighbour(rij , column)
                neighbourCount = []
                for neighbourCell in neighbour:
                    if neighbourCell.isAlive():
                        neighbourCount.append(neighbourCell)
                cellObject = self._grid[rij][column]
                statusCell = cellObject.isAlive()
                if statusCell == True:
                    if len(neighbourCount) < 2 or len(neighbourCount) > 3:
                        killed.append(cellObject)
                    if len(neighbourCount) == 3 or len(neighbourCount) == 2:
                        alive.append(cellObject)
                else:
                    if len(neighbourCount) == 3:
                        alive.append(cellObject)
        for items in alive:
            items.setAlive()

        for items in killed:
            items.setDead()