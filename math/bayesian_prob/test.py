class tournament:
    total_goals = 0


match1 = tournament()
match2 = tournament()

match1.total_goals += 2
match2.total_goals += 3
tournament.total_goals += 4
print(match1.total_goals, match2.total_goals, tournament.total_goals)
