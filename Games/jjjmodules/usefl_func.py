import random
cim=100
km=1000
pinkFloyed=["roger waters","David gilmour","syd barret"]
def get_file_ext(filename):
    return filename[filename.index(".")+1]

def roll_dice(num):
    return random.randint(1,num)