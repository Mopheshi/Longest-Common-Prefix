list = ["planet", "player", "pluto"]


def longestCommonPrefix(lst):
    global length
    l = len(lst)
    for i in range(1, len(lst)):
        length = min(l, len(lst[i]))
        while (length > 0 and lst[0][0:length] != lst[i][0:length]):
            length = length - 1
            if length == 0:
                return 0
    return lst[0][0:length]


if __name__ == "__main__":
    print(longestCommonPrefix(list))
