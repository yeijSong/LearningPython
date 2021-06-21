'''
https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=python&oquery=python&tqi=h5zCzsp0Yihsscil%2Fa8ssssstaK-331420


'''

a='https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=python&oquery=python&tqi=h5zCzsp0Yihsscil%2Fa8ssssstaK-331420'
print('a=https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=python&oquery=python&tqi=h5zCzsp0Yihsscil%2Fa8ssssstaK-331420',end='\n\n')

e=a.split('?')
print(e,end='\n\n')
print('URL=',e[0],end='\n\n')

d=e[1]
f=d.split('&')

print('QueryString')
for c in range(0,len(f)):
	print('  ',f[c],end='\n\n')

print('QueryString 개수:',len(f),'개')
'''


b=a.replace('https://search.naver.com/search.naver?','')
print(b)
print(b.split('&'))
c=b.split('&')
print(len(c))
'''
