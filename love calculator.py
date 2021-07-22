watch_word = 'love'
names = input('enter: ').lower()
name = input('enter: ').lower()
u = (name + names)
#print(u)
l = []
for x in u:
    if x in watch_word:
      l.append(x)
L = str(len(l))
print(f'Number of letter in LOVE = {L}')

m = []
chck_word = 'true'
for v in u:
    if v in chck_word:
        m.append(v)
M = str(len(m))
print(f'Number of letter in TRUE ={M}')
result = L + M
#print(result)
con_integer = int(result)
if con_integer >40 <= 50:
    print(f'Your scores is {con_integer}, you are alright together')
elif con_integer < 40:
    print(f'score {con_integer} heartbreak is real')
else:
    print(con_integer)
