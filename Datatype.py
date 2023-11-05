# x = "hsfhsbfjsj"
# print(type(x))
# print(x)
#
# v =int(20.3)
# print(type(v))
# print(v)
#
# a = ["s", "d", "r"]
# print(type(a))
# print(a)
#
# b = ('f', 'p')
# print(type(b))
# print(b)
#
# g = range(-56)
# print(g)
# print(type(g))
#
# l = {'name' : 'Hridoy'}
# print(type(l))
# print(l)

# Name = 'Bodor uddin ahmad ridoy'
# print('My name is' + ' ' + Name)
#
# #boolean type
# a = 10
# b = 11
#
# print(b >= a)
#
# c = 10
# C = 10
# print(C == c)

#string formating
#
# a = 35
# b = 90
# c = 9
# d = float(b)
# print(f"{a+c+d}")

# def find_clumps(string, k, L, t):
#   clumps = []
#   for i in range(len(string) - L + 1):
#     window = string[i:i + L]
#     for j in range(len(window) - k + 1):
#       kmer = window[j:j + k]
#       if window.count(kmer) >= t and kmer not in clumps:
#         clumps.append(kmer)
#   return clumps
#
#
# sequence = input("Enter the DNA sequence: ")
# k, L, t = map(int, input().split())
#
# clumps = find_clumps(sequence, k, L, t)
# print(*find_clumps(sequence,k,L,t))

# def clump_finding(txt, k, L, t):
#     kmer_counts = {}
#     result = set()
#
#     for i in range(len(txt) - L + 1):
#         sub_txt = txt[i:i + L]
#
#         for j in range(len(sub_txt) - k + 1):
#             kmer = sub_txt[j:j + k]
#
#             if kmer in kmer_counts:
#                 kmer_counts[kmer].append(i + j)
#             else:
#                 kmer_counts[kmer] = [i + j]
#
#     for kmer, positions in kmer_counts.items():
#         if len(set(positions)) >= t:
#             result.add(kmer)
#
#     return result
#
# input_str = input()
# k, L, t = map(int, input().split())
# print(*clump_finding(input_str, k, L, t))

# def find_clumps(string, k, L, t):
#     clumps = []
#     for i in range(len(string) - L + 1):
#         window = string[i:i + L]
#         for j in range(len(window) - k + 1):
#             kmer = window[j:j + k]
#             if window.count(kmer) >= t and kmer not in clumps:
#                 clumps.append(kmer)
#     return " ".join(clumps)
#
#
# sequence = input("DNA sequence: ")
# k, L, t = map(int,input().split())
# print(*find_clumps(sequence,k,L,t))