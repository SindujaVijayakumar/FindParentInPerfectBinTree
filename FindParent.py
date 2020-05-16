
import cProfile
def solution(h, q):
    root = (1 << h) -1
    leftmost_leaf = 1
    rightmost_leaf = (1 << h) - h
    result = [None] * len(q)
    left = [None] * h
    right = [None] * h
    left[0] = leftmost_leaf
    right[0] = rightmost_leaf
    right[h - 1] = left[h - 1] = root

    for i in range(h - 2, 0, -1):
        left[i] = ((left[i + 1] + 1) >> 1) - 1
        right[i] = right[i + 1] - 1

    for i, item in enumerate(q):
        if item >= root:
            result[i] = -1
            continue

        if item == leftmost_leaf:
            if h == 1:
                result[i] = -1
            else:
                result[i] = 3
            continue

        if item == rightmost_leaf:
            result[i] =  rightmost_leaf - h
            continue

        parent = root
        for height in range(h-1, 0, -1):
            if item == left[height]:
                result[i] = left[height + 1]
                break
            elif item == right[height]:
                result[i] = right[height + 1]
                break
            else:
                left_child = parent - 2**height
                right_child = parent - 1
                if item in [left_child, right_child]:
                    result[i] = parent
                    break
                elif item < left_child:
                    parent = left_child
                else:
                    parent = right_child

    return result

if __name__ == "__main__":
    h = 5
    # q = [19, 14]
    q = [15]
    # q = [1 ]
    # q = [31]
    # q = [27]
    # q = [28]

    print(solution(h, q))
