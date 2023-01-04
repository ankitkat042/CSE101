def word_count(fname):
    
    with open(fname) as f:           
            words=f.read().split()
            myDict = {}
            
            for key in words:
                myDict[key] = words.count(key)
    
    return myDict

def word_unique(fname):
    
    with open(fname) as f:
            words=f.read().split()
            
            unique = []          
            [unique.append(x) for x in words if x not in unique]
            finaltxt=' ; '.join(unique)
    
    return finaltxt

def replace(fname, word1,word2):
    strlist=[]
    f= open(fname, 'r')
    data = f.read()
    data=data.split("\n")
    for i in range(len(data)):
        z=data[i].split()
        for j in range(len(z)):
            if z[j]==word1:
                z[j] = word2
                
        z=' '.join(z)
        strlist.append(z)
    f.close()
        
    
    with open(fname, 'w') as f:
        for i in strlist:
            f.write(f"{i}\n")
    
    return (f'Success!! {word1} has been replaced by {word2}')


filename="runtime/question1_input.txt"
while True:
    print('''\n--------------------------------
Enter your choice:
1. Display specific Word Count
2. Display all Unique Words
3. Display all Word Counts
4. Replace word
5. Quit
--------------------------------''')

    n=int(input("Enter here: "))
    if n==1:
        check=input("Enter the word: ")
        count=word_count(filename).get(check)
        if count==None:
            count=0
        print(f"word count of {check} is {count}")
        n=0

    elif n==2:
        print(word_unique(filename)  )
        n=0

    elif n==3:
        print("word counts are: \n")
        for key, value in word_count(filename).items():
            print(key, ' : ', value)
            n=0
            
    elif n==4:

        word1=input("Enter the word to be replaced: ")
        word2=input("Recplace with: ")
        print(replace(filename, word1,word2))
        print("The original file is changed to a updated version.")
        n=0
    
    if n==0:
        continue
    
    elif n==5:
        print("program is exiting...\n")
        break
