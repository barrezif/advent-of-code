from typing import Optional


class Sensor:
    def __init__(self, sCoord, bCoord):
        self.pos = sCoord
        self.range = self.getRange(sCoord, bCoord)

    def getRange(self, beacon: list[int], sensor: list[int]) -> int:
        return abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])
        
    def getCoverageRangeForRow(self, row: int) -> Optional[list[int]]:
        """
        Sensor (0,0) with range 2 spans -
                2 tiles before / after it in row  0        [-2,2]
                1 tile  before / after it in rows 1 and -1 [-1,1]
                0 tiles before / after it in rows 2 and -1 [0 ,0]

        Following this logic we can say that
        for integers n,m in [-inf, inf] and r in [0, inf] and z <= r

        Sensor (n,m) with range r spans -
                r   tiles before / after it in row  m            [m-r, m+r]
                r-1 tiles before / after it in rows n+1 and n-1  [m-r+1, m+r-1]
                r-z tiles before / after it in rows n+z and n-z  [m-r+z, m+r-z]

        And using that, we can get the intervals a sensor covers a row
        """
        if  row >= self.pos[1]:
            reach = self.pos[1] + self.range
        elif row < self.pos[1]:
            reach = self.pos[1] - self.range

        if (row >= self.pos[1] and reach >= row or
            row <  self.pos[1] and reach <= row):
            diff = abs(row - reach)
            return [self.pos[0] - diff, self.pos[0] + diff]