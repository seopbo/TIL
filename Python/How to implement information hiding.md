# How to implement information hiding
Python에서 **객체지향 프로그래밍(object-oriented programming, oop)** 으로 프로그램을 작성 시, value object와 function object를 하나의 단위로 묶고, 더불어 구현 내용 중 일부를  감추는 **정보 은닉(information hiding)** 을 하는 **캡슐화(encapsulation)** 를 `class` 를 이용해서 구현하나, 정보 은닉을 위해서 C++에서 `public` , `pricate` 등의 접근 제어 지시자(access modifier)를 지원하는 반면에 Python에서는 애초에 정보 은닉을 지원하지 않는다. Python에서 정보 은닉을 비슷하게 구현하기위해서 아래 의 세 가지 정도를 활용한다.

* Reference
	+ <https://hashcode.co.kr/questions/383/%EC%9D%B4%EB%A6%84-%EC%95%9E%EC%97%90-_%EB%B0%91%EC%A4%84%EC%B3%90%EC%A0%B8-%EC%9E%88%EB%8A%94-%EA%B0%9D%EC%B2%B4%EB%8A%94-%EB%AD%94%EA%B0%80%EC%9A%94> 

### Summary
* **`_` 를 사용** 
  + class variable, class method, instance variable, instance method 등을 정의 시, `_` 를 variable명 또는 method명에 붙여 정의함으로써 private임을 명시,**프로그래머 간에 수정하지않는 variable 또는 method라고 약속, class 외부에서 접근하기 힘들게함**
* **name mangling**
  + class variable, class method, instance variable, instance method 등을 정의 시, `__` 를 variable명 또는 method명에 붙여 정의
  + class 내부에서는 `__variable명` 또는 `__method명` 으로 접근 가능하나 class 외부에서는 `_class명__variable명`, `__class명__method명` 으로만 접근이 가능
* **property 기법**
  + `@property` decorator를 활용하는 방법으로 `@property` decorator를 이용하면 instance variable, class variable을 호출하는 것 같지만 실제로는 instance method, class method를 호출하도록 만들 수 있다.

### Example : Account class
`Account` class를 **Summary**에 기술한 세 가지 방법 중 `_` 을 사용하는 경우는 사실상 프로그래머간의 약속이므로 예제에서 제외하고, **name mangling** , **property 기법** 을 사용하는 예제를 보면 아래와 같다.

* **name mangling**

```python
class Account:
    def __init__(self, name, money):
        self.__name = name
        self.__balance = money
        
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, new_bal):
        if new_bal < 0:
            return
        self.__balance = new_bal
        
aisolab = Account(name = 'aisolab', money = 5000)
print(aisolab.__dict__)
```

```bash
{'_Account__name': 'aisolab', '_Account__balance': 5000}
```

```python
# 잔고를 음수를 설정할 수 없다.
aisolab.__balance = -5000
print(aisolab.__dict__)
print(aisolab._Account__balance)

aisolab.set_balance(-7000)
print(aisolab.__dict__)

# 완벽한 정보은닉이 아니기 때문에 실제 외부에서 접근할 수 있는 이름을 알면 설정할 수 있다.
aisolab._Account__balance = -5000
print(aisolab.__dict__)
```

```bash
{'_Account__name': 'aisolab', '_Account__balance': 5000, '__balance': -5000}
5000
{'_Account__name': 'aisolab', '_Account__balance': 5000, '__balance': -5000}
{'_Account__name': 'aisolab', '_Account__balance': -5000, '__balance': -5000}
```

* **property 기법**

```python
class Account:
    def __init__(self, name, money):
        self.__name = name
        self.balance = money

    @property
    def balance(self): # getter function
        return self.get_balance()
    
    @balance.setter
    def balance(self, new_bal): # setter function
        self.set_balance(new_bal)
    
    def get_balance(self): # original getter function
        return self.__balance
    
    def set_balance(self, new_bal): # original setter function
        if new_bal < 0:
            pass
        else:
            self.__balance = new_bal
            
aisolab = Account(name = 'aisolab', money = 5000)
print(aisolab.__dict__)
```

```bash
{'_Account__name': 'aisolab', '_Account__balance': 5000}
```

```python
# 인스턴스 변수에 접근한 것 같지만 사실은 @property가 적용된
# balance()가 실행되어 return 값을 본 것
print(aisolab.balance)
```

```bash
5000
```

```python
# 인스턴스 변수를 직접 수정한 것 같지만 @blance.setter가 적용된 blance()가 실행된 것 
aisolab.balance = -20
print(aisolab.get_balance())

aisolab.balance = 50
print(aisolab.get_balance())
```

```python
5000
50
```

```python
# 완벽한 정보은닉이 아니기 때문에 실제 외부에서 접근할 수 있는 이름을 알면 설정할 수 있다.
aisolab._Account__balance = -5000
print(aisolab.__dict__)
print(aisolab.get_balance())
```

```bash
{'_Account__name': 'aisolab', '_Account__balance': -5000}
-5000
```
