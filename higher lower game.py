import random as rd

def main():
    print("Choose difficulty:")
    print("1.Easy (0-100)(10 tries)")
    print("2.Hard (0-1000)(15 tries)")

    diff=int(input("Enter difficulty: "))

    if diff==1:
        print("Easy difficulty choosen")
        x=rd.randint(0,100)
        for i in range(10):
            ask=int(input("Enter your guess between 0 and 100: "))
            if x==ask:
                print("Correct answer, you won")
                break
            elif x>ask:
                print("Try Higher")
            else:
                print("Try Lower")


    elif diff==2:
        print("Hard difficulty choosen")
        x=rd.randint(0,1000)
        for i in range(15):
            ask=int(input("Enter your guess between 0 and 1000: "))
            if x==ask:
                print("Correct answer, you won")
                break
            elif x>ask:
                print("Try Higher")
            else:
                print("Try Lower")

    
        

main()
again=int(input("Do you want to play again?(1=yes, 2=no)"))
if again==1:
    main()
else:
    exit()


