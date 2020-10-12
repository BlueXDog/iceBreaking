#include<stdio.h>
#include<time.h>
#include<math.h>

int tinhtong (int N){
    int total=0;
    for (int j=0;j<N;j++)
        {
            total+=j;
        }
    return total;

}
float nhieuPhepToan(int N){
    float result=0.0;
    for (int j=1;j<=N;j++)
    {
        result +=(float)j/(float)((j+1)+(j+2));
        
    }
    return result;
}
void fibonaci_generation(int N)
{
    int first =1;
    int second =1 ;
    printf ("%d ",first);
    printf(" %d ",second);
    int third =0;
    while (third <N)
    {
        third=first+second;
        printf("%d ",third);
        first=second;
        second=third;
    }



}
int main ()
{
    //printf("hello this is vinh");
    int max_rand, min_rand;
    int count;
    double time_tinhtong, time_nhieupheptinh,time_fibonaci;
    printf(" nhap so luong so N can test : ");
    scanf("%d", &count);
    printf("nhap gioi han tren :");
    scanf("%d", &max_rand);
    printf("nhap gioi han duoi :");
    scanf("%d",&min_rand);
    for (int i=0 ;i<count; i++)

    { 
        int randNum =min_rand+rand() %(max_rand-min_rand+1);

        int total =0;
        
        clock_t time_start=clock();
        total =tinhtong(randNum);
        printf("tong day so la %d \n",total);
        time_tinhtong+=(double)(clock() - time_start)/CLOCKS_PER_SEC;
        printf("Time taken: %.5fs\n", time_tinhtong);
        

        float result=0;
        time_start=clock();
        result =nhieuPhepToan(randNum);
        printf("ket qua thuc hien nhieu phep toan la %f \n",result);
        time_nhieupheptinh+=(double)(clock() - time_start)/CLOCKS_PER_SEC;
        printf("Time taken: %.5fs\n", time_nhieupheptinh);

        time_start=clock();
        printf("day fibonaci nho hon %d \n",randNum);
        fibonaci_generation(randNum);
        time_fibonaci+=(double)(clock() - time_start)/CLOCKS_PER_SEC;
        printf("Time taken: %.5fs\n", time_fibonaci);

    }  
    printf("thoi gian tinh tong trung binh: %.5fs \n",time_tinhtong/count);
    printf("thoi gian thuc hien nhieu phep tinh trung binh :%.5fs\n",time_nhieupheptinh/count);
    printf("thoi gian thuc hien tao day fibonaci : %.5fs \n",time_fibonaci/count);
    printf("ket thuc chuong trinh"); 
    return 0 ;

}