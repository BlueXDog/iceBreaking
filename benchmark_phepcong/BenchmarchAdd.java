import javax.swing.plaf.synth.SynthScrollBarUI;

public class BenchmarchAdd {

   /* This is my first java program.
    * This will print 'Hello World' as the output
    */

   public static void main(String []args) {
      System.out.println("Hello World"); // prints Hello World
      
      
      long startTime=System.nanoTime();
      
      for(int i=0; i< 100; i++){
         greeting();
     }
      double runningTime =System.nanoTime()-startTime;

      double runningTime_second=(double)runningTime/1000000000.0;
      System.out.println("this is running time:" + runningTime);
      System.out.println("this is runnign time in second "+ runningTime_second);

     tinhtong(100);
     fibonaci_generate(100);

   }
   public static void greeting(){
      System.out.println("this is vinh");
      return;
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
