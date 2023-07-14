from joblib import load    # We already dump our linear regression model on joblib file, whenever we require we call it .

def prediction():
  print('model can predict in range of 0 - 1000 ml')
  try:
    weight = int(input('Enter The weight in gm/ml to predict:'))
    if not (weight > 0 and weight < 1000):
      return print('Enter the value between 0-1000 ml or gm')
  except:
    return print('You entered invalid input')
  test_model = load('/Users/anchalkumarchaubey/Desktop/LDI Pro system/python_code/linear_model.joblib') # we call regression model from joblib
  sequence = test_model.predict([[weight]])
  hrs = (sequence*5)/60
  return print(hrs[0,0],'hours')

prediction()
prediction()
prediction()
prediction()
prediction()
prediction()
