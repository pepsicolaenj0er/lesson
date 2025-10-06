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
            available.append(i)  # ❌ можно не собирать список, а сразу итерироваться по героям

    if action == "b":  # BAN
        best_result = solve(step + 1, used_hero, dire, radiant)  
        # ⚠️ Тут у тебя получается, что "бан можно пропустить".
      

        for hero in available:
            new_used_hero = used_hero | (1 << hero)
            result = solve(step + 1, new_used_hero, dire, radiant)

            if team == 1:  
                if result > best_result:  # ❌ это можно заменить на max(best_result, result)
                    best_result = result
            else:  
                if result < best_result:  # ❌ тут можно min(best_result, result)
                    best_result = result
        return best_result

    else:  # PICK
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
                    if result > best_result:  # ❌ можно заменить на max()
                        best_result = result
                else:  
                    if result < best_result:  # ❌ можно заменить на min()
                        best_result = result
        return best_result


print(solve(0, 0, 0, 0))
