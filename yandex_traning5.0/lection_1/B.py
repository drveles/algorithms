need_goals = 0;
input_string = input();
time_1_team_1, time_1_team_2 = map(int, input_string.split(':'));
input_string = input();
time_2_team_1, time_2_team_2 = map(int, input_string.split(':'));
home_round = int(input());
team_1_goals = time_1_team_1 + time_2_team_1;
team_1_guestgoals = time_2_team_1 if (home_round == 1) else time_1_team_1;
team_2_goals = time_1_team_2 + time_2_team_2;
team_2_guestgoals = time_1_team_2 if (home_round == 1) else time_2_team_2;
unpriority_goal = 0;

if (team_1_goals > team_2_goals):
    need_goals = 0;
elif(team_1_goals == team_2_goals):
    if(team_1_guestgoals > team_2_guestgoals):
        need_goals = 0;
    else:
        need_goals = 1;
else:
    need_goals = team_2_goals - team_1_goals;
    if(home_round == 1):
        team_1_guestgoals += need_goals;
    if(team_1_guestgoals <= team_2_guestgoals):
        need_goals += 1;

print(need_goals);

# OK, Artur S. helps me