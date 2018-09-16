def calc(*numbers):
	sum=0
	for n in numbers:
		sum=sum+n*n
	return sum

#def person(name, age, **kw):
#	print('name:',name,'age:',age,'other:',kw)

def person(name, age, **kw):
    if 'city' in kw:
      pass
    if 'job' in kw:
      pass
    print('name:',name,'age:',age,'other:',kw)
