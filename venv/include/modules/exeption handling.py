## exeption handling -> 10/0 ,a=5 , a.lower()
## try ,except ,else ,finaly

try:
    a = 5
    a.Lower()
except AttributeError:
    print("int object does not have lower() method")
else:
    print("No error today")
