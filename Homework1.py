language, number=input("Type in language and number,split by comma\n").split(',')
if language == 'English':
 text = 'Hello'
elif language == 'Chinese':
 text = 'Nihao'
elif language == 'Russian':
 text = 'Privet'

for i in range(int(number)):
    print(text)
