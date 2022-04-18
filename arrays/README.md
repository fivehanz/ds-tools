# Arrays and Slices

## in Rust.

### Arrays

[Rust Array Spec](https://doc.rust-lang.org/std/primitive.array.html)

```rust

// assign array with contents of expr repeated for Size elements.
let array: [Type; Size] = [expr; Size]

let array: [Type; Size] = [x, y, z, ..]


```

Examples

```rust

// create an array of type i32, length N
let mut array: [i32; 3] = [1, 2, 3];

let mut array: [i32; 3] = [0; 3];


```

### Slice

A dynamically-sized view into a contiguous sequence, [T]. 

Slices are similar to arrays, but their length is not known at compile time. Instead, a slice is a two-word object, the first word is a pointer to the data, and the second word is the length of the slice.

A slice is a kind of reference, so it does not have ownership.

[Rust Slice Spec](https://doc.rust-lang.org/std/primitive.slice.html)

```rust

let s = String::from("hello world");

let hello = &s[0..5];
let world = &s[6..11];

```

[More on Slices in Rust](https://doc.rust-lang.org/book/ch04-03-slices.html)

Note: Rust also has [Vectors](https://doc.rust-lang.org/std/vec/) in the std lib.

## in Go.

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
- similar to vector in c++
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