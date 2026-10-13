Bhargavi=dict()
s=input("enter your name")
for ch in s:
    if ch not in Bhargavi:
        Bhargavi[ch]=1
    else:
        Bhargavi[ch]=Bhargavi[ch]+1 
print(Bhargavi)   