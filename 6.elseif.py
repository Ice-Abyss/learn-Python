point=input('please enter your point:')
point=int(point)

if point>100:
    print('Please enter ture point!')
elif point>=80 and point<=100:
    print('Nice!')
elif point>=60 and point<80:
    print('Good!')
elif point>=0 and point<60:
    print('Try again!You can!')
else :
    print('Enter ture point!')
    
