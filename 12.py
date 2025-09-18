grades  = { 
    "math": 5,
    "geography": 4,
    "english": 3,
    "history": 4,
    "biology": 5
}
avgBalls  = sum(grades.values()) / len(grades)
maxScore = max(grades.values())
maxBall = [subj for subj, score in grades.items() if score == maxScore]
print(avgBalls)
print(maxBall)
print(maxScore)

