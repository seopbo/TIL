# How to use abstract class
Python에서 클래스(class)간의 관계를 정의할 때, 자식 클래스가 부모 클래스를 상속하는 경우 부모 클래스의 메소드를 무조건 **메소드 오버라이딩(method overriding)** 을 하게하고, 부모 클래스로부터 인스턴스(instance)를 생성못하게 하고 싶은 경우가 있다. 이 경우 **추상 클래스(abstract class)** 로 부모 클래스를 정의하고, 메소드를 정의할 시 `@abstractmethod`, `@abstractclassmethod` 등의 decorator를 활용한다.

### Template
Python에서 추상 클래스를 정의할 시, `abc` module에서 `ABCMeta`, `abstractmethod`, `abstractclassmethod` 등을 가져와서 아래와 같이 사용한다. 
보통 아래의 형태로 추상 클래스를 정의하며, `@abstractclassmethod` 와 `@abstractmethod` decorator로 꾸며진 메소드가 상속하는 자식 클래스에서 하나라도 재정의되지않으면, 추상 클래스로 취급되어 자식 클래스도 인스턴스를 생성할 수 없다.

```python
from abc import ABCMeta, abstractmethod, abstractclassmethod
class AbstractClass(metaclass = ABCMeta):
    
    @abstractclassmethod
    def class_method(cls):
        pass
    
    @abstractmethod
    def instance_method(self):
        pass
```

```python
try:
    test = AbstractClass()
except TypeError as e:
    print(e)
```

```bash
Can't instantiate abstract class AbstractClass with abstract methods class_method, instance_method
```

### Example : Animal class
`Animal` 클래스를 추상 클래스로 정의하고, `Lion` , `Deer`, `Human` 클래스 등이 상속하는 예제

```python
from abc import ABCMeta, abstractmethod, abstractclassmethod

class Animal(metaclass = ABCMeta):
    
    def die(self):
        print('time to die')
        
    @abstractmethod # 자식클래스에서 반드시 재정의해야한다. 
    def eat(self):  # abstract instance method
        pass
```

```python
class Lion(Animal):
    def eat(self):
        print('eat meat')
        
class Deer(Animal):
    def eat(self):
        print('eat grass')
        
class Human(Animal):
    def eat(self):
        print('eat meat and grass')
```

```python
animals = []
lion = Lion()
deer = Deer()
human = Human()

animals.append(lion)
animals.append(deer)
animals.append(human)

for animal in animals:
    animal.eat()
    animal.die()
```


```bash
eat meat
time to die
eat grass
time to die
eat meat and grass
time to die
```