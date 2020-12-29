# def isIsomorphic(s: str, t: str) -> bool:
# if len(s) != len(t):
#     return False
#
# s_map = dict()
# t_map = dict()
#
# for i in range(0, len(s)):
#     if not s[i] in s_map and not t[i] in t_map:
#         s_map[s[i]] = [i]
#         t_map[t[i]] = [i]
#
#     else:
#         if s[i] not in s_map or t[i] not in t_map:
#             return False
#
#         if s_map[s[i]] == t_map[t[i]]:
#             s_map[s[i]].append(i)
#             t_map[t[i]].append(i)
#         else:
#             return False
#
# return True
# def isIsomorphic(s: str, t: str) -> bool:
#     if (s == None and t == None) or (s == "" and t == "") or (s == t):
#         return True
#
#     if len(s) != len(t):
#         return False
#
#     return [s.find(i) for i in s] == [t.find(i) for i in t]

def isIsomorphic(self, s: str, t: str) -> bool:
    d = {}
    for ix, ch in enumerate(s):
        if ch not in d:
            if t[ix] in d.values():
                return False
            d[ch] = t[ix]
        else:
            if d[ch] != t[ix]:
                return False
    return True


print(isIsomorphic('foo', 'baa'))
