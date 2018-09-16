height=1.75
weight=80.5
bmi=float(weight/(height*height))
print(bmi)
if bmi<18.5:
	print('too slim')
elif bmi<25:
	print('normal')
elif bmi<28:
	print('overweight')
elif bmi<32:
	print('obessity')
else:
	print('sever obessity')