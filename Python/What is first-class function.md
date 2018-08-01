# What is First-class function
Python에서는 function은 모두 **First-class function**으로 이는 function을 **First-class citizen**으로 취급하는 것을 의미한다. **First-class citizen**에 대한 상세한 내용은 Reference를 참고, 이 의미를 간단하게 요약해보자면 아래의 세 항목과 같다.

* Reference
	+ <https://ko.wikipedia.org/wiki/%EC%9D%BC%EA%B8%89_%EA%B0%9D%EC%B2%B4>
	+ <http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%8D%BC%EC%8A%A4%ED%8A%B8%ED%81%B4%EB%9E%98%EC%8A%A4-%ED%95%A8%EC%88%98-first-class-function/>

**Summary**
* First-class function (as First-class citizen)
  + function as argument
  + function as variable
  + function as return 

### Function as argument
function을 다른 function에 argument에 전달할 수 있다.

```python
def foo(a,b):
    return a + b

def bar(func, a, b):
    return func(a, b)

result = bar(foo, 1, 2)
print(result)
```

```python
3
```

### Function as variable
function은 variable이므로 다른 variable로 가리킬 수 있다.

```python
spam = foo

result = spam(1, 2)
print(result)
```

```python
3
```

### Function as return
function을 다른 function에서 return 할 수 있다.

```python
def calc_func_gen(kind):
    if kind=='add':
        def add(a, b):
            return a + b
        return add
    elif kind=='subtract':
        def subtract(a, b):
            return a - b
        return subtract

adder = calc_func_gen('add')
result = adder(1, 2)
print(result)
```

```python
3
```