need_goals = 0;
input_string = input();
time_1_team_1, time_1_team_2 = map(int, input_string.split(':'));
input_string = input();
time_2_team_1, time_2_team_2 = map(int, input_string.split(':'));
home_round = int(input());
team_1_goals = time_1_team_1 + time_2_team_1;
team_1_homegoals = time_1_team_1 if (home_round == 1) else time_2_team_1;
team_2_goals = time_1_team_2 + time_2_team_2;
team_2_homegoals = time_2_team_2 if (home_round == 1) else time_1_team_2;
unpriority_goal = 0;

if(team_1_homegoals < team_2_homegoals or (team_1_homegoals == team_2_homegoals and home_round == 2)):
    unpriority_goal = 1;

if(team_1_goals > team_2_goals):
    need_goals = 0;
elif(team_1_goals == team_2_goals):
    need_goals = 1 + unpriority_goal;
else:
    if(home_round == 1):
        need_goals = team_2_goals - team_1_goals;
        if (need_goals == time_2_team_2):
            need_goals += 1;
    else:
        need_goals = team_2_goals - team_1_goals + 1;

print(need_goals);