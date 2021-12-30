

def flight(hieght):
    if hieght <= 0 :
        print("invalid hieght of ", hieght)
        return 0
    else:
        print("hieght of", hieght)
        if hieght>1:

        # recyrsive case
            if hieght%2 ==0:
                return 1+flight(hieght/2)
            
            elif hieght %2 != 0:
                return 1+flight(hieght*3+1)
        else:
            return 0

def main():
    print("welcome to hailstone generator")
    msg  = "please eneter a hieght to start at: "
    start_hieght = int(input(msg))

    steps = flight(start_hieght)

    print(f"it took {steps} steps to hit the ground")

main()


