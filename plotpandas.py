#plot pandas data
data=pd.Series(np.random.randn(1000),index=np.arange(1000))
data=data.cumsum()

df5=pd.DataFrame(np.random.randn(1000,4), 
	             index=np.arange(1000),
	             columns=list("ABCD"))
	             