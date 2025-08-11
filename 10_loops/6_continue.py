for i in range(1,11):
    if i==5:
        continue
    else:
        print("Hello")

criminals = ["Kona","Sabiha","Oishi","Fahmida","Sayma"]
for criminal in criminals:
    if(criminal=="Fahmida"):
        jail = criminal
        continue
    else:
        print("Release {0}".format(criminal)) 
print("main criminal: {0}".format(jail))