# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    n = len(Text)
    k = len(Pattern)
    for i in range(n-k+1):
        subtext = Text[i:i+k]
        distance = HammingDistance(subtext,Pattern)
        if distance <= d:
            count += 1
    return count


# Insert your HammingDistance function on the following line.
def HammingDistance(p, q):
    hamming_distance = 0
    n = min(len(p),len(q))
    for i in range(n):
        if p[i] != q[i]:
            hamming_distance += 1
    return hamming_distance



### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(ApproximatePatternCount(lines[0],lines[1],int(lines[2])))
