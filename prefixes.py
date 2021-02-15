
l1 = ['florence','flower','flight']
l2 = ['appple','appp','apppertif','appp']
l3 = ['','hello']
l4 = ['la','ag']
l5 = ['flo','fle']

def get_shortest_word(word_list):
    l = sorted(word_list, key=len)
    return l[0]


def list_includes_prefix(input_list, prefix):
    includes_prefix = True

    prefix_length = len(prefix)

    for word in input_list:
        if word[:prefix_length] != prefix:
            includes_prefix = False

    return includes_prefix


def find_common_prefix(word_list):

    shortest_word = get_shortest_word(word_list)

    if shortest_word == '':
        return ['']

    solution_not_found = True
    while solution_not_found:
        if list_includes_prefix(word_list, shortest_word):
            solution_not_found = False
            return [shortest_word]
        else:
            shortest_word = shortest_word[:-1]




print(find_common_prefix(l1))
print(find_common_prefix(l2))
print(find_common_prefix(l3))
print(find_common_prefix(l4))
print(find_common_prefix(l5))

