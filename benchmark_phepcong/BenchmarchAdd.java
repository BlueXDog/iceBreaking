import java.util.Random;
import java.util.Scanner;

import javax.swing.plaf.synth.SynthScrollBarUI;



public class BenchmarchAdd {

   /* This is my first java program.
    * This will print 'Hello World' as the output
    */

   public static void main(String []args) {
      Scanner scanner=new Scanner(System.in);
      System.out.println("nhap gioi han tren cua day random ");
      int rand_max=scanner.nextInt();
      System.out.println("nhap so lan thuc hien :");
      int run_counter=scanner.nextInt();
      double runningTimeTinhTong=0;
      double runningTimeNhieuPhepTinh=0;
      double runningTimeFibonaci=0;

      for( int i=0;i<run_counter;i++){
         Random rand= new Random(); 
         int rand_int=rand.nextInt(rand_max);
         System.out.println(rand_int);

         double startTime=System.nanoTime();
         tinhtong(rand_int);
         double runningTime =System.nanoTime()-startTime;
         double runningTime_second=(double)runningTime/1000000000.0;
         runningTimeTinhTong+=runningTime_second;     
         //System.out.println("this is running time in second "+ runningTime_second);
         
         startTime=System.nanoTime();
         nhieupheptinh(rand_int);
         runningTime =System.nanoTime()-startTime;
         runningTime_second=(double)runningTime/1000000000.0;
         runningTimeNhieuPhepTinh+=runningTime_second;
         //System.out.println("this is running time in second "+ runningTime_second);

         startTime=System.nanoTime();
         fibonaci_generate(rand_int);
         runningTime =System.nanoTime()-startTime;
         runningTime_second=(double)runningTime/1000000000.0;
         runningTimeFibonaci+=runningTime_second;       
         //System.out.println("this is running time in second "+ runningTime_second);
      }

      System.out.println("\n thoi gian chay trung binh tinh tong "+runningTimeTinhTong/run_counter);
      System.out.println("thoi gian chay trung binh nhieu phep tinh :"+runningTimeNhieuPhepTinh/run_counter );
      System.out.println("thoi gian chay trung binh tao day fibonaci :"+runningTimeFibonaci/run_counter);
   }
 
   public static void tinhtong(int n){
      int tong=0;
      for (int i=0;i<n;i++){
         tong +=i;
      }
      System.out.println("ket qua cua tong day so la "+tong);
   }
   public static void nhieupheptinh(int n ){
      float result=0;
      for (int i =0;i<n;i++)
      {
         result += (float)i/(float)((i+1)+(i+2));

      }
      System.out.println("ket qua cua nhieu phep tinh la :"+result);
   }
   public static void fibonaci_generate(int n){
      int first =1;
      int second =1;
      int third =0;
      System.out.print(first+" "+second );
      while(third < n){
         third=first +second;
         System.out.print(" "+third);
         first=second;
         second=third;
         
      }    
   }
}
