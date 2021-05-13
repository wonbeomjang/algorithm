from itertools import combinations

def solution(gems):
    kinds_of_gems = list(set(gems))
    num_gems = len(kinds_of_gems)
    gem_count = {}
    
    start = 0
    end = 0
    
    section = [-1, 100001]
    
    while start < len(gems) and end < len(gems):
        if len(gem_count) < num_gems:
            end += 1
            if not end < len(gems):
                break
                
            print(start < len(gems) and end < len(gems))
            print(end)
            if gem_count.get(gems[end]) is None:
                gem_count[gems[end]] = 1
            else:
                gem_count[gems[end]] += 1
            
        else:
            if section[1] - section[0] > end - start:
                section[0] = start
                section[1] = end
            
            if gem_count[gems[start]] > 1:
                gem_count[gems[start]] -= 1
            else:
                del gem_count[gems[start]]
            
            start += 1
            
    return section

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	))