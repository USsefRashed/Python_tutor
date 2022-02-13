'''
                    r   r+  w   w+  a   a+
------------------|-------------------------
read              | +   +       +       +
write             |     +   +   +   +   +
create            |         +   +   +   +
truncate          |         +   +
position at star  | +   +   +   +
position at end   |                 +   +

template explain if you want to purpose of rigth cloumns 
'''
workers_file=open("Workers.txt","a")
                                #r read oly
                                #r+ read & write
                                #a append add from last & cannot modify the above data if exist
                                #w write only & all prev data will earase
workers_file.write("\nhuba luba")
workers_file=open("Workers.txt","w")
workers_file.write("I am write command i erased the data")
workers_file.close()