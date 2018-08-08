# Object-oriented programming
본 내용은 [양태환](https://github.com/ythwork)님의 저서 **컴퓨터 사이언스 부트캠프 with 파이썬** 을 읽고 요약정리한 내용

* Reference
	+ <https://ko.wikipedia.org/wiki/%ED%95%A8%EC%88%98_(%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)> 
	+ <https://ko.wikipedia.org/wiki/%EC%BA%A1%EC%8A%90%ED%99%94>
	+ <http://cerulean85.tistory.com/149>

## 1. 프로그래밍 패러다임
다양한 프로그래밍 패러다임이 있으나 현재 대표적인 프로그래밍 패러다임으로는 아래의 세 가지가 있다.

* **프로그래밍 패러다임**
	+ 절차지향 프로그래밍(procedural programming)
	+ 객체지향 프로그래밍(object-oriented programming)
	+ 함수형 프로그래밍(functional programming) 

## 2. 절차지향 프로그래밍
절차를 의미하는 **프로시져(procedure)** 는 서브 루틴(subroutine), 메소드(method), 함수(function) 등으로 불리며 ***한번 정의해두면 어디서든 다시 호출해 사용할 수 있다.*** 함수를 작성하는 데에 있어서는 아래와 같은 사항이 중요하다.

* 이름만 봐도 이 함수가 어떤 일을 하는 지 쉽게 알 수 있게 한다.
* 함수를 작성한 사람과 사용하는 사람이 다르다면, 함수를 사용하는 사람의 입장에서 함수의 내부구현은 알 필요없이 사용할 수 있도록 인터페이스를 설계한다.

위와 같은 사항을 잘 지켜서 함수를 작성하면, ***어떤 일을 수행하는 긴 코드를 기능 별로 나누어 함수로 정의하고, 함수 호출을 사용해 코드를 작성하면 다른 프로그래머도 쉽게 프로그램을 이해하고 유지 보수가 가능하다.***

**절차지향 프로그래밍(procedural programming)** 을 간단히 정의하자면 함수를 설계할 때 위와 같은 사항들을 잘 지켜서 ***"이 프로그램은 어떤 일을 하는 가?"*** 에 대한 질문에 쉽게 답할 수 있도록 함수를 사용해 프로그래밍을 하는 것이라 할 수 있다. 

## 3. 절차지향으로 프로그래밍 만들기
예를 들어, 절차지향으로 엑셀에 저장된 학생들의 점수를 가져와 평균과 표준편차를 구하고, 이를 학년 전체 평균과 비교하는 프로그램을 Python을 이용해서 절차지향으로 작성한다고하면 `functions.py` script (module)에 엑셀에 저장된 학생들의 점수를 가져오는 함수, 평균을 구하는 함수, 분산을 구하는 함수 등을 정의해두고, 사용자 프로그램인 `main.py` script에서 `functions.py` script (module)에 정의된 함수들을 불러와 사용할 수 있다. 이 예제에서 사용하는 데이터와 작성된 `functions.py`, `main.py` script는 아래와 같다.

* `class_1.xlsx`
실제로 각 column의 이름에 대한 row는 존재하지 않음.

| name    | score |
|---------|-------|
| greg    | 95    |
| john    | 25    |
| yang    | 50    |
| timothy | 15    |
| melisa  | 100   |
| thor    | 10    |
| elen    | 25    |
| mark    | 80    |
| steve   | 95    |
| anna    | 20    |

* `functions.py`

```python
from openpyxl import load_workbook
from functools import reduce
import math

def get_data_from_excel(filepath):

    wb = load_workbook(filename = filepath)
    ws = wb.active
    rows = ws.rows
    raw_data = {name_cell.value : score_cell.value for name_cell, score_cell in rows}
    scores = raw_data.values()
    return scores

def get_average(scores):
    
    avrg = reduce(lambda score1, score2 : score1 + score2, scores) / len(scores)    
    return avrg

def get_variance(scores, avrg):
    
    tmp = 0
    for score in scores:
        tmp += (score - avrg)**2       
    else:
        var = tmp / len(scores)
    return var

def get_std_dev(var):
    
    std_dev = round(math.sqrt(var),1)    
    return std_dev

def evaluate_class(avrg, var, std_dev, total_avrg, total_std_dev):
    '''
    evaluate_class(avrg, var, std_dev, total_avrg, total_std_dev) -> None
    
    Args:
        avrg : 반평균
        var : 반분산
        std_dev : 반표준편차
        total_avrg : 학년평균
        total_std_dev : 학년분산
    '''
    print("평균:{}, 분산:{}, 표준편차:{}".format(avrg, var, std_dev))
    if avrg < total_avrg and std_dev > total_std_dev:
        print('성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.')
    elif avrg > total_avrg and std_dev > total_std_dev:
        print('성적은 평균 이상이지만 학생들의 실력 차이가 크다. 주의 요망!')
    elif avrg < total_avrg and std_dev < total_std_dev:
        print('학생들의 실력 차이는 크지 않지만 성적이 너무 저조하다. 주의 요망!')
    elif avrg > total_avrg and std_dev < total_std_dev:
        print('성적도 평균 이상이고 학생들의 실력 차이도 크지 않다.')
```

* `main.py`

```python
from functions import *
import argparse 
parser = argparse.ArgumentParser(prog = '평가프로그램',
                                 description = '엑셀에 저장된 학생들의 점수를 가져와 평균과 표준편차를 구하고, 학년 전체 평균과 비교하는 프로그램')
parser.add_argument('filepath', type = str, help = '엑셀파일 저장경로')
parser.add_argument('total_avrg', type = float, help = '학년평균')
parser.add_argument('total_std_dev', type = float, help = '학년표준편차')
args = parser.parse_args()

def main():
    scores = get_data_from_excel(filepath = args.filepath)
    avrg = get_average(scores = scores)
    var =  get_variance(scores = scores, avrg = avrg)
    std_dev = get_std_dev(var = var)
    evaluate_class(avrg, var, std_dev, args.total_avrg, args.total_std_dev)

if __name__ == '__main__':
    main()
```

위에서 보듯이 절차지향으로 프로그래밍을 작성하면, 사용자 프로그램인 `main.py` script에서는 코드가 매우 단순화 된 것을 볼 수 있다. 사용자는 아래처럼 사용하고자하는 프로그램을 실행시키기만하면된다.

```bash
$ python main.py --help
```

```bash
usage: 평가프로그램 [-h] filepath total_avrg total_std_dev

엑셀에 저장된 학생들의 점수를 가져와 평균과 표준편차를 구하고, 학년 전체 평균과 비교하는 프로그램

positional arguments:
  filepath       엑셀파일 저장경로
  total_avrg     학년평균
  total_std_dev  학년표준편차

optional arguments:
  -h, --help     show this help message and exit
```

```bash
$ python main.py ./class_1.xlsx 50 25
```

```python
평균:51.5, 분산:1240.25, 표준편차:35.2
성적은 평균 이상이지만 학생들의 실력 차이가 크다. 주의 요망!
```

## 4. 객체지향 프로그래밍
**객체지향 프로그래밍(object-oriented programming)** 은 ***"현실 세계에 존재하는 객체(object)를 어떻게 모델링(modeling) 할 것인 가?"*** 에 대한 물음에 대한 답이라고 볼 수 있다.

### 4.1 캡슐화
현실 세계의 **객체(object)** 를 구현하기 위해서는 **변수(variable)** 과 **함수(function)** 만 있으면 구현이 가능하다. 왜냐하면 ***객체가 지니는 특성은 변수로 나타낼 수 있고 객체의 행동 혹은 기능은 함수로 표현할 수 있기 때문이다.*** 이처럼 변수와 함수를 가진 객체를 이용하는 패러다임을 **객체지향 프로그래밍(object-oriented programming)** 이라고하며, 변수와 함수를 하나의 단위로 묶어서 구현하는 것과 더불어 구현 내용 일부를 **information hiding** 기법을 이용하여 감추는 데, 이 두 가지를 통칭하여  **캡슐화(encapsulation)**  라고 한다. 대부분의 프로그래밍 언어에서는 이를 **클래스(class)** 를 이용해 구현한다. 이는 Python에서도 마찬가지이다.

### 4.2 클래스를 사용해 객체 만들기 
컴퓨터에서는 객체가 현실 세계의 사물을 모델링한 것이라는 중요한 의미를 모르며, 컴퓨터에게 객체란 그저 메모리의 한 단위일 뿐이다. 객체라는 메모리 공간을 할당한 다음 객체 안에 묶인 변수를 초기화하고 함수를 호출하는데 필요한 것이 **클래스(class)** 일 뿐이다. **클래스(class)** 는 ***객체를 생성해 내는 템플릿이고 객체는 클래스를 이용해 만들어진 변수와 함수를 가진 메모리 공간이며, 둘은 서로 다른 존재이며 메모리 공간도 다르다. 간단하게 정리하자면 아래와 같다.***

* **클래스(class)** : 현실 세계에 존재하는 객체(object)를 구현하는 설계도
	+ in Python
		- 클래스 변수(class variable), 클래스 멤버(class member)라고도 부르는 변수를 정의할 수 있음
			- 인스턴스 모두가 공유하는 동일한 값
			- 인스턴스를 생성하지않고도 클래스만 선언한 상태에서 사용가능
			- oop에서 전역변수(global variable)을 대체하기위하여 사용 
		- 클래스 메소드(class method)를 정의할 수 있음
			- oop에서 전역함수(global function)을 대체하기위해 사용할 때도 있으나, 주로 대체 생성자(constructor)를 만들 때 사용
			- Python에서 oop를 구현할 때, 전역함수(global function)을 대체하기위해서 클래스 메소드보다는 정적 메소드(static method)를 활용하는 것이 더 일반적 
* **인스턴스(instance)** : 클래스(class)라는 설계도로 현실 세계에 존재하는 객체(object)를 메모리공간에 생성해 낸 것
	+ "이 객체는 특정 클래스의 인스턴스"라는 표현이 가능
	+ 메모리 관점에서보면 객체와 인스턴스는 동일
	+ in Python
		- 인스턴스 변수(instance variable), 인스턴스 멤버(instance member)라고도 부르는 변수를 정의할 수 있음
			- 인스턴스마다 값이 다른 변수, 인스턴스가 가지는 고유한 값 (상태) 
		+ 인스턴스 메소드(instance method)를 정의할 수 있음 
			- 메소드 오버라이닝(method overriding)으로 다형성(polymorphism)을 구현할 수 있음

예를 들어, Python으로 간단한 `Person` 클래스를 구현하면 아래와 같다.

```python
class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        
    def give_money(self, other, money):
        other.get_money(money)
        self.money -= money
        
    def get_money(self, money):
        self.money += money
        
    def __str__(self):
        return 'name : {}, money : {}'.format(self.name, self.money)
```

```python
greg = Person('greg', 5000)
john = Person('john', 2000)

print(greg, john)
```

```bash
name : greg, money : 5000 name : john, money : 2000
```

```python
greg.give_money(john, 2000)
print(greg, john)
```

```bash
name : greg, money : 3000 name : john, money : 4000
```
### 4.3 파이썬의 클래스
4.2 절에서 구현한 `Person` class를 아래의 코드를 이용해 분석해보면 `Person.give_money`, `Person.get_money` 모두 각각의 함수를 가리키고 있음을 알 수가 있다.

```python
from pprint import pprint
pprint(Person.__dict__)
print(type(Person.give_money))
print(type(Person.get_money))
```

```bash
mappingproxy({'__dict__': <attribute '__dict__' of 'Person' objects>,
              '__doc__': None,
              '__init__': <function Person.__init__ at 0x10607cc80>,
              '__module__': '__main__',
              '__str__': <function Person.__str__ at 0x10607c840>,
              '__weakref__': <attribute '__weakref__' of 'Person' objects>,
              'get_money': <function Person.get_money at 0x10607cd90>,
              'give_money': <function Person.give_money at 0x10607cea0>})
<class 'function'>
<class 'function'>
```

반면에 `Person` 클래스의 인스턴스인 `greg` 의 `greg.give_money`, `greg.get_money` 는 모두 `method` 이다.  이며 `Person.__dict__` 의 실행결과와는 다르게 `greg.__dict__` 는 인스턴스 변수의 목록을 `dict` 형태로 가지고 있는 **값 객체(value object)** 를 가리킨다.

```python
print(type(greg.give_money))
print(type(greg.get_money))
print(greg.__dict__)
```

```bash
<class 'method'>
<class 'method'>
{'name': 'greg', 'money': 3000}
```

아래 코드의 실행 결과를 보면 결국 `greg.give_money` 는 `Person.give_money` 를 가리키고 있는 함수를 가리키고, `greg.get_money` 역시 `Person.get_money` 가 가리키고 있는 함수를 가리키고 있음을 알 수 있다.

```python
print(hex(id(greg.give_money.__func__)))
print(hex(id(Person.give_money)))
print(greg.give_money.__func__ is Person.give_money)
```

```bash
0x10607cea0
0x10607cea0
True
```

아래의 코드의 실행 결과를 보면 `Person` 클래스에서 각각의 인스턴스 메소드(instance method)를 정의할 때, `self` 인자(argument)가 존재했는 데, `Person` 의 인스턴스인 `greg` 에서 `greg.give_money`, `greg.get_money` 등의 `method` 를 실행할 때는 `self` 인자에 매개변수(parameter)를 명시적으로 전달하지 않는 이유를 알 수 있는데, 그 이유는 ***인스턴스 메소드 내부에 함수와 인스턴스의 자신의 참조를 가지고 있으므로 함수에 직접 인스턴스의 참조를 전달할 수 있기 때문이다.***

```python
print(hex(id(greg.give_money.__self__)))
print(hex(id(greg)))
print(greg.give_money.__self__ is greg)
```

```bash
0x1060a93c8
0x1060a93c8
True
```

위의 결과를 생각해보면 아래와 같은 코드로도 실행할 수 있음을 알 수 있다.

```python
print(greg.__str__())
print(Person.__str__(greg))
```

```bash
name : greg, money : 3000
name : greg, money : 3000
```

위에서 구현한 `Person` 클래스에는 클래스 변수(class variable)과 클래스 메소드(class method)가 없기 때문에 정보은닉을 위한 테크닉 중 하나인 **name mangling** 을 이용하여, `Person` 클래스의 클래스 변수 `__whole_population` 과 클래스 메소드 `__birth` 를 구현하고, **name mangling** 테크닉 없이 `check_population` 클래스 메소드를 구현한다. **name mangling** 테크닉은 클래스 변수이건 인스턴스 변수이건 간에 클래스 정의시 변수명을 `__변수명` 으로 정의하면, 클래스 외부에서 호출하려면 `_클래스명__변수명` 으로 호출할 수 있게 만드는 것을 의미한다. 클래스 변수와 클래스 메소드는 클래스를 요약할 때 상기한 특징 뿐만아니라 ***"인스턴스에서도 접근하거나 호출할 수 있다."*** 는 특징이 있다. (스태틱 메소드(static method)도 해당)

```python
class Person:
    
    # 여기에 class variable (또는 class member)
    # instance 모두가 공유하는 동일한 값
    # instance를 생성하지않고도, class만 선언한 상태에서 호출이 가능하다.
    # oop에서 global variable을 대체하기위하여 사용
    __whole_population = 0 
    # name mangling technique 사용, 외부에서
    ## Person.__whole_population으로 접근 불가
    ## Person._Person__whole_population으로 접근 가능
    
    # class method
    # oop에서 global에 선언된 function을 대체하기위해 사용
    # 대체 생성자를 만들 때, 더 많이씀 (여긴 대체생성자 구현하지 않음)
    @classmethod
    def __birth(cls):
        cls.__whole_population += 1
    
    @staticmethod
    def check_population():
        return Person.__whole_population
    
    # instance method
    def __init__(self, name, money): # 생성자(constructor)
        Person.__birth()
        
        # instance variable (또는 instance member)
        # instance마다 값이 다른 변수, instance가 가지는 고유한 값
        # 여기에서는 self.name, self.age
        self.name = name
        self.money = money

    def get_money(self, money):
        self.money += money
        
    def give_money(self, other, money):
        # message passing
        # 다른 인스턴스(객체)랑 상호작용을 할 때, 상대 인스턴스(객체)의 인스턴스 변수를 바꿔야한다면  
        other.get_money(money) # 이렇게하세요
        # other.money += money 이렇게하지마세요
        self.money -= money
        
    def __str__(self):
        return '{} : {}'.format(self.name, self.money)        
```

```python
# 클래스 메소드는 인스턴스를 생성하지않고도 호출할 수 있다.
print(Person.check_population())
```

```bash
0
```

```python
# 클래스 변수는 인스턴스간에 모두 공유한다.
# 인스턴스를 통해서도 클래스 변수나 클래스 메소드를 호출할 수 있다.
mark = Person('mark', 5000)
greg = Person('greg', 3000)
steve = Person('steve', 2000)

print(Person.check_population())
print(Person._Person__whole_population)
print(mark._Person__whole_population)
print(greg._Person__whole_population)
print(steve._Person__whole_population)

steve._Person__birth()

print(mark._Person__whole_population)
print(greg._Person__whole_population)
print(steve._Person__whole_population)
```

```bash
3
3
3
3
3
4
4
4
```

### 4.4 객체지향으로 은행 입출금 프로그램 만들기
위에 정리한 내용을 바탕으로 계좌 클래스를 구현하면 아래와 같다.

```python
class Account:
    __num_acnt = 0
    
    @staticmethod
    def get_num_acnt():
        return Account.__num_acnt
    
    def __init__(self, name, money):
        self._user = name
        self._balance = money
        
        Account.__num_acnt += 1
        
    def deposit(self, money):
        assert money > 0, '금액이 음수입니다.'
        self._balance += money
    
    def withdraw(self, money):
        assert money > 0, '금액이 음수입니다.'

        if self._balance >= money:
            self._balance -= money
        else:
            pass

    def transfer(self, other, money):
        assert money > 0, '금액이 음수입니다.'
        self.withdraw(money)
        if self._balance >= 0:
            other.deposit(money)
            return True
        else:
            return False
        
    def __str__(self):
        return 'user : {}, balance :{}'.format(self._user, self._balance)
```

```python
print(Account.get_num_acnt())
aisolab = Account(name = 'aisolab', money = 10000)
modulab = Account(name = 'modulab', money = 5000)
print(Account.get_num_acnt())
```

```bash
0
2
```

```python
aisolab.deposit(2000)
print(aisolab)
aisolab.withdraw(1000)
print(aisolab)
```

```bash
user : aisolab, balance :12000
user : aisolab, balance :11000
```

```python
aisolab.transfer(modulab, 1000)
print(aisolab)
print(modulab)
```

```bash
user : aisolab, balance :10000
user : modulab, balance :6000
```

### 4.5 정보 은닉

## 5. 객체지향으로 다시 만드는 학급 성적 평가 프로그램