import pickle
with open('ML CODE/model_pickle', 'rb') as mod:
	model = pickle.load(mod)
#print(model.predict(cv.transform('hello'))[0])
statement = input("Enter your statement and I will predict whether it is true or false : ")
user_input = pd.Series(statement)
user_test=cv.transform(user_input)
print("The prediction is",model.predict(user_test)[0])