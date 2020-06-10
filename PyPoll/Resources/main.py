import os
import csv
import numpy as np

csvpath = os.path.join('Resources', 'election_data.csv')


candidates = []
candidate_list = []
votes = []



with open("C:\\Users\\winyi\\OneDrive\\Desktop\\LearnPython\\gt-inc-data-pt-05-2020-u-c\\02-Homework\\03-Python\\Instructions\\PyPoll\\Resources\\election_data.csv") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    data = list(csvreader)
    total_votes = len(data)
    vote_count = []
    percentage = []
    z = []
    
    
    for row in data:
        candidate_list.append(row[2])
        
    unique_list = list(set(candidate_list))
        
    for candidate in unique_list:
        candidate_count = sum(x.count(candidate) for x in data)
        candidate_percent = round(candidate_count/total_votes*100,3)
        vote_count.append(candidate_count)
        percentage.append(candidate_percent)
        
    final = dict(zip(unique_list,zip(percentage,vote_count)))
    
    winner = max(final, key=final.get)
   
    output1 = (
            f"Election Results\n"
            f"--------------------------\n"
            f"Total Votes : {total_votes}\n"
            f"---------------------------\n"
            
    )     


    output3 = (

                                 
            f"Winner : {winner}\n"
            f"-----------------------------"



    ) 
    



    output2 = ""
    for x in final:
        output2 = output2 + f"{x} {final[x][0]} {final[x][1]}\n"
    print(output2)
        
print(output1 + output2 + output3)    

output_path = os.path.join('Resources', 'results.txt')

with open("C:\\Users\\winyi\\OneDrive\\Desktop\\LearnPython\\python_challenge\\PyPoll\\Resources\\results.txt", 'w') as newtextfile:
    csvwriter = csv.writer(newtextfile)
    newtextfile.write(output1 + output2 + output3)
    

