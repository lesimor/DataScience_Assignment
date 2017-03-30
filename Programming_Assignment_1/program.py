# encoding: utf-8
# 우선 값을 읽어서 빈도수를 체크
# 파일을 읽기위해 연다.
import calculate
from set import Set

f = open('./small_input.txt')
f.readline()

# set의 집합
frequency_table = []

# 입력받은 support
minimal_support = 3

for line in f:
    # 모든 경우의 수를 산출
    transaction = map(int, line.split())
    for num in transaction:
        if not set([num]) in frequency_table:
            frequency_table.append(set([num]))

# minimal support에 미치지 못하는 값은 삭제

l_1 = [s for s in frequency_table if calculate.set_stat(f, s)["frequency"] >= minimal_support]
# print "l_1"
# print l_1
# # join수행
# l_2 = []
# for index, s in enumerate(l_1):
#     for x in range(index + 1, len(l_1)):
#         union_set = s.union(l_1[x])
#         if len(union_set) == 2 and calculate.get_frequency(f, union_set) >= minimal_support:
#             l_2.append(union_set)
# print "l_2"
# print l_2
result = l_1
result_save = []
step = 2
while calculate.join_and_prune(f, result, minimal_support, step):
    result = calculate.join_and_prune(f, result, minimal_support, step)
    if not result:
        break
    print step
    step += 1
    result_save = result

print result_save

# 검증
output_file = open("output.txt", 'w')
for s in result_save:
    st = calculate.set_stat(f, s)["frequency"]
    output_file.write(str(st))

print calculate.get_confidence(f, set([1, 2]), set([11]))

f.close()

# L2 generate
#
