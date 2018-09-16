import numpy as np
import pandas as pd
s=pd.Series([1,3,6,np.nan,44,1])
s
dates=pd.date_range('20180901',periods=6)

df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
df1=pd.DataFrame(np.arange(12).reshape((3,4)))

df2=pd.DataFrame({'A':1.,
	'B':pd.Timestamp('20180818'),
	'C':pd.Series(1, index=list(range(4)),dtype='float32'),
	'D':np.array([3]*4,dtype='int32'),
	'E':pd.Categorical(["test","train","test",'train']),
	'F':'foo'})

df4=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['a','b','c','d'])

