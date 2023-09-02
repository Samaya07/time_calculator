def add_time(start_time,duration_time,day=None):
    list_start=[]
    list_duration=[]
    list_start=start_time.split(" ")
    day_night=list_start[1]               #specifies 'AM' or 'PM'
    list_start=list_start[0].split(":")        #this list holds the hours and mins of start time
    list_duration=duration_time.split(":")     #this list holds the hours and mins of duration time
    ans_list=[0,0]
    list_start[0]=int(list_start[0])
    list_start[1]=int(list_start[1])
    if day_night=='PM':
        if list_start[0]!=12:
            list_start[0]=int(list_start[0])+12  #changing the start time to 24 hours format
    ans_list[1]=int(list_start[1])+int(list_duration[1])
    if ans_list[1]>=60:
        ans_list[1]=ans_list[1]-60  
        ans_list[0]=ans_list[0]+1       
    ans_list[0]=ans_list[0]+list_start[0]+int(list_duration[0])
    days=ans_list[0]//24            #calculating number of days from start time after adding duration time
    if ans_list[0]%24!=0:
        ans_list[0]=(ans_list[0]%24)   #changing result time back to 12 hour format
        while(ans_list[0]>24):
            ans_list[0]=ans_list[0]-12
            day_night='PM'
        if ans_list[0]<12:
            day_night='AM'  
        if ans_list[0]>12:
            ans_list[0]=ans_list[0]-12
            day_night='PM'
        if ans_list[0]==12:
            day_night='PM'
    else:    
        while(ans_list[0]>24):
            ans_list[0]=ans_list[0]-12
            day_night='AM'
        if ans_list[0]<12:
            day_night='AM'  
        if ans_list[0]>12:
            ans_list[0]=ans_list[0]-12
            day_night='PM'
        if ans_list[0]==12:
            day_night='AM' 
    day_result=''
    if day!=None:
        current_day=day.capitalize()  
        day_result=days_def(current_day,days)     #calculating the resultant day
    
    result=print_format(ans_list,day_result,day_night,days,day)
    print(result)    

def print_format(ans_list,day_result,day_night,days,day): #the exact print format in the output
    if day==None:
        result=''
        result=result+str(ans_list[0])+':'
        if ans_list[1]<10:
            result=result+'0'+str(ans_list[1])
        else:
            result=result+str(ans_list[1])
    
        result=result+' '+day_night
        if days==1:
            result=result+' (next day)'
        elif days>1:
            result=result+' ('+str(days)+' days later)'
    else:
        result=''
        result=result+str(ans_list[0])+':'
        if ans_list[1]<10:
            result=result+'0'+str(ans_list[1])
        else:
            result=result+str(ans_list[1])
    
        result=result+' '+day_night
        result=result+', '+day_result
        if days==1:
            result=result+' (next day)'
        elif days>1:
            result=result+' ('+str(days)+' days later)'
    return result


def days_def(day,noOfDays): #decides the resultant day after adding number of days
    week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    index=week.index(day)
    index=(index+noOfDays)%7
    return week[index]
            

add_time("11:30 PM","00:30",'thursDay')