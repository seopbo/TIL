# How to use functional programming 

Python에서 **Functional programming**을 활용하는 방법으로 `lambda`를 활용하며, `lambda`로 선언한 **Anonymous function**은 주로 **Functional programming**을 더 효율적으로 활용하기위해서 `map`, `filter`, `reduce` 등과 같이 활용되며,  이 때 **Functional programming**이 지원하는 **Lazy evaulation**은 `map`, `filter`에 적용된다

* Reference
	+ <https://www.dataquest.io/blog/introduction-functional-programming-python/>
	+ <http://bluese05.tistory.com/55>
	+ <http://bluese05.tistory.com/56?category=559959>
	+ <https://devbruce.github.io/2018/01/23/py-14lazy+evaluation/>
	+ <https://jiminsun.github.io/2018-05-11/Iteration/>

### lambda
Python에서 `lambda`는 **Anonymous function**을 선언하기 위한 것으로 **Anonymous function**을 활용하는 이유는 한번만 사용할 function이라서, **global frame**에 function에 대한 메모리를 할당할 필요가 없을 경우에 활용한다.

[아래의 예시에 대한 동작 확인](http://pythontutor.com/visualize.html#code=result%20%3D%20%28lambda%20a,%20b%20%3A%20a%20%2B%20b%29%281,3%29%0Aprint%28result%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
result = (lambda a, b : a + b)(1,3)
print(result)
```

```python
4
```

물론 function을 명시적으로 선언하여, **global variable**에 해당 function을 variable이 가리키게 할 수도 있다. 즉 **global frame**에 function에 대한 메모리를 할당할 수 도 있다.

[아래의 예시에 대한 동작 확인](http://pythontutor.com/visualize.html#code=f%20%3D%20lambda%20a,%20b%20%3A%20a%20%2B%20b%0Aresult%20%3D%20f%281,%203%29%0Aprint%28result%29&cumulative=false&curInstr=6&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
f = lambda a, b : a + b
result = f(1, 3)
print(result)
```

```python
4
```

### Lazy evaluation
**Lazy evaluation**은 **Functional programming**의 특징 중 하나로 필요할 때만 연산을 수행하여, 실행 속도를 계산하는 방법이다. Python에서 `iterator` object에 대해서만 동작하며, `iterator` object는 간단하게 말하자면 `next` function으로 데이터를 순차적으로 호출 가능한 object이다. (`__next__` method가 존재한다는 뜻) Python에서는 `map`, `filter`가 생성하는 각각의 `map` object, `filter` object 등이 `iterator` object이다. `reduce`로 하는 연산은 **Lazy evaluation**이 아니다. 그러므로 주의해야할 것은 `map` object, `filter` object를 일부러 `list` function을 이용하여, `iterable`로 바꾸는 것은 멍청하고 비효율적인 행동이다. **Lazy evaluation**을 활용하지 못하기 때문이다.

`lambda`와는 아래와 같이 조합하여 활용한다.

#### map
`map`은 function과 `iterable`한 object를 받아서 `iterator` object를 내준다.

```python
some_list = [1, 2, 3, 4, 5]
result = map(lambda elm : elm + 1, some_list)
print(result)
```

```python
<map object at 0x108e490f0>
```

`map` object가 `iterator` object인지 아래와 같이 확인, `next` function이 동작한다.

```python
try:
    while True:
        print(next(result))
except StopIteration as e:
    print('iterator가 다 element를 내주었습니다.')
```

```python
2
3
4
5
6
iterator가 다 element를 내주었습니다.
```

물론 `for` 문도 동작한다.

```python
for elm in result:
    print(elm)
```

```python
2
3
4
5
6
```

#### filter
`filter`는 function과 `iterable`한 object를 받아서 `iterator` object를 내준다. 이 때 function의 return 값은 `True` 또는 `False`이도록 하며, `filter`는 `iterable` object에서 `True`인 것만 뽑아 `iterator` object를 만든다.

```python
# boolean으로 봤을 때, True인 것과 False인 것 골라내기
some_list = [{},[],0,'',None,{'userid' : 'aisolab'},
             ['modulab'], 10, 'boseop']

true_list = filter(lambda elm : bool(elm) == True, some_list)
false_list = filter(lambda elm : bool(elm) == False, some_list)
print(true_list, false_list)
```

```python
<filter object at 0x1115e6438> <filter object at 0x1115e63c8>
```

`filter` object가 `iterator` object인지 아래와 같이 확인, `next` function이 동작한다.

```python
try:
    while True:
        print(next(true_list))
except StopIteration as e:
    print('iterator가 다 element를 내주었습니다.')
```

```python
{'userid': 'aisolab'}
['modulab']
10
boseop
iterator가 다 element를 내주었습니다.
```

물론 `for` 문도 동작한다.

```python
for elm in false_list:
    print(elm)
```

```python
{}
[]
0

None
```

### reduce
`reduce` function은 function과 `iterable`한 object를 받아 하나의 value를 내준다.

```python
from functools import reduce

some_list = [1,2,3,4,5]
add_result = reduce(lambda elm1, elm2 : elm1 + elm2, some_list)
max_result = reduce(lambda elm1, elm2 : elm1 if elm1 >= elm2 else elm2, some_list)
print(add_result, max_result)
```

```python
15 5
```

또한 `reduce` function은 initial value를 줄 수 있다.

```python
add_initial_result = reduce(lambda elm1, elm2 : elm1 + elm2, some_list, 10)
print(add_initial_result)
```

```python
25
```

initail value를 이용하여 아래와 같이 빈도수를 세는 reduce 연산도 가능하다.
```python
result = reduce(lambda dic, elm : dic.update({elm : dic.get(elm, 0) + 1}) or dic, char_list, {})
print(result)
```

```python
{'a': 3, 'b': 2, 'c': 1}
```
