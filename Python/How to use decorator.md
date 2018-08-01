# How to use decorator
Python에서 function에 기능을 추가할 때, ***실제로는 추가할 기능을 가지고 있으며, function을 입력으로 전달받는 specific function을 선언하여 활용하게된다.*** 하지만 Python에서 지원하는 **decorator keyword**인 `@` keyword를 이용하면 아주 손쉽게 기능을 추가할 수 있다.

* Reference
	+ <https://aisolab.github.io/programming/2018/02/28/Python_decorator/>

### Template
**decorator** 기능을 활용하는 것은 크게 아래의 형태를 벗어나지 않는다.

* decorator function을 생성
```python
def decorator_func(func):
    def __wrapper(*args, **kwargs): 
    	# positional argument들은 packing하여 local variable args에 받는다
    	# keyword argument들은 packing하여 local variable kwargs에 받는다.
        print('things to do') # 추가하고 싶은 기능(실행문)을 작성
        return func(*args, **kwargs)
        # return할 때 local variable args, kwargs unpacking해서 기능을 추가하고자하는
        # function에 전달한다.
    return __wrapper # decorator_func은 __wrapper func은 return한다.
```
* 기능을 추가하고 싶은 function에 decorator function을 활용하여 기능 추가
  + 기능을 추가하고 싶은 function
  ```python
  def add(a,b):
      '''To add a and b      
          
         Args:
             a : int or numeric type
             b : int or numeric type
         Returns:
           a + b : int or numeric type
      '''
      return a + b
  
  print(add.__name__)
  print(add.__doc__)
  ```

  ```python
  add
  To add a and b      
          
         Args:
             a : int or numeric type
             b : int or numeric type
         Returns:
           a + b : int or numeric type
  ```

  + decorating func without `@` keyword
  ```python
  add = decorator_func(add)
  result = add(1,3)
  print(result)
  print(add.__name__)
  print(add.__doc__)
  ```

  ```python
  # add function에 print('things to do') 기능이 잘 추가되었으나, decorator_func의 return이 __wrapper이므로 add.__name__, add.__doc.__이 각각 __wrapper.__name__, __wrapper.__doc__을 가리키게 됨
  things to do
  4
  __wrapper 
  None 
  ```

  + decorating func with `@` keyword
  ```python
  @decorator_func
  def add(a,b):
      return a + b
  
  result = add(1,3)
  print(result)
  print(add.__name__)
  print(add.__doc__)
  ```

  ```python
  # add function에 print('things to do') 기능이 잘 추가되었으나, decorator_func의 return이 __wrapper이므로 add.__name__, add.__doc.__이 각각 __wrapper.__name__, __wrapper.__doc__을 가리키게 됨
  things to do
  4
  __wrapper
  None
  ```

위의 template과 같이 `@` keyword를 활용하면, 매우 손쉽게 `add` function에 기능을 추가할 수있으나, `add` function의 `add.__name__` 과 `add.__doc__`이 `decorator_func` function의 내부 function인 `__wrapper` function의 `__wrapper.__name__`과 `__wrapper.__doc__`을 가리키게되며, 이 같은 문제를 해결하기위해서는 `decorator_func`을 정의할 때,  `functools` module에서 `wraps` function을 불러워서 아래와 같이 활용하면 해결 가능

```python
from functools import wraps
def decorator_func(func):
    @wraps(func)
    def __wrapper(*args, **kwargs): 
        # positional argument들은 packing하여 local variable args에 받는다
        # keyword argument들은 packing하여 local variable kwargs에 받는다.
        print('things to do') # 추가하고 싶은 기능(실행문)을 작성
        return func(*args, **kwargs)
        # return할 때 local variable args, kwargs unpacking해서 기능을 추가하고자하는
        # function에 전달한다.
    return __wrapper # decorator_func은 __wrapper func은 return한다.
```

```python
@decorator_func
def add(a,b):
    '''To add a and b      
        
       Args:
           a : int or numeric type
           b : int or numeric type
       Returns:
         a + b : int or numeric type
    '''
    return a + b

result = add(1,3)
print(result)
print(add.__name__)
print(add.__doc__)
```

```python
things to do
4
add
To add a and b      
        
       Args:
           a : int or numeric type
           b : int or numeric type
       Returns:
         a + b : int or numeric type
```

### Example : time_check
function마다 실행되는 데 걸리는 시간을 측정하는 기능을 추가하기위해, decorator function으로서의 `time_check` function을 구현하고, decorator keyword인 `@`를 활용하는 예제

```python
import time
from functools import wraps

def time_check(func):
    @wraps(func)
    def __wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print('{} execution time : {} sec'.format(func.__name__, round(elapsed, 6)))
        return result
    return __wrapper
```

```python
@time_check
def add(a,b):
    '''To add a and b      
        
       Args:
           a : int or numeric type
           b : int or numeric type
       Returns:
         a + b : int or numeric type
    '''
    return a + b
```

```python
result = add(1,3)
print(result)
print(add.__name__)
print(add.__doc__)
```

```python
add execution time : 1e-06 sec
4
add
To add a and b      
        
       Args:
           a : int or numeric type
           b : int or numeric type
       Returns:
         a + b : int or numeric type
```