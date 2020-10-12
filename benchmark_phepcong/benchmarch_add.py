import time
import sys
import random



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
    for _ in range (max_n):
        third =first+second
        if third > max_n:
            break
        fibo_arr.append(third)
        first=second
        second=third
       
    return fibo_arr

if __name__ == "__main__":
    time_tinhtong=0
    time_nhieupheptoan=0
    time_fibonaci=0
    log_file =open("../log_file.txt","ab+")
    log_file.write(b" day la log cua python file \r\n")
    print("Thuc hien N lan phep toan ,tinh thoi gian trung binh\n")

    print (" nhap so lan thuc hien N  ")

    N =input()
    print("nhap khoang tao so random ")
    print("nhap so dau")
    rand1=int(input())
    print("nhapp so tiep theo")
    rand2=int(input())

    for i in range(int(N)):
        n_random=random.randint(rand1,rand2)

        start_time=time.time()
        tinhtong(n_random)
        time_tinhtong+=time.time()-start_time
        
        start_time=time.time()
        nhieupheptoan(n_random)
        time_nhieupheptoan+=time.time()-start_time

        start_time=time.time()
        fibo_arr=fibonaci_generate(n_random)
        print(fibo_arr)
        time_fibonaci+=time.time()-start_time

    print("\nthoi gian thuc hien phep cong trung binh ",time_tinhtong/int(N))
    print("\nthoi gian thuc hien nhieu phep tinh trung binh ",time_nhieupheptoan/int(N))
    print("\nthoi gian thuc hien tao day fibonaci trung binh ",time_fibonaci/int(N))
       #print("thuc hien phep toan voi n =", n)
    #start_time=time.time()
    #total =tinhtong(n)
    #print ("tong day so la total",total)

    

   
    



log_file.close()


