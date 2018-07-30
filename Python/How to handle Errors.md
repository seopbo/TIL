# How to handle Errors
`ValueError`, `FileNotFoundError`, `NameError`, `IndexError` 등등 여러가지 Error를  `try / except` 구문을 이용하여 처리하는 방법에 대해서 정리, 아래의 Reference를 참고함

* Reference
	+ <https://wayhome25.github.io/python/2017/02/26/py-12-exception/>

### try / except 기본 
`try / except` 구문은 아래와 같이 두 가지 경우에 대하여 사용할 수 있다.
*  어떤 Error가 발생할 지 아는 경우
*  어떤 Error가 발생할 지 모르는 경우

또한 `try / except` 구문 자체를 아래의 두 가지 형태로 활용할 수 있으며, 주로 ***usage 1의 형태가 usage 2의 형태보다 자주 활용된다.*** 목적에 맞게 활용하면 usage 2의 형태도 쓸모가 있다. 

#### usage 1
```python
try:
	# error가 발생할 것 같은 code
except: # except 뒤에 Error 종류 명시 가능
	# error가 발생했을 시 실행할 code
```

#### usage 2
```python
try:
	# error가 발생할 것 같은 code
except: # except 뒤에 Error 종류 명시 가능
	# error가 발생했을 시 실행할 code
else:
	# try문 안의 code 대신 실행되면, 바로 이어서 실행할 code
```

### try / except 활용
#### 어떤 Error가 발생할 지 아는 경우
어떤 Error가 발생할 지 아는 경우에도 위와 같이 Error 종류를 명시하지않고 활용할 수 있으나, Error 종류를 알고 있다면 명시적으로 선언하고 아래의 예와 같이 활용한다.

```python
# ZeroDivisionError가 발생되는 예제
foo, bar = 1, 0

try:
	result = foo / bar # ZeroDivisionError가 발생할 것이라는 것을 알고 있으므로
except ZeroDivisionError as e: # e 변수로 해당 Error 발생 시 출력하는 Error message을 받아옴
	print('0으로 나눴습니다.') # Error 발생 시 실행할 코드
	print(e) # Error 발생 시 실행할 코드, ZeroDivisionError 발생 시 나오는 Error message를 출력
```

```python
0으로 나눴습니다.
division by zero
```

#### 어떤 Error가 발생할 지 모르는 경우
어떤 Error가 발생할 지 모르는 경우에도 위와 같이 Error 종류를 명시하지않고 활용할 수 있으나, `Exception`을 활용하고, 이를 variable로 받아서 Error message를 출력하는 형태로 활용한다.

```python
# NameError가 발생되는 예제
a = 1

try:
	print(b)
except Exception as e:
    print(e)
```

```python
name `b` is not defined
```
