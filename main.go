package main

import "fmt"

func foobar() int {
	x := 0
	y := 1
	return func() {
		x = y
		y = y + x
		return x
	}
}

func main() {
	for i := 0; i < 10; i++ {
		if i%2 == 0 {
			fmt.Println(foobar())
		}
	}
}
