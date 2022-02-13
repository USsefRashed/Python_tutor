#workers_file=open("Workers.txt","r")
                                #r read oly
                                #r+ read & write
                                #a append add from last & cannot modify the above data if exist
                                #w write only
# print(workers_file.readable())
# #return boolean if i can read
# print(workers_file.readlines())
# #take all content of textfile then 
# # put into List 

# print(workers_file.readline())
# print(workers_file.readline())
# #read line in file and move the cursur to the next line 
# #to be ready to read if i use the function again

##diplay file's lines with for loop
# for worker in workers_file.readlines():
#     print(worker+" hahahahahaaaay")#Ican modify on it

#print(workers_file.readlines()[2])
#Here i specify which line
# I want to read on the file


#workers_file.close()
#BEST PRACTICE : write this line while open the file
# to avoid forgeting close the file