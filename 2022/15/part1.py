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


def mergeIntervals(intervals:list[list[int]]) -> Optional[list[list[int]]]:
    """
    Now we essentially have this leetcode problem
    https://leetcode.com/problems/merge-intervals/description/
    Given a list of ranges, we sort them and check them one by one,
    merging them if they overlap at any point
    """
    intervals = sorted(intervals)
    combinedIntervals = [intervals[0]]
    for left, right in intervals[1:]:
        if combinedIntervals[-1][1] >= left:
            combinedIntervals[-1][1] = max(combinedIntervals[-1][1], right)
        else:
            combinedIntervals.append([left, right])
    return combinedIntervals


def part1(row:int) -> int:
    pInput = get_puzzle_input()
    sensors: Sensor = getSensors(pInput)
    
    ranges = [rowRange for sensor in sensors if (rowRange:=sensor.getCoverageRangeForRow(row))]
    
    combinedRanges = mergeIntervals(ranges)

    # returns the sum of the space taken up by each interval
    return sum([right-left for left,right in combinedRanges])


if __name__ == '__main__':
    ROW_TO_SEARCH = 2000000
    print(part1(ROW_TO_SEARCH))


