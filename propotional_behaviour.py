import matplotlib.pyplot as plt 

#Define all variables::
initial_speed_left=-10
initial_speed_right=10
initial_error=0
max_intensity=100
min_intensity=0
target_light=50


color=['red', 'blue', 'green', 'yellow', 'black', 'pink']
current_error=[]

current_speed_left=[]
current_speed_right=[]

kp=[.1, .3, .5, 1.8 ,2.4]


count=0
#####propotional changes:::

for kp_va in kp:
    current_speed_left=[]
    current_speed_right=[]
    current_error=[]
    
    for item in range(min_intensity-target_light,max_intensity-target_light,2):
        
        current_error.append(item)
        current_speed_right.append(initial_speed_right-kp_va*item)
        current_speed_left.append(-initial_speed_left+kp_va*item)
        
    plt.plot( current_error, current_speed_right, color[count], linestyle="dashed")
    plt.plot( current_error, current_speed_left, color[count], linestyle="solid")
    
    plt.xlabel("Intensity difference: Error") 
    plt.ylabel("Current speed") 
    count +=1
plt.show()

