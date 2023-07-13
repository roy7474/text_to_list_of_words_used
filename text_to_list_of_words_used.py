fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    ws = line.split()            # w is the list of splitted words
    for ws_new in ws:
        if ws_new not in lst:   #if the word is not in the list lst
         lst.append(ws_new)      #add the new word to the list lst

        else: 
            continue #otherwise, continue

lst.sort()    
print(lst)