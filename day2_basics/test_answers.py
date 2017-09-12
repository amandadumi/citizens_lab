def check_forloop(variable):
    x_temp=0
    for i in range(21):
        x_temp += (x_temp + 31)/94
    if variable==x_temp:
        print('You are correct! Great job!')
    else:
        print('You are incorrect. Try again!')
