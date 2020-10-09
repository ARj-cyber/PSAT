# problem 7



t1a , t1b ,t1c = input("Enter First timestamps ") .split()
t2a , t2b ,t2c = input("Enter Second timestamps ") .split()
t1 = ( int(t1a)* 3600 )+(int(t1b)*60)+int(t1c)
t2 = ( int(t2a)* 3600 )+(int(t2b)*60)+int(t2c)
tot = int(t2)-int(t1)
print ("Seconds between the two timestamps is " , int(tot) )
