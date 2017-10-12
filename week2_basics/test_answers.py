


def check_forloop2(start,end,step_size,value):
    if start==10:
        print('Your start variable is correct! Great job!')
    else:
        print('Your start variable is incorrect. Try again!')
    if end==0:
        print('Your end variable is correct! Great job!')
    else:
        print('Your end variable is incorrect. Try again!')
    if step_size==-2:
        print('Your step_size variable is correct! Great job!')
    else:
        print('Your step_size variable is incorrect! Try again!')
    if value==36:
        print('Your value variable is correct! Great job!')
    else:
        print('Your value variable is incorrect! Try again!')

def check_forloop2(variable):
    x_temp=0
    for i in range(21):
        x_temp += (x_temp + 31)/94
    if variable==x_temp:
        print('You are correct! Great job!')
    else:
        print('You are incorrect. Try again!')

def check_fuelcells(fcn):
    if fcn==8:
        print('Your fuel cell calculation is correct! Great job!')
    else:
        print('Your fuel cell calculation is incorrect! Try again!')
