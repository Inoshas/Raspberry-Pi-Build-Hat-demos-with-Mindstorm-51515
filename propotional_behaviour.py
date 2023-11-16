import matplotlib.pyplot as plt 

#Define all variables::
initial_speed_left=-20
initial_speed_right=20
initial_error=0

target_light=50
read_light=19

error=read_light-target_light
color=['red', 'blue', 'green', 'yellow']
current_error=[]

current_speed_left=[]
current_speed_right=[]

ki=[.1, .3, .5 ]
kp=[.1, .3, .5] 

count=0
#####propotional changes:::

for ki_va in ki:
    current_speed_left=[]
    current_speed_right=[]
    current_error=[]
    for item in range(-60,60,2):
        
        current_error.append(item)
        current_speed_right.append(initial_speed_right-ki_va*item)
        current_speed_left.append(-initial_speed_left+ki_va*item)
        
    plt.plot( current_error, current_speed_right, color[count])
    count +=1
plt.show()

