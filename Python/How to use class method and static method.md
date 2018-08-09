# How to use class method and static method
Python에서 **객체지향 프로그래밍(object-oriented programming, oop)** 을 구현하기위하여 `class` 를 활용할 때, class method와 static method를 활용하는 방법에 대하여 정리

* **class method**
  + Python에서 `@classmethod` decorator를 이용하여 활용
  + Python에서 oop를 구현할 때 전역함수(global function)를 대체하기위해 사용할 때도 있지만, ***Python에서는 주로 `__init__` 생성자(constructor)를 만들 때 활용*** , Python에서의 type은 `method`
  + ***class variable과 마찬가지로 instance를 생성하지않고도 호출할 수 있으며, instance에서도 접근하거나 호출 할 수 있다.***

* **static method**
  + Python에서 `@staticmethod` decorator를 이용하여 활용
  + Python에서 oop를 구현할 때 전역함수(global function)를 대체하기위해 활용, Python에서 type은 `function`
  + ***class variable, class method 마찬가지로 instance를 생성하지않고도 호출할 수 있으며, instance에서도 접근하거나 호출 할 수 있다.***

### Template
Python에서 oop를 구현할 때, `@classmethod` `@staticmethod` decorator를 활용하는 것은 크게 아래의 형태를 벗어나지 않는다. `@classmethod` decorator를 이용하여 class method를 정의할 시, class method의 type은 `method` 이기 때문에 class 자기 자신에 대한 참조를 가지고 있다. 그리하여 class method 정의 시 첫 번째 argument는 `cls` 를 통상적으로 활용한다. (instance method 정의 시 첫 번째 argument로 통상적으로 `self` 를 쓰는 것과 같음)

`@staticmethod` decorator를 이용하여 static method를 정의할 시, static method의 type은 `function` 이다. 이 때 argument를 비워놓거나 argument에 parameter로 instance, class를 전달하지 않는 것이 중요한 점이다. (단지 `class` 로 정의된 class 명의 namespace에 있을 뿐, 일반적인 전역함수와 같다.)

```python
class Base:
    @staticmethod 
    def f():
        pass
        
    @classmethod
    def g(cls):
        pass
        
    # 이 밑에 instance method 들을 정의하거나 method overriding
```

```python
print(type(Base.f))
print(type(Base.g))
```

```bash
<class 'function'>
<class 'method'>
```

### Example : Person class

`Person` class에 `__init__` instance method 대신 다른 생성자(constructor)를 `@classmethod` 를 이용하여 class method `init_from_string` 를 정의하는 예제


```python
class Person:
    
    __whole_population = 0
    
    @staticmethod
    def check_population(language):
        assert language in ['kor', 'eng']
        if language == 'kor':
            return '현재 인구는 {}명 입니다.'.format(Person.__whole_population)
        else:
            return 'The population is {}'.format(Person.__whole_population)
    
    @classmethod
    def init_from_string(cls, string):
        '''
        string format --> <name>_<age>
        '''
        name, age = string.split('_')
        age = int(age)
        return cls(name = name, age = age)
    
    @classmethod
    def __birth(cls):
        cls.__whole_population += 1
        
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.__birth()
        
    def __str__(self):
        return '{} : {}'.format(self.name, self.age)
```

```python
string_list = ['greg_36', 'mark_24', 'john_12']
instances = [Person.init_from_string(string) for string in string_list]
greg, mark, john = instances

print(greg)
print(mark)
print(john)
print(Person.check_population(language='kor'))
```

```bash
greg : 36
mark : 24
john : 12
현재 인구는 3명 입니다.
```