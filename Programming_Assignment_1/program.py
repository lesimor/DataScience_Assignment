# encoding: utf-8
# 우선 값을 읽어서 빈도수를 체크
# 파일을 읽기위해 연다.
import calculate
import sys

# minimal_support(%)
minimal_support_argv = sys.argv[1]

# input file path
input_file = sys.argv[2]

# output file path
output_file = sys.argv[3]

# type casting to float
minimal_support = float(minimal_support_argv)

# file open and read
f = open(input_file)


# table of set
frequency_table = []

# read by line
for line in f:
    # convert each transaction into list
    transaction = map(int, line.split())

    # generate all occurence by list
    for num in transaction:
        if not set([num]) in frequency_table:
            # insert unique value into table of set
            frequency_table.append(set([num]))

# prune by minimal support
print "1 step proceeding..."
result = [s for s in frequency_table if calculate.set_stat(f, s)["support"] >= minimal_support]

# temporary saving space
result_save = []

# join_and_pruning step
step = 2

# join and prune until further progress is no longer proceeding.
while calculate.join_and_prune(f, result, minimal_support, step):
    result = calculate.join_and_prune(f, result, minimal_support, step)
    if not result:
        break
    print str(step)+" step proceeding..."
    step += 1
    result_save = result

# open file for writing
output_file = open(output_file, 'w')

# result set
for s in result_save:
    # generate all subsets
    subsets = calculate.generate_all_subsets(s)

    # generate combination of subsets and calculate support and confidence of them
    for subset in subsets:
        combinations = calculate.generate_item_associative(subset)

        # file write after each combinations
        for item_associative in combinations:
            r = calculate.associative_set_stat(f, item_associative[0], item_associative[1])
            print_line = '%10s\t%10s\t%.1f\t%.1f\n' % ("{"+",".join(map(str, list(item_associative[0]))) + "}",
                                                       "{"+",".join(map(str, list(item_associative[1]))) + "}",
                                                       r["support"],
                                                       r["confidence"])
            output_file.write(print_line)
print "done"

# close file
f.close()
