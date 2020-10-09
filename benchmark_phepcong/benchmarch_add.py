import time
import sys



def tinhtong(max_n):
    total=0
    for i in range (max_n):
        total+=i
    return total
def nhieupheptoan(max_n):
    result =0
    for i in range (max_n):
        result += i/((i+1)*(i+2))
    return result
def fibonaci_generate(max_n):
    first=1
    second=1
    fibo_arr=[]
    fibo_arr.append(first)
    fibo_arr.append(second)
    for _ in range (n):
        third =first+second
        if third > n:
            break
        fibo_arr.append(third)
        first=second
        second=third
       
    return fibo_arr



log_file =open("../log_file.txt","ab+")
log_file.write(b" day la log cua python file \r\n")
print (" nhap day so N ")
N =map (int, input().split(" ") )
for n in N :
    print("thuc hien phep toan voi n =", n)
    start_time=time.time()
    total =tinhtong(n)
    print ("tong day so la total",total)
   
    print("thoi gian thu hien la %f voi N = %d " %(time.time()- start_time , n))
    log_file.write(b"thoi gian thu hien la %f voi N = %d \r\n " %(time.time()- start_time , n))
    
    start_time=time.time()
    result =nhieupheptoan(n)
    print ("tong nhieu phep toan la total",result)
   
    print("thoi gian thu hien la %f voi N = %d  " %(time.time()- start_time , n))
    
    start_time=time.time()
    fibonaci_arr =fibonaci_generate(n)
    print("day fibonaci la ",fibonaci_arr)
   
    print("thoi gian thu hien la %f voi N = %d  " %(time.time()- start_time , n))



log_file.close()


