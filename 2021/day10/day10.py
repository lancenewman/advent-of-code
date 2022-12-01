from collections import deque

inputFile = 'day10/input.txt'
#inputFile = 'day10/test.txt'
lines = [line.strip() for line in open(inputFile).readlines()]


baseChunks = {'[': ']', '{': '}', '(': ')', '<': '>'}
corruptionPoints = {')': 3, ']': 57, '}': 1197, '>': 25137}
completionPoints = {')': 1, ']': 2, '}': 3, '>': 4}


def isCorrupted(line: str) -> set:
    stack = deque()
    for delim in line:
        if delim in baseChunks.keys():
            stack.append(delim)
        elif delim != baseChunks[stack.pop()]:
            return (True, delim)
    return (False, None)


def getCompletionString(line: str) -> str:
    stack = deque()
    for delim in line:
        if delim in baseChunks.keys():
            stack.append(delim)
        else:
            stack.pop()

    if len(stack) > 0:
        completionString = ''
        while stack:
            completionString += baseChunks[stack.pop()]
        return completionString
    return None


def getCompletionScore(line: str) -> int:
    score = 0
    for char in line:
        score *= 5
        score += completionPoints[char]
    return score


corruptionScore = 0
completionScores = list()
for line in list(lines):
    corrupt, char = isCorrupted(line)
    if corrupt:
        # Part 1
        corruptionScore += corruptionPoints[char]
    else:
        # Part 2
        completionString = getCompletionString(line)
        completionScore = getCompletionScore(completionString)
        print(f'{completionString}: {completionScore}')
        completionScores.append(completionScore)
        print(completionScores)

print(f'Part 1: {corruptionScore}')
print(f'Part 2: {sorted(completionScores)[len(completionScores) // 2]}')
