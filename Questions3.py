import json
Score=0
List1 = []
print('choose the correct answer')
name1 = input("Enter your name first :")
with open("Questions.json","r") as Q:
    q=json.loads(Q.read())
    for i in q :
        print(i)
        ans = input("choose the correct answer a/b :")
        List1.append(ans)
        if ans ==q[i]:
            print("correct answer,you got 1 point")
            Score=Score+1
        else:
            print("wrong answer")
            Score=Score-1
    inf_ans ={name1:List1}
    print(inf_ans)
    print("Score :",Score)
inf2=json.dumps(inf_ans)
with open("inf.json","w")as Q:
    Q.write(inf2)
