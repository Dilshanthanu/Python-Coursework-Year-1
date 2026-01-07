def main():
    progress=[]
    trailer=[]
    retriever=[]
    exclude=[]
    outcome=0
    progression_histogram=[0,0,0,0]
    star=["","","",""]
    while True:
        progression=[0,0,0]
        index=0
        total=0
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
                progress.append(progression)
            elif progression[0]== 100:
                print("Progress(module trailer)")
                outcome=outcome+1
                progression_histogram[1]=progression_histogram[1]+1
                star[1]=star[1]+"*"
                trailer.append(progression)
            elif progression[0]== 80:
                print("Do not progress-module retriever")
                outcome=outcome+1
                progression_histogram[2]=progression_histogram[2]+1
                star[2]=star[2]+"*"
                retriever.append(progression)
            elif progression[0]== 60:
                print("Do not progress-module retriever")
                outcome=outcome+1
                progression_histogram[2]=progression_histogram[2]+1
                star[2]=star[2]+"*"
                retriever.append(progression)
            elif progression[0]== 40 and progression[1] >= 20:
                print("Do not progress-module retriever")
                outcome=outcome+1
                progression_histogram[2]=progression_histogram[2]+1
                star[2]=star[2]+"*"
                retriever.append(progression)
            elif progression[2] >= 80:
                print("Exclude")
                outcome=outcome+1
                progression_histogram[3]=progression_histogram[3]+1
                star[3]=star[3]+"*"
                exclude.append(progression)
            elif progression[0] == 20 and progression[2] <= 60:
                print("Do not progress-module retriever")
                outcome=outcome+1
                progression_histogram[2]=progression_histogram[2]+1
                star[2]=star[2]+"*"
                retriever.append(progression)
            elif progression[0] == 0 and progression[2] <= 60:
                print("Do not progress-module retriever")
                outcome=outcome+1
                progression_histogram[2]=progression_histogram[2]+1
                star[2]=star[2]+"*"
                retriever.append(progression)
            else:
                print("Invalid")
                continue
            while True:
       
                print("Would you like to enter another set of data?")
                response=str.lower(input("Enter 'Y' for yes or 'Q' to quit and view results:"))
                print("")
                if response != "y" and response != "q":
                    print("Response is incorrect")
                    continue
                else:
                    break
            if response == "y":
                continue
            else:
                return progress,retriever,trailer,exclude,outcome,progression_histogram,star
                
def output():
    progress,retriever,trailer,exclude,outcome,progression_histogram,star=main()
    print('-'*80)
    print("Histogram")
    print('\n',"Progress",progression_histogram[0],":",star[0],'\n',
          "Trailer",progression_histogram[1],":",star[1],'\n',
          "Retriever",progression_histogram[2],":",star[2],'\n',
          "Exclude",progression_histogram[3],":",star[3],'\n',)
    print(outcome,"outcomes in total")
    print('-'*80)
    print("Part 2:")
    part2_index1=0
    part2_index2=0
    for i in range(progression_histogram[0]):
        print("Progress-",progress[part2_index1][part2_index2],',',progress[part2_index1][part2_index2+1],',',progress[part2_index1][part2_index2+2])
        part2_index1=part2_index1+1
        part2_index1=0
        part2_index2=0
    for i in range(progression_histogram[1]):
        print("Progress (module trailer)-",trailer[part2_index1][part2_index2],',',trailer[part2_index1][part2_index2+1],',',trailer[part2_index1][part2_index2+2])
        part2_index1=part2_index1+1
        part2_index1=0
        part2_index2=0
    for i in range(progression_histogram[2]):
        print("Module retriever-",retriever[part2_index1][part2_index2],',',retriever[part2_index1][part2_index2+1],',',retriever[part2_index1][part2_index2+2])
        part2_index1=part2_index1+1
        part2_index1=0
        part2_index2=0
    for i in range(progression_histogram[3]):
        print("Exclude -",exclude[part2_index1][part2_index2],',',exclude[part2_index1][part2_index2+1],',',exclude[part2_index1][part2_index2+2])
        part2_index1=part2_index1+1
        
                    
output()



