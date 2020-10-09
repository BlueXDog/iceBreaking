package main

import (
	"fmt"
	"time"
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
	fmt.Println("hello world")
	start := time.Now()
	tinhtong(100)
	elapsed := time.Since(start)
	fmt.Printf("the running time is  %s\n", elapsed)

	nhieupheptinh(10)
	fibonaci_generate(100)

}
