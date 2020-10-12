package main

import (
	"fmt"
	time "time"
	"math/rand"
)

func tinhtong(N int) error {
	var result = 0
	for a := 0; a < N; a++ {
		result += a
	}
	fmt.Println("gia tri tong la :  ", result)
	return nil
}
func nhieupheptinh(N int) error {
	var result float64
	result = 0
	for a := 0; a < N; a++ {
		result += float64(a) / float64(((a + 1) * (a + 2)))

	}
	fmt.Println("gia tri cua nhieu phep tinh la: ", result)
	return nil
}
func fibonaci_generate(N int) error {
	first := 1
	second := 1
	fmt.Println("Day so fibonaci la :")
	fmt.Print(first, " ", second)
	third := 2
	for third < N {

		fmt.Print(" ", third)

		first = second
		second = third
		third = first + second
	}
	fmt.Print("\n")
	return nil
}

func main() {
	var randMax,randMin int
	var counter int
	var timeTinhTong,timeNHieuPhepTinh,timeFibonaci int64
	fmt.Println("hello world")
	fmt.Println("nhap so lan thuc hien :")
	fmt.Scanln(&counter)
	fmt.Println("nhap gioi han tren so random:")
	fmt.Scanln(&randMax)
	fmt.Println("nhap gioi han duoi so random")
	fmt.Scanln(&randMin)
	for i:=0 ;i<counter ; i++{
		randNum:=rand.Intn(randMax-randMin)+randMin
		
		start := time.Now()
		tinhtong(randNum)
		elapsed :=time.Since(start)
		timeTinhTong+=int64(elapsed)
		fmt.Printf("the running time is  %d\n", timeTinhTong)

		start = time.Now()
		nhieupheptinh(randNum)
		elapsed =time.Since(start)
		timeNHieuPhepTinh+=int64(elapsed)
		fmt.Printf("the running time is  %d\n", timeNHieuPhepTinh)

		start = time.Now()
		tinhtong(randNum)
		elapsed =time.Since(start)
		timeFibonaci+=int64(elapsed)
		fmt.Printf("the running time is  %d\n", timeFibonaci)
	}
	fmt.Printf("thoi gian thuc hien trung binh tinh tong la %fs\n",float64(timeTinhTong)/(float64(counter)*1000000000.0))
	fmt.Printf("thoi gian thuc hien trung binh nhieu phep tinh la %fs\n",float64(timeNHieuPhepTinh)/(float64(counter)*1000000000.0))
	fmt.Printf("thoi gian thuc hien trung binh tao day fibonaci la %fs\n",float64(timeFibonaci)/(float64(counter)*1000000000.0))

	


}
