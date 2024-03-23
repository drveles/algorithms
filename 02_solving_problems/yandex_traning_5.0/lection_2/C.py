counter_ropes = int(input())
ropes_lens_list = list(map(int, input().split()))
max_rope_lens = max(ropes_lens_list)
sum_ropes_lens = sum(ropes_lens_list)
mininal_taken_rope = 1

if sum_ropes_lens - max_rope_lens - max_rope_lens >= 0:
    mininal_taken_rope = sum_ropes_lens
else:
    mininal_taken_rope = max_rope_lens - (sum_ropes_lens - max_rope_lens)

print(mininal_taken_rope)

# OK