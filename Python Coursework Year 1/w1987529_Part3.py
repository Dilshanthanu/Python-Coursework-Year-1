def main():
    progress=[]
    trailer=[]
    retriever=[]
    exclude=[]
    outcome=0
    progression_histogram=[0,0,0,0]
    star=["","","",""]
    while True:
        progression_int=[]
        progression_str=[]
        index=0
        total=0
        while index < 3:
            try:
                progression_input=int(input("Enter Pass,Defer,Fail in this oder:"))
                if progression_input not in [0,20,40,60,80,100,120]:
                    print("Out of range")
                    continue
                else:
                    progression_int.append(progression_input)
                    progression_str.append(str(progression_input))
                    index=index+1
                    
            except ValueError:
                print("Integer required")
                continue
        for x in progression_int:
            total=total+x
            
        if total != 120:
            print("Total incorrect")
            continue
        else:
            if progression_int[0] == 120:
                print("Progress")
                outcome=outcome+1
                progression_histogram[0]=progression_histogram[0]+1
                star[0]=star[0]+"*"
                progress.append(progression_str)
            elif progression_int[0]== 100:
                print("Progress(module trailer)")
                outcome=outcome+1
                progression_histogram[1]=progression_histogram[1]+1
                star[1]=star[1]+"*"
                trailer.append(progression_str)
            elif progression_int[0]== 80:
                print("Do not progress-module retriever")
                outcome=outcome+1
                progression_histogram[2]=progression_histogram[2]+1
                star[2]=star[2]+"*"
                retriever.append(progression_str)
            elif progression_int[0]== 60:
                print("Do not progress-module retriever")
                outcome=outcome+1
                progression_histogram[2]=progression_histogram[2]+1
                star[2]=star[2]+"*"
                retriever.append(progression_str)
            elif progression_int[0]== 40 and progression_int[1] >= 20:
                print("Do not progress-module retriever")
                outcome=outcome+1
                progression_histogram[2]=progression_histogram[2]+1
                star[2]=star[2]+"*"
                retriever.append(progression_str)
            elif progression_int[2] >= 80:
                print("Exclude")
                outcome=outcome+1
                progression_histogram[3]=progression_histogram[3]+1
                star[3]=star[3]+"*"
                exclude.append(progression_str)
            elif progression_int[0] == 20 and progression_int[2] <= 60:
                print("Do not progress-module retriever")
                outcome=outcome+1
                progression_histogram[2]=progression_histogram[2]+1
                star[2]=star[2]+"*"
                retriever.append(progression_str)
            elif progression_int[0] == 0 and progression_int[2] <= 60:
                print("Do not progress-module retriever")
                outcome=outcome+1
                progression_histogram[2]=progression_histogram[2]+1
                star[2]=star[2]+"*"
                retriever.append(progression_str)
            else:
                print("Invalid")
                continue
        while True:
                print("Would you like to enter another set of data?")
                response=str.lower(input("Enter 'Y' for yes or 'Q' to quit and view results:"))
                print("")
                if response !="y" and response !="q":
                    print("Response is incorrect")
                    continue
                else:
                    break
        if response =="y":
            continue
        else:
            return progress,retriever,trailer,exclude,outcome,progression_histogram,star
def output():
    progress,retriever,trailer,exclude,outcome,progression_histogram,star=main()
    print("Histogram")
    print('\n',"Progress",progression_histogram[0],":",star[0],'\n',
          "Trailer",progression_histogram[1],":",star[1],'\n',
          "Retriever",progression_histogram[2],":",star[2],'\n',
          "Exclude",progression_histogram[3],":",star[3],'\n',)
    print(outcome,"outcomes in total")
                
    part3_textfile=open("Part_3.txt","x")
    part3_textfile=open("part_3.txt","w")
    part3_textfile.write("Part 3:.\n")
                
    part2_index1=0
    part2_index2=0
    for i in range(progression_histogram[0]):
        part3_textfile.write("Progress-")
        part3_textfile.write(progress[part2_index1][part2_index2])
        part3_textfile.write(',')
        part3_textfile.write(progress[part2_index1][part2_index2+1])
        part3_textfile.write(',')
        part3_textfile.write(progress[part2_index1][part2_index2+2]+'\n')
        part2_index1=part2_index1+1
    part2_index1=0
    part2_index2=0
    for i in range(progression_histogram[1]):
        part3_textfile.write("Progress (module trailer)-")
        part3_textfile.write(trailer[part2_index1][part2_index2])
        part3_textfile.write(',')
        part3_textfile.write(trailer[part2_index1][part2_index2+1])
        part3_textfile.write(',')
        part3_textfile.write(trailer[part2_index1][part2_index2+2]+'\n')
        part2_index1=part2_index1+1
    part2_index1=0
    part2_index2=0
    for i in range(progression_histogram[2]):
        part3_textfile.write("Module retriever-")
        part3_textfile.write(retriever[part2_index1][part2_index2])
        part3_textfile.write(',')
        part3_textfile.write(retriever[part2_index1][part2_index2+1])
        part3_textfile.write(',')
        part3_textfile.write(retriever[part2_index1][part2_index2+2]+'\n')
        part2_index1=part2_index1+1
    part2_index1=0
    part2_index2=0
    for i in range(progression_histogram[3]):
        part3_textfile.write("Exclude -")
        part3_textfile.write(exclude[part2_index1][part2_index2])
        part3_textfile.write(',')
        part3_textfile.write(exclude[part2_index1][part2_index2+1])
        part3_textfile.write(',')
        part3_textfile.write(exclude[part2_index1][part2_index2+2]+'\n')
        part2_index1=part2_index1+1
        part3_textfile.close()
    part3_textfile=open("part_3.txt","r")
    print(part3_textfile.read(),'\n')
    part3_textfile.close()
    import os
    os.remove("part_3.txt")
                

output()



