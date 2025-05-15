wifi_enabled: bool = True
has_electricity: bool = True
has_subscription: bool = True

if wifi_enabled and has_electricity and has_subscription:
    print('Connected') #OUTPUT: Connected


wifi_enabled: bool = True
has_electricity: bool = True
has_subscription: bool = True

requirements: list[bool] = [wifi_enabled, has_electricity, has_subscription]

if all(requirements):
    print('Connected to internet') #OUTPUT: Connected to internet


people_voted: list[int] = [1, 1, 1, 0, 1, 0, 1, 1, 1, 0]
# 1 means True and 0 means False

if all(people_voted):
    print('Everyone voted')
else:
    print('Some people did not vote')
#OUTPUT: Some people did not vote

if not all(people_voted):
    print('Some people did not vote')
else:
    print('Everyone voted')
#OUTPUT: Some people did not vote




