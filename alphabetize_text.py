import re
import os

'''
Created by: Max Grodzki in Python 3.6.3
    Sorts input in alphabetical order, ignoring case. 
    (current regex splits paragraphs on '.?!' so phrases such as
        ' "Will you keep working on it?" asked Man. '
    are split into "Will you keep working on it?" and "asked Man."
    thus the need for sorting regardless of case.)
'''

f = open("ShortStory.txt", "r")
text= f.read()
f.close()
text = re.split(r' *[\.\?!][\'"\)]*[\n]* *', text)

for i in range(len(text)):
    #Removing partial quotations from the string to help with sorting
    text[i] = re.sub(r"\"", "", text[i])
    #Removing spacer lines from original text
    text[i] = re.sub(r"------------------------------------------------\n\n", "", text[i])
    #Removing dashed lines to help with sorting 
    #   there was one instance where a line started with "--"
    text[i] = re.sub(r"--","", text[i])
    #Removing leading unbalanced parenthesis for sorting
    text[i] = re.sub("^\(", "", text[i])

#Sorts alphabetically, while ignoring case
#   opted for python's built in sort function (Timsort) as on average it is 
#   just as fast as heapsort and mergesort, and faster in the best case.
#text.sort(key = str.casefold)


#The following methods are used for an implementation of Python's built in sort()

#picking an arbitrarily large RUN, determines max size of subarrays/string length
RUN = 1000
# This function sorts array from left index to  
# to right index which is of size atmost RUN 
def insertionSort(arr, left, right):  
   
    for i in range(left + 1, right+1):  
        temp = arr[i]  
        j = i - 1 
        while j >= left and arr[j].lower() > temp.lower() :  
           
            arr[j+1] = arr[j]  
            j -= 1
           
        arr[j+1] = temp  

def merge(arr, l, m, r): 
    # split array into 2 arrays, left and right  
    len1, len2 =  m - l + 1, r - m  
    left, right = [], []  
    for i in range(0, len1):  
        left.append(arr[l + i])  
    for i in range(0, len2):  
        right.append(arr[m + 1 + i])  
    
    i, j, k = 0, 0, l 
    # compare and merge into larger sub array  
    while i < len1 and j < len2:  
       
        if left[i] <= right[j]:  
            arr[k] = left[i]  
            i += 1 
           
        else: 
            arr[k] = right[j]  
            j += 1 
           
        k += 1
       
    # copy remaining elements of left, if any  
    while i < len1:  
       
        arr[k] = left[i]  
        k += 1 
        i += 1
    
    # copy remaining element of right, if any  
    while j < len2:  
        arr[k] = right[j]  
        k += 1
        j += 1

def timSort(arr, n):  
    # Sort individual subarrays of size RUN  
    for i in range(0, n, RUN):  
        insertionSort(arr, i, min((i+999), (n-1)))  
    
    # start merging from size RUN 
    size = RUN 
    while size < n:  
       
        # pick starting point of left sub array. 
        # merge arr[left..left+size-1] and arr[left+size, left+2*size-1]  
        # After every merge increase left by 2*size  
        for left in range(0, n, 2*size):  
           
            # find end point of left sub array  
            # mid+1 is starting point of right sub array  
            mid = left + size - 1 
            right = min((left + 2*size - 1), (n-1))  
    
            # merge sub array arr[left.....mid] & arr[mid+1....right]  
            merge(arr, left, mid, right)  
          
        size = 2*size 

n = len(text)
timSort(text, n)

#If output file already exists, delete it
if os.path.exists("SortedOutput.txt"):
    os.remove("SortedOutput.txt")
#Create output file
f = open("SortedOutput.txt", "w")
for i in text:
    f.write(i + "\n")
