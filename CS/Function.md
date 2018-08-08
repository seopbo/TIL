# Function
본 내용은 [양태환](https://github.com/ythwork)님의 저서 **컴퓨터 사이언스 부트캠프 with 파이썬** 을 읽고 요약정리한 내용

* Reference
	+ <https://en.wikipedia.org/wiki/Call_stack#STACK-FRAME> 
	+ <https://en.wikipedia.org/wiki/Namespace> 
	+ <http://tcpschool.com/c/c_memory_stackframe>
	+ <https://item4.github.io/2015-07-18/Some-Ambiguousness-in-Python-Tutorial-Call-by-What/>

## 1. 함수를 시작하기 전에
### 1.1 자료 구조 미리 엿보기
**함수(function)** 정의된 이후 **호출(call)** 될 때, **스택 프레임(stack frame)** 이라는 함수 내부에서 생성되는 **지역변수(local variable)** 가 저장되는 메모리 공간이 생기는데, 이름에서 보듯이 자료구조의 **스택(stack)** 과 매우 유사하게 작동한다.  
주의 해야할 점은 위의 이야기는 Python에서는 거의 유사하나 조금 다르게 동작한다. 그 이유는 Python은 **변수(variable)** 는 그저 이름일 뿐이고, 실제로는 다른 메모리 공간에 저장된 **값 객체(value object)** 를 가리킬 뿐이기 때문이다. 일반적으로 다른 언어에서는 변수 자체가 메모리 공간이다.

### 1.2 전역변수와 지역변수
* **전역변수(global variable)** : ***전체 영역에서 접근할 수 있는 변수*** 로 변수에 값을 할당함과 동시에 (Python에서는 변수가 값 객체를 가리킴과 동시에) **글로벌 프레임(global frame)** 에 할당된다.
* **지역변수(local variable)** : ***함수 내부에서 접근할 수 있는 변수*** 로 함수가 호출됨과 동시에 함수의 이름을 **namespace** 으로하는 스택 프레임에 할당된다. ***지역 변수는 함수 외부에서는 접근할 수 없고 함수가 호출될 때 생성되었다가 호출이 끝나면 사라진다.***

Python에서는 아래의 코드로 확인이 가능하다. 아래의 코드에 대한 글로벌 프레임과 스택 프레임의 모습을 아래를 클릭하여 확인할 수 있다. 물론 Python에서의 동작이라는 점을 감안한다.

[아래의 예시에 대한 동작 확인](http://pythontutor.com/visualize.html#code=g_var%20%3D%2010%0Adef%20func%28%29%3A%0A%20%20%20%20g_var%20%3D%2020%0A%20%20%20%20print%28'g_var%20%3D%20%7B%7D%20in%20function'.format%28g_var%29%29%0A%20%20%20%20%0Afunc%28%29%0Aprint%28'g_var%20%3D%20%7B%7D%20in%20main'.format%28g_var%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
g_var = 10
def func():
    g_var = 20
    print('g_var = {} in function'.format(g_var))
    
func()
print('g_var = {} in main'.format(g_var))
```

```bash
g_var = 20 in function
g_var = 10 in main
```

함수 내부에서 전역변수에 접근하는 것은 가능하나 수정하는 것은 불가능하다. 만약 함수 내부에서 전역변수를 수정하고 싶다면, Python에서는 `global` 키워드를 활용한다. 아래의 코드로 확인가능하다.

[아래의 예시에 대한 동작 확인](http://pythontutor.com/visualize.html#code=g_var%20%3D%2010%0Adef%20func%28%29%3A%0A%20%20%20%20%23%20global%20variable%20g_var%EC%9D%84%20%ED%95%A8%EC%9C%BC%EB%A1%9C%EC%8D%A8%20%ED%95%A8%EC%88%98%20%EB%82%B4%EB%B6%80%EC%97%90%EC%84%9C%20%0A%20%20%20%20%23%20global%20variable%20g_var%EC%9D%98%20%EC%9D%B4%EB%A6%84%EC%9D%84%20%EC%82%AC%EC%9A%A9%ED%95%A0%20%EC%88%98%20%EC%9E%88%EA%B3%A0%0A%20%20%20%20%23%20g_var%EB%A1%9C%20%EC%83%88%EB%A1%AD%EA%B2%8C%20%EC%83%9D%EC%84%B1%EB%90%9C%20%EA%B0%92%20%EA%B0%9D%EC%B2%B4%2020%EC%9D%84%20%EA%B0%80%EB%A6%AC%ED%82%B4%0A%20%20%20%20global%20g_var%0A%20%20%20%20g_var%20%3D%2020%0A%20%20%20%20print%28'g_var%20%3D%20%7B%7D%20in%20function'.format%28g_var%29%29%0A%20%20%20%20%0Afunc%28%29%0Aprint%28'g_var%20%3D%20%7B%7D%20in%20main'.format%28g_var%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
g_var = 10
def func():
    # global variable g_var을 함으로써 함수 내부에서 
    # global variable g_var의 이름을 사용할 수 있고
    # g_var로 새롭게 생성된 값 객체 20을 가리킴
    global g_var
    g_var = 20 
    print('g_var = {} in function'.format(g_var))
    
func()
print('g_var = {} in main'.format(g_var))
```

```bash
g_var = 20 in function
g_var = 20 in main
```

또 살펴 볼 것은 ***함수(외부 함수) 내부에 함수(내부 함수)가 정의된 경우, 내부 함수가 아닌 외부 함수에 정의된 변수는 전역변수도 아니고, 내부 함수의 지역변수도 아니다.*** 이러한 경우를 통칭하여 **non-local variable** 이라고 칭한다. 이는 Python에서의 네이밍이며 다른 언어에서는 다른 이름일 수 있다. 아래의 코드로 확인가능하다.

[아래의 예시에 대한 동작 확인](http://pythontutor.com/visualize.html#code=a%20%3D%2010%20%23%20global%0Adef%20outer%28%29%3A%0A%20%20%20%20b%20%3D%2020%20%23%20non-local%0A%20%20%20%20def%20inner%28%29%3A%0A%20%20%20%20%20%20%20%20c%20%3D%2030%20%23%20non-local%0A%20%20%20%20%20%20%20%20def%20deeper%28%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20d%20%3D%2040%20%23%20local%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28a,%20b,%20c,%20d%29%0A%20%20%20%20%20%20%20%20deeper%28%29%0A%20%20%20%20inner%28%29%0A%20%20%20%20%0Aouter%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
a = 10 # global
def outer():
    b = 20 # non-local
    def inner():
        c = 30 # non-local
        def deeper():
            d = 40 # local
            print(a, b, c, d)
        deeper()
    inner()
    
outer()
```

```bash
10 20 30 40
```

위의 코드에서 보면 `outer` 함수 내부에 정의된 `inner` 함수, `inner` 함수 내부에 정의된 `deeper` 함수의 입장에서 변수 `b`, 변수 `c` 전역변수가 아니고 non-local variable이며, `deeper` 함수 내부에서 변수 `b`와 변수 `c`를 수정하려면 `nonlocal` 키워드를 활용한다. 아래의 코드로 확인가능하다.

[아래의 예시에 대한 동작 확인](http://pythontutor.com/visualize.html#code=a%20%3D%2010%20%23%20global%0Adef%20outer%28%29%3A%0A%20%20%20%20b%20%3D%2020%20%23%20non-local%0A%20%20%20%20def%20inner%28%29%3A%0A%20%20%20%20%20%20%20%20c%20%3D%2030%20%23%20non-local%0A%20%20%20%20%20%20%20%20def%20deeper%28%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20nonlocal%20b,%20c%0A%20%20%20%20%20%20%20%20%20%20%20%20b%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20c%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20d%20%3D%2040%20%23%20local%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28a,%20b,%20c,%20d%29%0A%20%20%20%20%20%20%20%20deeper%28%29%0A%20%20%20%20inner%28%29%0A%20%20%20%20%0Aouter%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

```python
a = 10 # global
def outer():
    b = 20 # non-local
    def inner():
        c = 30 # non-local
        def deeper():
            nonlocal b, c
            b += 1
            c += 1
            d = 40 # local
            print(a, b, c, d)
        deeper()
    inner()
    
outer()
```

```bash
10 21 31 40
```

## 2. 인자 전달 방식에 따른 분류
함수는 **인자(argument)** 에 **매개변수(parameter)** 를 전달하는 방식에 크게 **값에 의한 전달(call by value)** , **참조에 의한 전달(call by reference)** 등으로 나뉜다. Python에서는 변수는 이름일 뿐이고 그 저 **값 객체(value object)** 를 가리킨다는 특징이 있어서, 함수의 인자에 매개변수를 전달하는 방식이 위의 두 가지가 아닌 **객체 참조에 의한 전달(call by object reference)** 를 따른다. 이는 **call by assignment** 라고도 불린다.

### 2.1 값에 의한 전달
아래의 C++ 코드의 실행결과를 보면, **값에 의한 전달(call by value)** 가 이루어지고 있음을 알 수 있다. `main` 함수가 호출되어 스택 프레임이 쌓이는 과정을 기술해보면, `main` 함수의 스택 프레임의 변수 x에 10이 할당되고, 이후 `change_value` 함수가 호출되면서 `change_value` 함수의 스택 프레임의 변수  val에는 20이 할당된다. 그 다음 `change_value` 함수의 스택 프레임의 변수 x에 10이 할당된다. ***그 이후 `change_value` 함수 내부에 `x = val;` 코드가 실행되면서 `change_value` 함수의 스택 프레임의 변수 val에 담긴 값만 복사하여 `change_value` 함수의 스택 프레임의 변수 x에 할당한다.*** `change_value` 함수가 실행을 마치면 `change_value` 함수의 스택프레임을 반환하기 때문에, 아래와 같은 출력결과가 나온다.

[아래의 코드에 대한 동작 확인](http://pythontutor.com/visualize.html#code=%23include%20%3Cstdio.h%3E%0A%0Avoid%20change_value%28int%20x,%20int%20val%29%20%7B%0A%20%20%20%20x%20%3D%20val%3B%0A%20%20%20%20printf%28%22x%20%3A%20%25d%20in%20change_value%20%5Cn%22,%20x%29%3B%0A%7D%0A%0Aint%20main%28void%29%20%7B%0A%20%20%20%20int%20x%20%3D%2010%3B%0A%20%20%20%20change_value%28x,%2020%29%3B%0A%20%20%20%20printf%28%22x%20%3A%20%25d%20in%20main%20%5Cn%22,%20x%29%3B%0A%7D&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=cpp&rawInputLstJSON=%5B%5D&textReferences=false)

```cpp
#include <stdio.h>

void change_value(int x, int val) {
	x = val;
	printf("x : %d in change_value \n", x);
}

int main(void) {
	int x = 10;
	change_value(x, 20);
	printf("x : %d in main \n", x);
}
```

```bash
x : 20 in change_value
x : 10 in main
```

### 2.2 참조에 의한 전달
아래의 C++ 코드의 실행결과를 보면, **참조에 의한 전달(call by reference)** 가 이루어지고 있음을 알 수 있다. `main` 함수가 호출되어 스택 프레임이 쌓이는 과정을 기술해보면, `main` 함수의 스택 프레임의 변수 x에 10이 할당되고,  `change_value` 함수가 호출되면서 `change_value` 함수의 스택 프레임의 변수  val에는 20이 할당된다. 그 다음 인자에 매개변수로  `&x` 를 전달하는데 이는 `main` 함수의 스택 프레임의 변수 x의 첫 번째 바이트 주소값을 전달한다는 의미이며, 고로 `change_value` 함수의 스택 프레임의 변수 x에 이 주소값이 할당된다. (`change_value` 함수의 스택 프레임의 변수 x가 `main` 함수의 스택 프레임의 변수 x를 가리키는 상태 ) 다음 `change_value` 함수의 내부에서 `*x = val` 실행되므로, `main` 함수의 스택 프레임의 변수 x에 `change_value` 함수의 스택 프레임의 변수  val에 담긴 값 20을 복사하여 할당한다. `change_value` 함수가 실행을 마치면 `change_value` 함수의 스택프레임을 반환하기 때문에, 아래와 같은 출력결과가 나온다.

[아래의 코드에 대한 동작 확인](http://pythontutor.com/visualize.html#code=%23include%20%3Cstdio.h%3E%0A%0Avoid%20change_value%28int%20*%20x,%20int%20val%29%20%7B%0A%20%20%20%20*x%20%3D%20val%3B%0A%20%20%20%20printf%28%22x%20%3A%20%25d%20in%20change_value%20%5Cn%22,%20*x%29%3B%0A%7D%0A%0Aint%20main%28void%29%20%7B%0A%20%20%20%20int%20x%20%3D%2010%3B%0A%20%20%20%20change_value%28%26x,%2020%29%3B%0A%20%20%20%20printf%28%22x%20%3A%20%25d%20in%20main%20%5Cn%22,%20x%29%3B%0A%7D&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=cpp&rawInputLstJSON=%5B%5D&textReferences=false)

```cpp
#include <stdio.h>

void change_value(int * x, int val) {
	*x = val;
	printf("x : %d in change_value \n", *x);
}

int main(void) {
	int x = 10;
	change_value(&x, 20);
	printf("x : %d in main \n", x);
}
```

```bash
x : 20 in change_value
x : 20 in main
```

### 2.3 객체 참조에 의한 전달
**객체 참조에 의한 전달(call by object reference)** 는 Python에서 함수의 인자에 매개변수를 전달하는 방식으로 사실은 Python의 변수는 그저 이름을 뿐이며, 변수는 **값 객체(value object)** 를 가리킨다는 사실만 상기하고 있으면, 매우 이해하기 쉽다. 그렇기 때문에 값 객체의 특성을 이해하는 것이 중요하며, Python에서 값 객체는 **immutable**과 **mutable** 의 두 종류가 있으며 아래와 같다.

* **immutable**
	+ number(int, float), str, tuple
* **mutable**
	+ list, dictionary, set

**immutable** 한 값 객체는 ***변경 또는 수정할 수 없으며, 변경 또는 수정하는 것처럼 보이는 경우는 항상 새로운 값 객체를 생성하여 가리키는 것일 뿐이다.*** 아래의 코드로 확인할 수 있다.

* number(int, float)

```python
a = 1
b = 1
print('a : {}, b : {}'.format(hex(id(a)), hex(id(b))))

a +=1 
print('a : {}'.format(hex(id(a))))
```

```bash
a : 0x10e29b210, b : 0x10e29b210
a : 0x10e29b230
```

* str

```python
a = 's'
b = 's'
print('a : {}, b : {}'.format(hex(id(a)), hex(id(b))))

a += 'f'
print('a : {}'.format(hex(id(a))))
```

```bash
a : 0x10cde1ca8, b : 0x10cde1ca8
a : 0x10ef446c0
```

* tuple
sequence type인 튜플은 각각 element가 가리키는 값 객체가 같아도 하나로 묶어서 튜플을 생성할 때 서로 다른 값 객체로 생성된다.

```python
a = 1,2
b = 1,2
print('b[0] : {}, b[1] : {}'.format(hex(id(b[0])), hex(id(b[1]))))
print('a[0] : {}, a[1] : {}'.format(hex(id(a[0])), hex(id(a[1]))))
print('a : {}, b : {}'.format(hex(id(a)), hex(id(b))))
```

```bash
b[0] : 0x10e2b2210, b[1] : 0x10e2b2230
a[0] : 0x10e2b2210, a[1] : 0x10e2b2230
a : 0x11045c788, b : 0x11045fc48
```

**mutable** 한 값 객체는 ***변경 또는 수정이 가능하므로, 이미 가리키고 있는 값 객체가 변한다.*** 아래의 코드로 확인할 수 있다.

* list

```python
a = [1,2]
b = [1,2]
print('a[0] : {}, a[1] : {}'.format(hex(id(a[0])), hex(id(a[1]))))
print('b[0] : {}, b[1] : {}'.format(hex(id(b[0])), hex(id(b[1]))))
print('a : {}, b : {}'.format(hex(id(a)), hex(id(b))))

a[0] += 2
print('a[0]: {}'.format(hex(id(a[0]))))
print('a : {}'.format(hex(id(a))))
```

```bash
a[0] : 0x1034dc210, a[1] : 0x1034dc230
b[0] : 0x1034dc210, b[1] : 0x1034dc230
a : 0x105841508, b : 0x1058414c8
a[0]: 0x1034dc250
a : 0x105841508
```

* dictionary

```python
a = dict(a = 1, b = 2)
b = dict(a = 1, b = 2)

print('a["a"] : {}, a["b"] : {}'.format(hex(id(a.get('a'))),hex(id(a.get('b')))))
print('b["a"] : {}, b["b"] : {}'.format(hex(id(b.get('a'))),hex(id(b.get('b')))))
print('a : {}, b : {}'.format(hex(id(a)), hex(id(b))))

a.update({'c' : 3})
print('a : {}'.format(hex(id(a))))
```

```bash
a["a"] : 0x101236210, a["b"] : 0x101236230
b["a"] : 0x101236210, b["b"] : 0x101236230
a : 0x10357b5a0, b : 0x10357b3f0
a : 0x10357b5a0
```

* set

```python
a = set([1,2,3])
print(a)
print('a : {}'.format(hex(id(a))))

a.update([3,4])
print(a)
print('a : {}'.format(hex(id(a))))
```

```bash
{1, 2, 3}
a : 0x1035814a8
{1, 2, 3, 4}
a : 0x1035814a8
```

Python에서 함수를 호출할 때, **객체참조에 의한 전달**로 함수의 인자에 매개변수를 전달하는 방식은 ***결국 인자에 어떤 값 객체를 전달하느냐에 따라 동작방식이 다르며*** , 코드를 통해서 확인하면 아래와 같다. 

* **immutable** 한 값 객체를 함수의 인자에 전달하는 경우
아래의 예제를 분석해보면, `global frame` 에 `global variable x` 가 생기고, 이 `global variable x` 가 메모리공간에 저장된 **immutable** 한 값 객체 `10` 을 가리킨다. `change_value` 함수가 호출되면 `change_value` 함수명을 이름으로하는 `stack frame` 에 `local variable value` 가 형성되고, 메모리공간에 저장된 **immutable** 한 값 객체 `20` 을 가리킨다. 바로 이어서 `local variable x` 가 형성되고, 메모리공간에 저장된 **immutable** 값 객체 `10` 을 가리킨다. `change_value` 함수 내부의 코드 `x = value` 가 실행되면서  `local variable value` 가 가리키고 있는 **immutable** 한 값 객체 `20` 을 `local variable x` 도  같이 가리킨다. 그 후 함수가 종료되면 `stack frame` 을 반환한다. `global variable x` 는 여전히 **immutable** 한 값 객체 `10` 을 가리키고 있기 때문에, 출력 결과는 아래와 같다.

```python
def change_value(x, value):
    x = value
    print('x : {} in function'.format(x))
    
if __name__ == '__main__':
    x = 10
    change_value(x, 20)
    print('x : {} in main'.format(x))
```

```bash
x : 20 in function
x : 10 in main
```

* **mutable** 한 값 객체를 함수의 인자에 전달할 경우
아래의 예제를 분석해보면, `global frame` 에 할당된  `global variable li` 는 메모리공간에 저장된 **mutable** 한 값 객체 `[0,1,2,3]` 을 가리킨다. `func` 함수가 호출되면 `func` 함수명을 이름으로하는 `stack frame` 에 `local variable li` 가 형성되고, 이는 `global variable li` 가 가리키는 **mutable** 한 값 객체 `[0,1,2,3]` 을 가리킨다. 동일한 값 객체를 `local variable li` , `global variablie li` 가 가리키고 있지만 **mutable** 한 값 객체이기 때문에, **global** 키워드가 없어도 `func` 함수 내부에서 수정이 가능하다. 함수 실행이 완료되면 `stack frame` 을 반환한다. `global variable li` 가 `func` 함수 내부에서 `li[0] = Talk is cheap. Show me the code.` 이 실행되어 수정된 값 객체 `li = ['Talk is cheap. Show me the code,1,2,3]` 을 가리키게 되기 때문에, 아래와 같은 출력이 나온다.


```python
def func(li):
    li[0] = 'Talk is cheap. Show me the code.'
    print('{} in function'.format(li))
    
if __name__ == '__main__':
    li = [0,1,2,3]
    func(li)
    print('{} in main'.format(li))
```

```bash
['Talk is cheap. Show me the code.', 1, 2, 3] in function
['Talk is cheap. Show me the code.', 1, 2, 3] in main
```
