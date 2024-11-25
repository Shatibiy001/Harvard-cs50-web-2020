welcome="welcome to ASH-SHATIBIY bank how may i help you"
print(welcome)
name1=str(input('enter your first name:'))
name2=str(input('enter your second name:'))
print(name1,name2)
details=input('enter your 10 digit account details:'))
if len(details) > 10:
  print('your details is more then 10 digit ')
if len(details) < 10: 
  print('your details is not up to 10 didgit')
if len(details) == 10:
  print('thanks for entring the correct info')
