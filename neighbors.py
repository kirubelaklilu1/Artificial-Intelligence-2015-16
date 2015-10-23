from sys import argv
from pprint import pprint
import pickle
from pickle import load
words = open("words.txt").read().split()
#givenWord = input("Enter a word:")
global lists
lists = {}
def findNeighbors(x):
   list =[]
   count = 0
   if x in words:
      for w in words:
         count = 0
         for n in range(0,6):
            if w[n] is x[n]:
               count+=1               
         if count == 5:
            list.append(w)
            
      print("The neighbors of %s are:" %x)
      for l in list:
         print (l)         
   else:
      print ("The word is not in the .txt file")
      
def buildStructure():
   for w in words:
      neighbors=[]
      for v in words:
         if isNbr(w,v):
            neighbors.append(v)
      lists[w] = neighbors  
   pprint(lists)
   pickle.dump(lists, open("save.pkl", "wb"))
def isNbr(w1,w2):
   same =0
   dif =0
   index =0
   if w1 is w2:
      return False
   while dif <=1:
      for c in w1:
         if c != w2[index]:
            dif +=1
            index+=1
         else :
            same+=1
            index+=1
            if same ==5:
               return True
   return False
    
##def findMax(lists):
##     maxNum = 0
##     tmp = 0
##     x=0
##     lst =[None]*maxNum+1
##     for k in lists:
##        tmp=len(lists[k])
##        if tmp > maxNum:
##           maxNum = tmp
##     print ("The Max Number of Neighbors is %s" %maxNum)
##   
##     for key in lists:
##        if len(lists[key]) == maxNum:
##          print ("Word: %s , Neighbors: %s" % (key, lists[key]))
##     while x <= maxNum:
##        for key in lists:
##           if len(lists[key]) == x:
##               lst[x]+=1
##     print (lst)
##        
def findFreq():
   lst1 = load( open( 'save.pkl' , 'rb' ) )
   freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
   l = list("")

   for w in lst1:
      x = len(lst1[w])
      if x == 14:
        l.append(w)
        l.append(lst1[w])
      y = freq[x]
      y += 1
      freq[x] = y
   print(freq)
   print("max degree: 14")
   print(l)




       
    
   

#buildStructure()
findFreq()
#findMax(lists)     
#findNeighbors(givenWord)
#print words
# Part One Ends Here
#Build a data structure to store all neighbor lists of all words
