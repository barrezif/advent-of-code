from collections import Counter, defaultdict
def get_puzzle_input():
    file = open('input.txt')
    puzzle_input = [num.strip() for num in file.readlines()]

    return puzzle_input

def get_map(puzzle_input):
    _map = defaultdict(lambda:[], {})
    for line in puzzle_input:
        match line.split('-'):
            case ['start', other]:
                _map['start'].append(other)
            case [other, 'start']:
                _map['start'].append(other)
            case [other, 'end']:
                _map[other].append('end')
            case ['end', other]:
                _map[other].append('end')
            case [node1, node2]:
                _map[node2].append(node1)
                _map[node1].append(node2)
    return _map


def main():
    _map = get_map(get_puzzle_input())
    return travel('start', _map, [], False)

def travel(current, _map, tracker, hault):
    new_map = _map.copy()
    if current == 'end':
        return 1
    
    if current.islower() and current in _map:
        if hault:
            new_map.pop(current)
        elif current in tracker:
            hault = True
            for item in tracker:
                new_map.pop(item)
            tracker = []
        else:
            tracker.append(current)

    return sum([travel(path, new_map, tracker[:], hault) for path in _map[current]])

print(main())