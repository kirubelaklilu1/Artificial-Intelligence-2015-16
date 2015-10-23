import pickle
from pickle import load
words = open("puzzles_wordLadder.txt").read().split()
start =[]
end=[]
i=len(words)
for x in range(0,i):
    if x%2==0:
        start.append(words[x])
    else:
        end.append(words[x])
def bfs():
    tmp =0
    lst1 = load( open( 'save.pkl' , 'rb' ) )
    while tmp<len(start):
        ar = []
        if start[tmp] in lst1:
            ar = lst1[tmp]
            while end[tmp] not in ar:
                findClosest(end[tmp],ar)
                ####
def compTo(s1,s2):
    count =0
    for n in range(0,len(s1)):
        if s1[n] is s2[n]:
            count+=1
    return len(s1)-count
##def findClosest(s, ary):
##    for i in range(len(ary)):
##        if ary[i].compTo(maxnum)>0:
##            maxnum = ary[i]
##            maxIndex = i
##    print (maxIndex)

findClosest("cattle",["bottle", "metric"])
        
    
