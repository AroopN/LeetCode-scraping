#
# CREATES A NEW CSV FILE WITH NAMES OF PROBLEMS EXTRCTED FROM LINK
# 
data = []
import csv
def extract_name(link):
    name = link.split('/')[-1]
    name = name.replace("-"," ").capitalize()
    # print(name)
    return name
with open("leetcode_data.csv","r") as file:
    data = file.readlines()
    data[0] = data[0][:-1].split(',')
    data[0].insert(1,"NAME")
    for i in range(1,len(data)):
        data[i] = data[i][:-1].split(",")
        # print(i)
        data[i].insert(1,extract_name(data[i][0]))
        # extract_name(data[-1][0])
    print(data[0])
# file.write("LINK,NAME,LIKES,DISLIKES,DIFFICULTY,Accepted,Submitted,Acceptance %\n")

with open("leetcode_data_with_names.csv", "w") as file:
    wr = csv.writer(file, dialect='excel')
    wr.writerows(data)


