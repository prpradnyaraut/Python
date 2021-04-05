from sklearn import tree
#Rough 1 #Smooth 0 #Tennis 1 #Cricket 2

def MarvellousML(weight,surface):
	#step 1 & 2 : Input Data set
	Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],
		[43,1],[110,0],[35,1],[95,0]]

	Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]
	
	#step 3 : fix Algo
	dobj = tree.DecisionTreeClassifier()
	
	#step 4 : to train
	dobj.fit(Features,Labels) # fit : tarin to data
	
	#step 5 : to predict the data
	result = dobj.predict([[weight,surface]])
	if result == 1:
		print("Your object is looks like Tennis ball")
	else:
		print("Your object is looks like Cricket ball")

def main():
	print("----------------Supervised Machine Lerning------------------")
	print("Enter weight of object :")
	weight = int(input())
	
	print("Enter surface type of object :")
	surface = input()
	
	if surface.lower() == "rough":
		surface = 1
	elif surface.lower() == "smooth":
		surface = 0
	else:
		print("Invalid data")
		return
	
	MarvellousML(weight,surface)
	
if __name__ == "__main__":
	main()
