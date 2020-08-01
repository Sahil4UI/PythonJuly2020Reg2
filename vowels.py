# for Given String, count the number of vowels , consonants & digits & special char
#in the number
string=input("Enter String : ")
vowels="aeiouAEIOU"
count_vow=0
for i in range(0,len(string)):
    if (string[i] >= 'a' and string[i] <='z') or  (string[i] >= 'A' and string[i] <='Z') :
        if string[i] in vowels:
            #count_vow+=1
            count_vow = count_vow+1
        

print("Vowels Count",count_vow)
            
            
