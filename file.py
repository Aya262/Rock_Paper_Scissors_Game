import random

def rand_fun():
    rules={
        '1':'rock',
        '2':'paper',
        '3':'scissors'
    }
    number=random.randint(1,3)
    return rules[str(number)]

def vaild_fun():
    rules={
        'r':'rock',
        'p':'paper',
        's':'scissors'
    }
    print("Enter a Character for your Choice : R for Rock , P for Paper , S for Scissors")
    answer=input().strip().lower()
    while (answer!='r' and answer !='p' and answer !='s'):
        try:
            raise ValueError ("Please , Enter a Vaild Choice : R for Rock , P for paper , S for Scissors")
        except ValueError as err:
            print("Oh it's wrong {} ".format(err))
            answer=input().strip().lower()
    return rules[answer]

def result_fun(sys,user):
    killers={
        'rock':'scissors',
        'paper':'rock',
        'scissors':'paper'
    }
    if sys == user:
        return 'Tie'
    elif killers[sys]!=user:
        return "User"
    else :
        return "Computer"

if __name__=='__main__':
    print("Welcome to Rock Paper Scissors Game ")
    print("What's Your Name ? : ")
    answer=input()
    User_score=0
    system_score=0
    for _ in range(3):
        user=vaild_fun()
        system=rand_fun()
        print("{} Choice is {}".format(answer,user))
        print("Computer Choice is {}".format(system))
        winer=result_fun(system,user)
        print("Round Winer is {}".format(winer))
        if winer== 'Tie':
            pass
        elif winer=="User":
            User_score+=1
        else :
            system_score+=1
    print("Game Over !")
    print("{} Score is {}".format(answer,User_score))
    print("Computer Score is {}".format(system_score))