# encoding: utf-8
# 우선 값을 읽어서 빈도수를 체크
# 파일을 읽기위해 연다.
import calculate

f = open('./input.txt')
f.readline()

# set의 집합
frequency_table = []

# 입력받은 support
minimal_support = 50

for line in f:
    # 모든 경우의 수를 산출
    transaction = map(int, line.split())
    for num in transaction:
        if not set([num]) in frequency_table:
            frequency_table.append(set([num]))

# minimal support에 미치지 못하는 값은 삭제

l_1 = [s for s in frequency_table if calculate.set_stat(f, s)["frequency"] >= minimal_support]
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
    subsets = calculate.generate_all_subsets(s)
    for subset in subsets:
        combinations = calculate.generate_item_associative(subset)
        for item_associative in combinations:
            r = calculate.associative_set_stat(f, item_associative[0], item_associative[1])
            print_line = '{%s}\t{%s}\t%.1f\t%.1f\n' % (",".join(map(str, list(item_associative[0]))),
                                                       ",".join(map(str, list(item_associative[1]))),
                                                       r["support"] * 100,
                                                       r["confidence"] * 100)
            output_file.write(print_line)

print calculate.associative_set_stat(f, set([1, 2]), set([11]))

print calculate.generate_item_associative(set([1, 2, 3, 4]))

print calculate.generate_all_subsets(set([1, 2, 3, 4, 5]))

f.close()

# L2 generate
#
