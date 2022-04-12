# Arrays and Slices

##Arrays and slices in golang.

[Golang Spec](https://go.dev/ref/spec#Array_types)

### Arrays 

Spec 

```go

ArrayType   = "[" ArrayLength "]" ElementType .
ArrayLength = Expression .
ElementType = Type .

```

Examples.


```go

var arr [20]int // declare 

var arr = [3]int{1,2,3} // declare and initialize

arr := [...]{1, 2, 3} // auto-determine the arraysize

arr := [20]int // shorthand 
arr := [2*N] struct { x, y int32 }

```


### Slices

- built on top of arrays
- slices are dynamic
- simillar to vector in c++
- by default is initialized to 0-value, nil.

[more on Slices](https://www.youtube.com/watch?v=3SCgZLb4ZYw)

Spec

```go

SliceType = "[" "]" ElementType .

```

Slices can also be initialized.

```go

slice = make([]T, length, capacity)

```


Examples.

```go

var slice []int // declare

var slice = []int{1,2,3} // declare and initialize

slice := []int{1,2,3} // declare and initialize

// with make()

slice := make([]int, 100) // capacity is optional
slice := make([]int, 100, 100)

```
## Arrays and Slices in Rust.