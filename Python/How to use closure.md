# How to use closure

Python에서 **객체지향(Object-Oriented Programming, OOP)** 을 구현하는 수단 중 하나인  **closure**를 사용하는 방법에 대하여 정리, 사실 Python은 을 `class`로 지원하기 때문에, ***사실 Closure를 사용할 일은 거의 없으며***, 먼저 **Closure**에 대해 정리하기에 **Namespace**을 알아야 하기 때문에 같이 정리

### Namespace

variable에는 **global variable**과 **local variable**이 있으며 **local variable**의 경우는 **global variable**과 달리 function을 선언할 때, 해당 function의 **Namespace**에서 존재한다. 즉 다시 말해서 **local variable**은 각각의 function마다 각각의 function **Namespace**에 존재한다. 요약해서 정리하면 아래와 같다.

* global variable : variable, function (Python에서는 모든 것이 object이므로)
* local variable : function 내에서 선언되는 variable들

코드로는 아래와 같이 확인해볼 수 있다.

#### global variable vs local variable
```python
a = 10 # global variable
def func():
	a = 20 # func namespace에 있는 local variable a
	print('{} in func'.format(a))

func()
print(a)
```

```python
20 in func # func namespace에 있는 local variable a 출력
10 # global variable a 출력
```

#### function 내부에서 global variable 참조 또는 수정
**local variable**을 생성하지않고, function의 내부에서 **global variable**을 참조하는 것이 가능하다. 단 이 경우에는 수정이 불가능하며 function 내부에서 **global variable**을 수정하고 싶으면 `global` keyword를 활용한다. ***그런데 사실 function 내부에서 global variable을 참조하거나 활용하는 것은 사실하지 말아야할 행위이다.***

##### function 내부에서 global variable 참조
```python
# function 내부에서 global variable을 참조하는 것이 가능
a = 10 # global variable
def func():
    print(a)
    
func()
```

```python
10 # global variable
```

##### function 내부에서 global variable 수정 
* `global` keyword를 활용하지 않을 때, `UnboundLocalError` 발생
```python
# function 내부에서 global variable을 global keyword없이 수정하는 것은 불가능
a = 10
def func():
    a += 1
    print(a)

func()
```

```python
# UnboundLocalError 발생
UnboundLocalError                         Traceback (most recent call last)
<ipython-input-3-769091722474> in <module>()
      4     print(a)
      5 
----> 6 func()

<ipython-input-3-769091722474> in func()
      1 a = 10
      2 def func():
----> 3     a += 1
      4     print(a)
      5 

UnboundLocalError: local variable 'a' referenced before assignment
```

* `global` keyword를 활용하면, function 내부에서 **global variable** 수정가능

```python
# 전역변수를 함수내에서 수정하려면
a = 10
def func():
    global a
    a += 1
    print(a)
    
func()
print(a)
```

```python
11 # global variable 
11 # global variable
```

#### nonlocal variable
**nonlocal variable**은 ***global variable도 아니고 local variable도 아닌 variable이다.*** 사실상 Python에서 **Closure**를 구현하기위한 핵심 내용 중 하나이다. 코드로는 아래와 같이 확인할 수 있다.

```python
# function마다 고유한 namespace를 가지고 있다.
a = 10 # global variable a 
def outer():
    b = 20 # nonlocal variable: outer function의 namespace에 있는 variable b
    def inner():
        c = 30 # local variable: inner funciont의 namespace에 있는 variable c
        print(a, b, c)
    inner()

outer()
```

```python
10 20 30
```

`nonlocal` keyword를 이용해 **nonlocal variable**을 수정할 수 있다.

```python
# function마다 고유한 namespace를 가지고 있다.
a = 10 # global variable a 
def outer():
    b = 20 # nonlocal variable: outer function의 namespace에 있는 variable b
    def inner():
        nonlocal b
        c = 30 # local variable: inner funciont의 namespace에 있는 variable c
        b += 30 # nonlocal variable b를 수정함
        print(a, b, c)
    inner()

outer()
```

```python
10 50 30
```
### Closure
**Closure**는 **nonlocal variable**을 이용하여 구현하며, **nonlocal variable**을 상태 정보(free variable)를 저장하는데 활용한다. 예시로 아래와 같이 간단한 은행계좌를 구현하여 확인

#### Example
##### Bank account를 Closure로 구현
```python
# 은행계좌를 Closure로 구현
def account(name, money):
    def change_money(amount):
        nonlocal money
        money += amount
        return name, money
    return change_money

aisolab_acnt = account('aisolab', 300)
modulab_acnt = account('modulab', 5000)

print(aisolab_acnt(200), modulab_acnt(5000))
print(aisolab_acnt.__name__, modulab_acnt.__name__)
print(aisolab_acnt.__class__, modulab_acnt.__class__)
print(aisolab_acnt.__code__ == modulab_acnt.__code__)
print(aisolab_acnt == modulab_acnt)
```

```python
('aisolab', 500) ('modulab', 10000)
change_money change_money
<class 'function'> <class 'function'>
True
False
```

##### Digging the inside of Closure
* function 내부의 closure에 **nonlocal variable** (상태정보를 담고있는 free variable을 담는데 활용)의 값들을 저장

```python
aisolab_closure = aisolab_acnt.__closure__
print([cell.cell_contents for cell in aisolab_closure])
```

```python
[500, 'aisolab']
```

* function의 code object에 **nonlocal variable** (상태정보를 담고있는 free variable을 담는데 활용) name과 **local variable**의 name을 저장

```python
aisolab_code_object = aisolab_acnt.__code__
print(aisolab_code_object.co_freevars)
print(aisolab_code_object.co_varnames)
```

```python
('money', 'name')
('amount',)
```
