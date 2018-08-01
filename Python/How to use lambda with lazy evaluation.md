# How to use lambda with lazy evaluation 

Python에서 **Anonymous function**이 필요할 때, `lambda`를 활용하며, **Anonymous function**은 주로  **Lazy evaulation**을 활용하기위한 function인 `map`, `filter`, `reduce` 와 같이 활용한다.

### lambda

`lambda`는 **Anonymous function**을 선언하기 위한 것으로 **Anonymous function**을 활용하는 이유는 한번만 사용할 function이라서, **global frame**에 function에 대한 메모리를 할당할 필요가 없을 경우에 활용한다.

```python
result = (lambda a, b : a + b)(1,3)
print(result)
```

```python
4
```

확인
<iframe width="800" height="500" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=result%20%3D%20%28lambda%20a,%20b%20%3A%20a%20%2B%20b%29%281,3%29%0Aprint%28result%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>


물론 function을 명시적으로 선언하여, **global variable**에 해당 function을 variable이 가리키게 할 수도 있다. 즉 **global frame**에 function에 대한 메모리를 할당할 수 도 있다.

```python
f = lambda a, b : a + b
result = f(1, 3)
print(result)
```

```python
4
```

