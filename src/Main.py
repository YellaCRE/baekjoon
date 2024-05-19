import sys
INPUT = sys.stdin.readline

# 인하대 A번 창고지기
graph = list(INPUT().strip())

robot_idx, box_idx, goal_idx = -1, -1, -1
for idx in range(len(graph)):
    if graph[idx] == '@':
        robot_idx = idx
    if graph[idx] == '#':
        box_idx = idx
    if graph[idx] == '!':
        goal_idx = idx


def solve(robot, box, goal):
    if not (robot < box < goal or goal < box < robot):
        return -1

    robot_move = abs(box - robot) - 1
    box_move = abs(goal - box)

    return robot_move + box_move


print(solve(robot_idx, box_idx, goal_idx))