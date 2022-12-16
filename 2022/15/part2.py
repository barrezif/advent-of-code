from typing import Optional
from Sensor import Sensor

def get_puzzle_input() -> list[list[str]]:
    """ Parse input text """
    file = open('input.txt')
    pInput = [line.strip().split(": ") for line in file.readlines()]
    return [[p.split("at ")[1] for p in pp] for pp in pInput]


def extractCoords(input: str) -> tuple[int,int]:
    """ Parses input text and returns coordinates from string """
    x, y = input.split(", ")
    x = int(x.split("=")[1])
    y = int(y.split("=")[1])
    return x, y


def getSensors(pInput: str) -> list[Sensor]:
    """ More input text parsing and instantiating Sensor class"""
    sensors: Sensor = []
    for pair in pInput:
        sensor, beacon = pair
        sensorCoords = extractCoords(sensor)
        beaconCoords = extractCoords(beacon)
        sensors.append(Sensor(sensorCoords, beaconCoords))
    return sensors


def gapFoundInRange(intervals:list[list[int]]) -> Optional[int]:
    """
    Still following the same logic as the mergeInterval function in pt1
    but we're returning the skipped over cell once we encounter it
    """
    intervals = sorted(intervals)
    combinedIntervals = [intervals[0]]
    for left, right in intervals[1:]:
        if combinedIntervals[-1][1] >= left:
            combinedIntervals[-1][1] = max(combinedIntervals[-1][1], right)
        else:
            if left > combinedIntervals[-1][1] + 1:
                return left-1
            combinedIntervals.append([left, right])


def part2(bound:int) -> int:
    pInput = get_puzzle_input()
    sensors: Sensor = getSensors(pInput)
    
    for row in range(bound):
        ranges = [rowRange for sensor in sensors if (rowRange:=sensor.getCoverageRangeForRow(row))]
        if res := gapFoundInRange(ranges):
            return res * bound + row


if __name__ == '__main__':
    BOUNDS = 4000000
    print(part2(BOUNDS))


