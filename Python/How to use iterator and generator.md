# How to use iterator and generator
Python에서 **Lazy evaluation** 을 활용하기위해서는 `iterator` object를 활용해야하며, `generator` 는 `function` object이면서 `iterator` object이다.  `iterator` object에 해당하는 object는 `generator` object외에도 `map` object, `filter` object가 있으며, 이들은 주로 anonymous function을 선언하는 `lambda` 키워드와 함께 `map`, `filter` 키워드가 사용되어 생성되며, **Lazy evaluation** 을 한다. (`reduce` 는 엄밀한 의미에서는 **Lazy evaluation** 은 아니다.) 해당 내용은 Reference에 자세히 정리되어있다. 

* Reference
	+ [How to use functional programming](https://aisolab.github.io/programming%20language/2018/08/07/Python_How-to-use-functional-programming/)

### Summary
`iterator` object와 `generator` object, 더불어 `iterator` object와 면밀한 관계가 있는 `iterable` object를 간략하게 정리하면 아래와 같다.

* `iterable` object
  + `__iter__` method가 정의되어있는 sequential data type의 object
  + `iter` function의 해당 `iterable` object를 넣으면, object의 element를 모두 가지고 있는 `iterator` object를 생성함 (eg. `list_iterator`, `str_iterator`, `tuple_iterator`)
  + `for` loop으로 순회가능하며, `iterable` object를 `for` loop로 순회하면 내부적으로 해당 `iterable` object를 기반으로 `iterator` object를 생성하여 `next` function을 적용하는 것과 같음

* `iterator` object
  + `__next__` method와 `__iter__` method가 정의되어있는 sequential data type의 object
  + 해당 object를 `for` loop로 한번 순회하면 그 이후 순회해도 object의 element에 접근불가
  + `next` function으로 object의 element를 다 꺼내면 `StopIteration` error 발생

* `generator` object
  + `function` object 이면서 `iterator` object의 일종
  + function을 정의시 `return` 대신 `yield` 를 사용하여 `generator` object 생성, `return` 은 function을 바로 종료시키는 반면 `yield` 는 그렇지 않다.

### Template
* `iterator` object
`class` 를 이용해서 `iterator` object를 정의하고 싶을 경우 일반적으로 아래와 같이 정의한다.

```python
class It:
    def __init__(self, *args):
        self.data = args
        self.idx = 0
        
    def __iter__(self): # __iter__ method 정의시 그냥 자기자신을 return
        return self 
    
    def __next__(self):

        if self.idx >= len(self.data):
            raise StopIteration
        else:
            elm = self.data[self.idx]
            self.idx += 1
            return elm
```

```bash
1
2
3
4
iterator가 element를 다 꺼냈습니다.
```

* `generator` object

```python
def gen():
    yield 1
    yield 2
    yield 3
    yield 4
```

```python
generator = gen()
print(type(generator))

try:
    while True:
        print(next(generator))
except StopIteration:
    print('StopIterator error 발생')
```

```bash
<class 'generator'>
1
2
3
4
StopIterator error 발생
```

### Example : Fibonacci number
* Non generator

```python
# non generator
def make_fibo(n):
    result = []
    a = 0
    b = 1
    for i in range(n):
        result.append(a)
        a, b = b, a+b
    else:
        return result

result = make_fibo(10)
print(result)
```

```bash
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

* Generator

```python
# generator
def make_fibo(n):
    a = 0
    b = 1 
    
    for _ in range(n):
        yield a
        a, b = b, a+b
        
gen = make_fibo(10)

result = []

try:
    while True:
        result.append(next(gen))
except StopIteration:
    print(result)
```

```bash
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

* Bonus : Recursive call

```python
# recursion call
def make_fibo(n):
    if n == 1:
        return 0
    elif n == 2 :
        return 1
    else:
        return make_fibo(n-1) + make_fibo(n-2)
    
result = [make_fibo(i) for i in range(1,11)]
print(result)
```


```bash
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```