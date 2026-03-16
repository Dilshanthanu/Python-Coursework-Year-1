def pass_credit():
    while True:
        try:
            p=int(input("Please enter your credits at pass:"))
            if p not in[0,20,40,60,80,100,120]:
                print("Out of range")
                continue
            else:
                return p
        except ValueError:
            print("Integer required")
            continue 
        break
def defer_credit():
    # while True:
    #     try:
    #         d=int(input("Please enter your credits at defer:"))
    #         if d not in[0,20,40,60,80,100,120]:
    #             print("Out of range")
    #             continue
    #         else:
    #             return d
    #     except ValueError:
    #         print("Integer required")
    #         continue
        break
def fail_credit():
    while True:
        try:
            f=int(input("Please enter your credits at fail:"))
            if f not in[0,20,40,60,80,100,120]:
                print("Out of range")
                continue
            else:
                return f
        except ValueError:
            print("Integer required")
            continue
        break
    
def progression_outcome():
    outcome=0
    progress=0
    trailer=0
    retriever=0
    exclude=0
    p_star=""
    t_star=""
    r_star=""
    e_star=""
    while True:
        p = pass_credit()
        d = defer_credit()
        f = fail_credit()
        total = p + d + f
        if total != 120:
            print("Total incorrect")
            continue
        else:
            if p == 120:
                print("Progress")
                outcome=outcome+1
                progress=progress+1
                p_star=p_star+"*"
            elif p == 100:
                print("Progress(module trailer)")
                outcome=outcome+1
                trailer=trailer+1
                t_star=t_star+"*"
            elif p == 80:
                print("Do not progress-module retriever")
                outcome=outcome+1
                retriever=retriever+1
                r_star=r_star+"*"
            elif p == 60:
                print("Do not progress-module retriever")
                outcome=outcome+1
                retriever=retriever+1
                r_star=r_star+"*"
            elif p == 40 and d >= 20:
                print("Do not progress-module retriever")
                outcome=outcome+1
                retriever=retriever+1
                r_star=r_star+"*"
            elif f >= 80:
                print("Exclude")
                outcome=outcome+1
                exclude=exclude+1
                e_star=e_star+"*"
            elif p == 20 and f <= 60:
                print("Do not progress-module retriever")
                outcome=outcome+1
                retriever=retriever+1
                r_star=r_star+"*"
            elif p == 0 and f <= 60:
                print("Do not progress-module retriever")
                outcome=outcome+1
                retriever=retriever+1
                r_star=r_star+"*"
            else:
                print("Invalid")
                continue
        print("Would you like to enter another set of data?")
        response=str.lower(input("Enter 'Y' for yes or 'Q' to quit and view results:"))
        print("")
        if response == "y":
            continue
        elif response == "q":
            print('-'*80)
            print("Histogram")
            print("")
            print("Progress",progress,":",p_star)
            print("Trailer",trailer,":",t_star)
            print("Retriever",retriever,":",r_star)
            print("Exclude",exclude,":",e_star)
            print("")
            print(outcome,"outcomes in total")
            print('-'*80)

            break
        else:
            print("Response is incorrect")
            continue
    


progression_outcome()



