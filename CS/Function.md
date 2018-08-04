# Function
본 내용은 [양태환](https://github.com/ythwork)님의 저서 **컴퓨터 사이언스 부트캠프 with 파이썬** 을 읽고 요약정리한 내용

* Reference
	+ <https://en.wikipedia.org/wiki/Call_stack#STACK-FRAME> 
	+ <https://en.wikipedia.org/wiki/Namespace> 
	+ <http://tcpschool.com/c/c_memory_stackframe>

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
