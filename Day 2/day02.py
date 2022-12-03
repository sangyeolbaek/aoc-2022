## Advent of Code Day 2 ##

# you get this many points for using one of the hands
pts_dict = {'X': 1, 'Y': 2, 'Z': 3}

# first element results in loss; second entry, victory
# (e.g. X loses against B, X wins against C, otherwise draw)
result_points = {'X': ['B', 'C'], 'Y': ['C', 'A'], 'Z': ['A', 'B']}

bonus = [0, 6] # 0 for loss, 6 for victory

total_pts = 0

def result(hands):
    them, you = hands[0], hands[1]
    if them in result_points[you]:
        return pts_dict[you] + bonus[result_points[you].index(them)]
    return pts_dict[you] + 3 # draw, reward 3 points

with open('input.txt', 'r') as fp:
    while line := fp.readline():
        total_pts += result(line.strip().split(' '))
        
print(f"Following the strategy guide, you will gain a total of {total_pts} points.")