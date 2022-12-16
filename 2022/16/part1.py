from collections import defaultdict, deque

simplifiedGraph = {}
TOTAL_TIME = 30

class Valve:
    def __init__(self, psi, neighbors):
        self.psi = psi
        self.neighbors = neighbors


def get_puzzle_input():
    file = open('input.txt')
    output = []

    for valve in [line.strip().split("; ") for line in file.readlines()]:
        curr, neighbors = valve
        currInfo = curr.split(" ")
        name = currInfo[1]
        psi = int(currInfo[4].split("=")[1])
        
        neighbors = neighbors.split(" to ")[1].split(" ")[1:]
        for i in range(len(neighbors)):
            neighbors[i] = neighbors[i].replace(",", "")
    
        output.append([name, psi, neighbors])
    return output


def getGraphAndAdjacencyList(valve_input):
    graph = defaultdict(lambda:defaultdict(int))
    adjacencyList = {}

    for name, psi, neighbors in valve_input:
        for neighbor in neighbors:
            graph[name][neighbor] = 1
        adjacencyList[name] = Valve(psi, neighbors)
    
    return graph, adjacencyList
    

def simplifyGraph(oldGraph):
    simplifiedGraph = defaultdict(lambda:defaultdict(lambda:float('inf'))) # might have to fix syntax here

    for name, valve in oldGraph.items():
        if name != 'AA' and valve.psi == 0:
            continue

        queue = deque([name])
        visited = set()
        currLevel = 0
        while queue:
            levelSize = len(queue)
            for _ in range(levelSize):
                curr = queue.popleft()
                visited.add(curr)

                if oldGraph[curr].psi != 0 and curr != name:
                    simplifiedGraph[name][curr] = min(simplifiedGraph[name][curr], currLevel)

                for neighbor in oldGraph[curr].neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
            currLevel += 1

    return simplifiedGraph


def checkWhatScoreWouldBeIfWeMakeThisDecision(a, b, c, d):
    return maximizeTotal(a, b, c, d)


def totalAmountOfPressureValveWillReleaseIfWeHeadThereAndOpenItRightNow(source, time, dest):
    if dest not in simplifiedGraph[source]:
        return -1
    else:
        distance = simplifiedGraph[source][dest]
        totalTimeToGetThereAndOpenValve = distance + 1
        psi = adjacencyList[dest].psi
        totalPotential = psi * TOTAL_TIME
        currentPotential = totalPotential - ((totalTimeToGetThereAndOpenValve + time) * psi)
        return currentPotential


def timeItWouldBeAfterWeGoToThisValveAndOpenIt(source, time, dest):
    if dest not in simplifiedGraph[source]:
        return 31
    else:
        return time + (simplifiedGraph[source][dest] + 1)


def maximizeTotal(currentNode, currTime, unopenValves, currentScore):
    if currTime > 30:
        return -1
    if currTime == 30 or not unopenValves:
        return currentScore

    maxPressureReleased = currentScore
    if currTime < 15:
        print(f'it is {currTime}; we are at {currentNode} and our choices are {unopenValves}')
    for potentialValve in unopenValves:
        newTime = timeItWouldBeAfterWeGoToThisValveAndOpenIt(currentNode, currTime, potentialValve)
        potentialScore = currentScore + totalAmountOfPressureValveWillReleaseIfWeHeadThereAndOpenItRightNow(currentNode, currTime, potentialValve)
        newListOfUnopenValvesIfWeOpenThisValve = unopenValves.copy()
        newListOfUnopenValvesIfWeOpenThisValve.remove(potentialValve)

        maxPressureReleased = max(checkWhatScoreWouldBeIfWeMakeThisDecision(potentialValve, newTime, newListOfUnopenValvesIfWeOpenThisValve, potentialScore), maxPressureReleased)

    return maxPressureReleased

def part1():
    # map out the input into edges
    # use the edges to create an adjacencyList
    # use the Adjacency List to make Valve objects out of the data
    # Simplify the graph by removing all nodes with valve 0 and adding edge weights
    # backtrack

    global simplifiedGraph
    simplifiedGraph = simplifyGraph(adjacencyList)

    unopenValves = set(simplifiedGraph.keys())
    unopenValves.remove('AA')

    return maximizeTotal('AA', 0, unopenValves, 0)


_, adjacencyList = getGraphAndAdjacencyList(get_puzzle_input())

if __name__ == '__main__':
    print(part1())