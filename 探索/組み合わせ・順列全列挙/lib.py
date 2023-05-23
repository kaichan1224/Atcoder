from ast import Pass
import itertools
# 順列
#(1,2,3),(1,3,2),(2,1,3),(2,3,1),...,(3,2,1)
for seq in itertools.permutations(range(1,4)):
    pass
# 重複なしの組み合わせ
# (1,2,3),(1,2,4),...,(7,8,9)
for seq in itertools.combinations(range(1,10),3):
    pass
# 重複ありの組み合わせ
#(1,1,1),(1,1,2),...,(9,9,9)
for seq in itertools.combinations_with_replacement(range(1,10),3):
    pass
# 直積
#(1,1),(1,2),(1,3),(2,1),(2,2),...,(3,3)
for seq in itertools.product(range(1,4),range(1,4)):
    pass





