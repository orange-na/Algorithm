

def snake_string(chars: str) ->list[list[str]]:
    results = [[],[],[]]
    results_index = {0,1,2}
    insert_index = 1
    for i, char in enumerate(chars):
        if i % 4 == 1:
            insert_index = 0
        elif i % 2 == 0:
            insert_index = 1
        elif i % 4 == 3:
            insert_index = 2
        results[insert_index].append(char)
        for rest_index in results_index - {insert_index}:
            results[rest_index].append(" ")
    return results



# def snake_string2(chars: str, depth: int) -> list[list[str]]:
#     results = [[] for _ in range(depth)]
#     results_index = { i for i in range(depth)}
#     insert_index = int(depth / 2)

#     def pos(i):
#         return i + 1
    
#     def neg(i):
#         return i - 1
    
#     op = neg

#     for char in chars:
#         results[insert_index].append(char)
#         for rest_index in results_index - {insert_index}:
#             results[rest_index].append(' ')
#         if insert_index <= 0:
#             op = pos
#         if insert_index >= depth - 1:
#             op = neg
#         insert_index = op(insert_index)
#     return results

def snake_string2(chars: str, depth: int) -> list[list[str]]:
    results = [[] for _ in range(depth)]
    results_index = { i for i in range(depth)}
    insert_index = int(depth / 2)

    def pos(i):
        return i + 1
    
    def neg(i):
        return i - 1
    
    op = neg

    for char in chars:
        results[insert_index].append(char)
        for rest_index in results_index - {insert_index}:
            results[rest_index].append(' ')
        if insert_index <= 0:
                op = pos
        if insert_index >= depth - 1:
                op = neg
        insert_index = op(insert_index)
    return results

import string

if __name__ == '__main__':
    alphabet = [s for _ in range(2) for s in string.ascii_lowercase]
    strings = ''.join(alphabet)
    for line in snake_string2(strings, 8):
        print(''.join(line))


