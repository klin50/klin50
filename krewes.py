import random
krewes = open("krewes","r")
data = krewes.read()
krewes_list = data.replace('\n', ' ').split(",")
def randomNum():
    x = random.randint(0,len(krewes_list)-1)
    print(krewes_list[x].replace(" ",""))
randomNum()