from functools import lru_cache
import sys

input = sys.stdin.readline

heroes = int(input())
strengthHeroes = list(map(int, input().split()))
numberMoves = int(input())
actions = []
for _ in range(numberMoves):
    action, team = input().split()
    actions.append((action, int(team)))

@lru_cache(None)
def solve(step, used_hero, dire, radiant):
    if step == numberMoves:
        return dire - radiant

    action, team = actions[step]
    available = []
    for i in range(heroes):
        if not (used_hero & (1 << i)):
            available.append(i)

    if action == "b":  
        best_result = solve(step + 1, used_hero, dire, radiant) 
        for hero in available:
            new_used_hero = used_hero | (1 << hero)
            result = solve(step + 1, new_used_hero, dire, radiant)
            if team == 1:
                max(best_result, result)
                best_result = result
            else:
                min(best_result, result)
                best_result = result
        return best_result
    else:  
        best_result = None
        for hero in available:
            new_used_hero = used_hero | (1 << hero)
            if team == 1:
                result = solve(step + 1, new_used_hero, dire + strengthHeroes[hero], radiant)
            else:
                result = solve(step + 1, new_used_hero, dire, radiant + strengthHeroes[hero])

            if best_result is None:
                best_result = result
            else:
                if team == 1:
                    max(best_result, result)
                    best_result = result
                else:
                    min(best_result, result)
                    best_result = result
        return best_result

print(solve(0, 0, 0, 0))