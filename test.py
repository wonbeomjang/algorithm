import re


def solution(words, queries):
    query_slice = []

    for query in queries:
        index = 0
        i = 0
        slices = []
        while i < len(query):
            print(i)
            if query[i] == "?":
                slices += [(index, i)]
                while i < len(query) and query[i] == "?":
                    i += 1
            else:
                i += 1
        query_slice += [slices]

    print(query_slice)

    return 0

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))