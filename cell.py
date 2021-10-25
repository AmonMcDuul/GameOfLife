#cell
class Cell:
    def __init__(self):
        self._status = 'Dead'

    def setDead(self):
        self._status = 'Dead'

    def setAlive(self):
        self._status = 'Alive'

    def isAlive(self):
        if self._status == 'Alive':
            return True
        return False

    def getPrintCharacter(self):
        if self.isAlive():
            return ' X '
        return ' . '