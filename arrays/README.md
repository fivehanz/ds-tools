# Arrays and Slices

Arrays and slices in golang. [Golang Spec](https://go.dev/ref/spec#Array_types)

## Arrays 

Spec 

```go

ArrayType   = "[" ArrayLength "]" ElementType .
ArrayLength = Expression .
ElementType = Type .

```

Examples.


```go

arr = [20]int
arr = [2*N] struct { x, y int32 }

```


## Slices

- built on top of arrays



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
```
