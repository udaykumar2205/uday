w1=int(input('enter first word'))
w2=int(input('enter second word'))
if sorted(w1)==sorted(w2):
    print('w1,w2 are anagrams')
else:
    print('w1,w2 are not anagrams')
