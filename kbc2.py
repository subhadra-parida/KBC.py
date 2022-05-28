que_list=["How many are girls in Sarjapur Campus?","What is Capital of India?","Name of Pink city name?","Who is  Dico in Sarjapur Campus?"]
opt_list=[[123,134,568,100],["Delhi","Bangalore","Nanital","Odisa"],["Aagra","Chamoli","Panjab","Jaypur"],["Himani","Kajal","Harman","Gudiya"]]
ans_list=[2,1,4,1]
cash=0
def option(index):
    j=0
    while j<len(opt_list[index]):
        print(j+1,opt_list[index][j])
        j=j+1
    user_ans = int(input('.....'))
    if user_ans==ans_list[index]:
        return True
    else:
        return False
def que():
    global cash
    index=0
    while index<len(que_list):
        print("Q.",index+1,que_list[index],"?")
        result=option(index)
        if result==True:
            cash+=10000
            print("Congratulations \n ","u won - ",cash)
        else:
            print("you Losse ! \n","u won - ",cash)
            break 
        index+=1
que()
