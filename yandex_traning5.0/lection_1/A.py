vasya_p_tree, vasya_range = map(int, input().split());
masha_q_tree, masha_range =  map(int, input().split());

min_vasya = vasya_p_tree - vasya_range;
max_vasya = vasya_p_tree + vasya_range;
min_masha = masha_q_tree - masha_range;
max_masha = masha_q_tree + masha_range;

if (vasya_p_tree == masha_q_tree):
    print( vasya_range * 2  + 1 if vasya_range >= masha_range else masha_range * 2 + 1);
elif ((max_vasya < min_masha and min_vasya < max_masha) or (max_masha < min_vasya and min_masha < max_vasya)):
    print((vasya_range * 2) + (masha_range * 2) + 2);
else:
    print( abs(min_vasya if min_vasya < min_masha else min_masha) + abs(max_vasya if max_vasya > max_masha else max_masha) + 1)
    
# ОК