#교집합,합집합,차집합

s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

#교집합_2가지 방법(but 동일한 결과)
inter1=s1&s2
inter2=s1.intersection(s2)
inter3=s2.intersection(s1)

print(inter1)
print(inter2)
print(inter3)

print()

#합집합
vUnion1=s1|s2
vUnion2=s1.union(s2)
vUnion3=s2.union(s1)

print(vUnion1)
print(vUnion2)
print(vUnion3)

#차집합
differ1=s1-s2
differ2=s2-s1

differ3=s1.difference(s2)
differ4=s2.difference(s1)

print(differ3)
print(differ4)