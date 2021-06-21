#리스트에 포함된 요소x의 개수 세기(count)

a=[1,2,3,1]
print(a.count(1))

'''
#리스트 확장(extend)
extend(x)에서 x에는 리스트만 올 수 있으며
원래의 a리스트에 x리스트를 더한다.
'''

b=[1,2,3]
b.extend([4,5])
print(b)

#b.extend([4,5])는 a+=[4,5]와 동일