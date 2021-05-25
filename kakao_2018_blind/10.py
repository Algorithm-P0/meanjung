"""
# 시간초과
from collections import deque
def solution(words):
    N = len(words)
    ans = 0
    for i in range(N):
        word = words[i]
        idx = 0
        lst = [words[j] for j in range(N) if j != i]
        lst = deque(lst)
        while True:
            if idx==len(word):
                ans += len(word)
                break
            newlst = deque()
            while lst:
                w = lst.popleft()
                if idx<len(w) and word[idx]==w[idx]:
                    newlst.append(w)
                else:
                    continue
            lst = newlst
            if len(newlst)==0:
                ans += (idx+1)
                break
            idx+=1
    return ans
"""
def solution(words):
    Trie = {}
    for word in words:
        cur_Trie = Trie
        for w in word:
            cur_Trie.setdefault(w, [0, {}])
            cur_Trie[w][0] += 1
            cur_Trie = cur_Trie[w][1]
    result = 0
    for word in words:
        cur_Trie = Trie
        for i in range(len(word)):
            if cur_Trie[word[i]][0] == 1:
                break
            cur_Trie = cur_Trie[word[i]][1]
        result += (i+1)
    return result

solution(["go","gone","guild"])