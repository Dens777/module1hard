grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students={'Johnny','Bilbo','Steve','Khendrik','Aaron'}
students1=tuple(sorted(students))
grades1=(grades)
def average(*args): return([sum(x) / len(x) for x in args])
answer_dict =dict(zip(students1,(average(*grades1))))
print(answer_dict)

