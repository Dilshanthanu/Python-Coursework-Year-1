def main():
    progress={}
    trailer={}
    retriever={}
    exclude={}
    output_dic={}
    outcome=0
    progression_histogram=[0,0,0,0]
    star=["","","",""]
   
    while True:
        progression=[0,0,0]
        index=0
        total=0
        sid=str(input("Enter Your Student ID:"))
        while index < 3:
            try:
                progression_input=int(input("Enter Pass,Defer,Fail in this oder:"))
                if progression_input not in [0,20,40,60,80,100,120]:
                    print("Out of range")
                    continue
                else:
                    progression[index]=progression_input
                    index=index+1
                    
            except ValueError:
                print("Integer required")
                continue
        for x in progression:
            total=total+x
            
        if total != 120:
            print("Total incorrect")
            continue
        else:
            if progression[0] == 120:
                print("Progress")
                outcome=outcome+1
                progression_histogram[0]=progression_histogram[0]+1
                star[0]=star[0]+"*"
                progress[sid]='-'.join(['progress']+[str(val) for val in progression])
            elif progression[0]== 100:
                print("Progress(module trailer)")
                outcome=outcome+1
                progression_histogram[1]=progression_histogram[1]+1
                star[1]=star[1]+"*"
                trailer[sid]='-'.join(['Progress (module trailer)']+[str(val) for val in progression])
            elif progression[0]== 80:
                print("Do not progress-module retriever")
                outcome=outcome+1
                progression_histogram[2]=progression_histogram[2]+1
                star[2]=star[2]+"*"
                retriever[sid]='-'.join(['Module retriever']+[str(val) for val in progression])
            elif progression[0]== 60:
                print("Do not progress-module retriever")
                outcome=outcome+1
                progression_histogram[2]=progression_histogram[2]+1
                star[2]=star[2]+"*"
                retriever[sid]='-'.join(['Module retriever']+[str(val) for val in progression])
            elif progression[0]== 40 and progression[1] >= 20:
                print("Do not progress-module retriever")
                outcome=outcome+1
                progression_histogram[2]=progression_histogram[2]+1
                star[2]=star[2]+"*"
                retriever[sid]='-'.join(['Module retriever']+[str(val) for val in progression])
            elif progression[2] >= 80:
                print("Exclude")
                outcome=outcome+1
                progression_histogram[3]=progression_histogram[3]+1
                star[3]=star[3]+"*"
                exclude[sid]='-'.join(['Exclude']+[str(val) for val in progression])
            elif progression[0] == 20 and progression[2] <= 60:
                print("Do not progress-module retriever")
                outcome=outcome+1
                progression_histogram[2]=progression_histogram[2]+1
                star[2]=star[2]+"*"
                retriever[sid]='-'.join(['Module retriever']+[str(val) for val in progression])
            elif progression[0] == 0 and progression[2] <= 60:
                print("Do not progress-module retriever")
                outcome=outcome+1
                progression_histogram[2]=progression_histogram[2]+1
                star[2]=star[2]+"*"
                retriever[sid]='-'.join(['Module retriever']+[str(val) for val in progression])
            else:
                print("Invalid")
                continue
            
        while True:
            print("Would you like to enter another set of data?")
            response=str.lower(input("Enter 'Y' for yes or 'Q' to quit and view results:"))
            print("")
            
            if response !="y" and response !="q" :
                print("Response is incorrect")
                continue
            else:
                break
        if response == "y":
            continue    
        else:
            output_dic.update(progress)
            output_dic.update(trailer)
            output_dic.update(retriever)
            output_dic.update(exclude)
            return output_dic,outcome,progression_histogram,star

def output():
    output_dic,outcome,progression_histogram,star=main()
    print("-"*80)
    print("Histogram")
    print('\n',"Progress",progression_histogram[0],":",star[0],'\n',
          "Trailer",progression_histogram[1],":",star[1],'\n',
          "Retriever",progression_histogram[2],":",star[2],'\n',
          "Exclude",progression_histogram[3],":",star[3],'\n',)
    print(outcome,"outcomes in total")
    print("-"*80)
    print("Part 4:")
    for key,value in output_dic.items():
        print(key,":",value,end=' ')
    
                
output()



