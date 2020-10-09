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
    
    int count;
    printf(" nhap so luong so N can test : ");
    scanf("%d", &count);
    for (int i=0 ;i<count; i++)

    {   
        int total =0;
        int N;
        printf("\n nhap so N:");
        scanf("%d", &N);
        getchar();
        clock_t time_start=clock();
        total =tinhtong(N);
        printf("tong day so la %d \n",total);
        printf("Time taken: %.5fs\n", (double)(clock() - time_start)/CLOCKS_PER_SEC);
        

        float result=0;
        time_start=clock();
        result =nhieuPhepToan(N);
        printf("ket qua thuc hien nhieu phep toan la %f \n",result);
        printf("Time taken: %.5fs\n", (double)(clock() - time_start)/CLOCKS_PER_SEC);

        time_start=clock();
        printf("day fibonaci nho hon %d \n",N);
        fibonaci_generation(N);
        printf("Time taken: %.5fs\n", (double)(clock() - time_start)/CLOCKS_PER_SEC);

    }  
    printf("ket thuc chuong trinh"); 
    return 0 ;

}