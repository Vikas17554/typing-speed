from time import *
import random as r
def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error+=1
        except:
            error+=1
    return error

def speed(time_e,time_u,user_input):
    time_3=time_u-time_e
    time_r=round(time_3,2)
    speed=len(user_input)/time_r
    return round(speed)
    


test=["hello my name is vikas","the sky is blue as ocean","kismat ka khel hai bhai 10 lakh lpa nhi milag","kuch toh log kahenge logo ka kaam hai kehna"]
test1=r.choice(test)
print("_________________Welcome to  Typing Area______________________\n")
time_1=time()
print("\t",test1)
print("_________________[Start Typing now]______________________________\n")
testinput=input("Type: ")
time_2=time()

print("speed",speed(time_1,time_2,testinput),"w/sec")
print("Error",mistake(test1,testinput) )