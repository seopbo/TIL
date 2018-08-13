# Class
본 내용은 [양태환](https://github.com/ythwork)님의 저서 **컴퓨터 사이언스 부트캠프 with 파이썬** 을 읽고 요약정리한 내용

* Reference
	+ <http://sonsooresoon.tistory.com/entry/Aggregation-%EA%B3%BC-Composition-%EC%9D%98-%EC%B0%A8%EC%9D%B4> 

## 1. 클래스 관계
**클래스(class)** 를 설계하다보면 클래스와 클래스 사이가 어떤 관계를 형성하는 것을 볼 수 있으며, 관계를 나타내는 방법으로 **IS-A** 와 **HAS-A** 있다. 두 가지를 짧게 요약하자면 아래와 같다.

* **IS-A**
	+ **Inheritance** 
	+ **자식 클래스(child, derived, sub)** 가 **부모 클래스(super, base, parent)**의 모든 instance variable(instance member), instance method, class variable(class member), class method를 가질 때
	+ ***위의 모든 variable 또는 method를 덮어쓰거나 유지하면서 다른 것을 추가해야할 때 (Polymorphism)***
* **HAS-A**
	+ **Composition**
		- 클래스 간 강한 연관관계(strong coupling)를 가지고, 같은 생명 주기(same life cycle)를 가질 때
	+ **Aggregation**
		- 클래스 간 약한 연관관계(weak coupling)를 가지고, 다른 생명 주기(different life cycle)를 가질 때

### 1.1 IS-A: 상속
**IS-A** 는 ***"~는 ~의 한 종류다."*** 라고 표현할 수 있으며, **IS-A** 관계를 프로그램에서 표현할 때는 **상속(inheritance)** 을 사용한다. 상속 관계에서 상속을 하는 클래스를 기본(base) 클래스, 부모(parent) 클래스, 슈퍼(super) 클래스라고 하며, 상속을 받는 클래스를 파생(derived) 클래스, 자식(child) 클래스, 서브(sub) 클래스라고 한다. ***상속은 자식 클래스가 부모 클래스의 모든 특성(instance variable, class variable) 또는 기능(instance method, class method) 등을 가지면서 그 외에 다른 특성이나 다른 기능을 가지고 있을 때 활용한다.*** Python으로 부모 클래스인 `Computer` 클래스와 자식 클래스인 `Laptop` 클래스를 구현해보면 아래와 같이 구현할 수 있다.

```python
class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        
    def browse(self):
        print('browse')
        
    def work(self):
        print('work')

class Laptop(Computer):
    def __init__(self, cpu, ram, battery): # method overriding
        super().__init__(cpu, ram)
        self.battery = battery
        
    def move(self):
        print('move')
```

```python
com = Computer(cpu = 'intel', ram = '64gb')
lap = Laptop(cpu = 'intel', ram = '16gb', battery = 'lg')

com.browse()
com.work()

lap.browse()
lap.work()
lap.move()
```

```bash
browse
work
browse
work
move
```

### 1.2 HAS-A: 합성 또는 통합
프로그램에서 **HAS-A** 관계는 ***~이 ~을 가진다 또는 포함한다.*** **HAS-A** 로 표현되는 두 관계는 각각 **합성(composition)** , **통합(aggregation)** 을 이용하여 표현한다.

#### 합성(composition)
**합성(composition)** 은 ***각각의 클래스로부터 생성된 인스턴스의 생명주기(life cycle)가 같고 강한 연관관계(strong coupling)을 갖고 있다.*** 예를 들어 컴퓨터와 CPU의 관계라고 볼 수 있으며, Python을 이용하여 아래의 코드처럼 표현할 수 있다.

```python
class CPU:
    pass

class RAM:
    pass

class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()
```

#### 통합(aggregation)
**통합(aggregation)** 은 ***각각의 클래스로부터 생성된 인스턴스의 생명주기(life cycle)이 서로 다르고 약한 연관관계(weak coupling)을 갖고 있다.*** 예를 들어 경찰과 총의 관계라고 볼 수 있으며, Python을 이용하여 아래의 코드처럼 표현할 수 있다.

```python
class Gun:
    def __init__(self, kind):
        self.kind = kind
    
    def bang(self):
        print('bang bang!')

class Police:
    def __init__(self):
        self.gun = None
    
    def acquire_gun(self, gun):
        self.gun = gun
        
    def release_gun(self):
        gun = self.gun
        self.gun = None
        return gun
    
    def shoot(self):
        if self.gun:
            self.gun.bang()
        else:
            print('Unable to shoot')
```

```python
revolver = Gun('revolver')
new_pol = Police()
new_pol.shoot()
```

```bash
Unable to shoot
```

```python
new_pol.acquire_gun(gun = revolver)
revolver = None
new_pol.shoot()
```

```bash
bang bang!
```

```python
revolver = new_pol.release_gun()
new_pol.shoot()
```

```bash
Unable to shoot
```

## 2. 메소드 오버라이딩과 다형성
**다형성(polymorphism)** 이란 ***"상속 관계에 있는 다양한 클래스의 인스턴스에서 같은 이름의 메소드를 호출할 때, 각 인스턴스가 서로 다르게 구현된 메소드를 호출함으로써 서로 다른 행동(behavior), 기능, 결과를 가져오는 것"*** 을 의미한다. 이를 구현하기위해서는 **파생 클래스(derived class)** 안에서 상속받은 메소드를 다시 구현 하는 것을 **메소드 오버라이딩(method overriding)** 이라고 한다.

### 2.1 메소드 오버라이딩
**메소드 오버라이딩(method overriding)** 은 자식클래스가 부모 클래스를 상속할 때, 부모 클래스에 존재하는 class method, instance method 등을 자식클래스에서 다시 구현하는 것을 의미한다. 아래의 예제로 확인할 수 있다. 또한 이를 통해서 같은 이름의 메소드를 호출해도 호출한 인스턴스에 따라 다른결과를 내는 **다형성(polymorphism)** 을 구현한다.

```python
class CarOwner:
    def __init__(self, name):
        self.name = name
    
    def concentrate(self):
        print('{}은 집중하느라 아무것도 못합니다.'.format(self.name))
        
class Car:
    def __init__(self, owner_name):
        self.car_owner = CarOwner(owner_name)
        
    def drive(self):
        self.car_owner.concentrate()
        
class SelfDrivingCar(Car):
    # method overriding
    # 자식 클래스가 부모 클래스에 이미 있는 메소드를 재정의하는 것!
    # 자식 클래스의 메소드의 기능이 달라졌을 때
    def drive(self):
        print('차가 운전합니다. {}는 지금 놀고있어요.'.format(self.car_owner.name))
```

```python
tesla = SelfDrivingCar(owner_name='aisolab')
tesla.drive()
```

```bash
차가 운전합니다. aisolab는 지금 놀고있어요.
```

```python
# 다형성 예시
normal_car = Car('yang')
self_car = SelfDrivingCar('park')
self_car2 = SelfDrivingCar('kim')

cars = []
cars.append(normal_car)
cars.append(self_car)
cars.append(self_car2)

for car in cars:
    car.drive()
```

```bash
yang은 집중하느라 아무것도 못합니다.
차가 운전합니다. park는 지금 놀고있어요.
차가 운전합니다. kim는 지금 놀고있어요.
```

### 2.2 다형성
**다형성(polymorphism)** 을 구현하는 데, 가장 큰 개념이 되는 부모 클래스로는 인스턴스를 생성하지 못하게 **추상 클래스(abstract class)** 기법을 이용할 수 있다. 추상 클래스 기법은 추상 클래스로 선언한 부모 클래스에서 정의된 instance method, class method 들 중, **추상 메소드(abstract method)** , **추상 클래스 메소드(abstract class method)** 로 정의된 메소드의 경우 상속받는 자식 클래스에서 반드시 메소드 오버라이딩을 해야한다. 그렇지않으면 자식 클래스도 추상 클래스가 되어 인스턴스를 만들 수가 없다. Python으로 작성한 예제를 통해서 확인해 볼 수 있다.

```python
# 아래의 방법으로 추상클래스를 만들자
from abc import ABCMeta, abstractmethod, abstractclassmethod

class Animal(metaclass = ABCMeta):
    
    def die(self):
        print('time to die')
        
    @abstractmethod # 자식클래스에서 반드시 재정의해야한다. 
    def eat(self):  # abstract instance method
        pass
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

## 3. 클래스 설계 예제
클래스를 계층적 구조로 설계할 때는 아래의 두 가지를 고려해야한다.

* 코드 재사용을 위해 공통 부분을 부모 클래스로 묶는다. 
* 부모 클래스가 추상 클래스인 경우를 제외하고, 자식 클래스에서 부모 클래스의 여러 메소드를 메소드 오버라이딩한다면 자식 클래스를 만들지 않는 것이 좋다.

예를 들어, 게임 세계의 Character와 Monster들을 클래스 계층적 구조로 아래와 섹션에서 소개하는 것들과 같이 구현할 수 있다.

### 3.1 Character 클래스 만들기
**추상 클래스(abstract class)** 로 `Character` 클래스를 구현하고, 해당 클래스를 이후 섹션에서 구현할 `Player` 클래스와 `Monster` 클래스가 상속

```python
from abc import ABCMeta, abstractmethod

# 자식 클래스가 상속 받을 추상 클래스
class Character(metaclass = ABCMeta):
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    # abstact method에서 거의 함수 signature를 정의함
    # abstract instance method를 상속받는 자식클래스는 무조건 method overriding으로 재정의해야함
    @abstractmethod 
    def attack(self, other, attackkind):
        pass

    @abstractmethod
    def get_damage(self, power, attackkind):
        pass

    def __str__(self):
        return '{} : {}'.format(self.name, self.hp)
```

### 3.2 Player 클래스 만들기
`Player` 클래스는 추상 클래스인 `Character` 클래스를 상속받아서 아래와 같이 구현

```python
class Player(Character):
    def __init__(self,name = 'player', hp = 100, power = 50, *skills):
        super().__init__(name, hp, power)
        self.skills = list(skills)

    def attack(self, monster, attackkind): #
        '''
        만약 attackkind가 skills에 있다면 monster 공격
        message passing으로 구현
        '''
        if attackkind in self.skills:
            monster.get_damage(power = self.power, attackkind = attackkind)
        else:
            return
    
    def get_damage(self, power, attackkind):
        '''
        monster의 attackkind가 플레이어의 skills 목록에 있으면 power // 2 만큼 데미지를 입는다.
        아니면 그대로 hp -= power
        '''
        if attackkind in self.skills:
            self.hp -= power // 2
        else:
            self.hp -= power 
```

### 3.3 Monster, IceMonster, FireMonster 클래스 만들기
`Monster` 클래스는 추상 클래스인 `Character` 클래스를 상속하고, `IceMonster` , `FireMonster` 클래스는 `Monster` 클래스를 상속

```python
'''
몬스터
attack -> 몬스터의 attackkind가 player의 attackkind와 같으면 공격 아니면 공격안함
get_damage -> 만약 'ICE' 공격을 받았는데 나의 self.attackkind = 'ICE' -> skdml self.hp += power
           -> 그게 아니면 나의 self.hp -= power
'''

class Monster(Character):    
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.attackkind = self.__class__.__name__.replace('Monster', '')


    def attack(self, player, attackkind):
        if self.attackkind == attackkind:
            player.get_damage(power = self.power, attackkind = self.attackkind)
        else:
            return

    def get_damage(self, power, attackkind):
        if self.attackkind == attackkind:
            self.hp += power
        else:
            self.hp -= power

class IceMonster(Monster):
    pass

class FireMonster(Monster):
    pass
```

위의 각각의 클래스에 대한 구현들이 잘 구현되었는 지 아래의 코드를 통해서 확인할 수 있다.

```python
player = Player('aisolab', 100, 50, 'Fire','Ice')
monsters = [IceMonster(name = 'IceMonster', hp = 100, power = 30),
            FireMonster(name = 'FireMonster', hp = 150, power = 50)]

for monster in monsters:
    print(monster)
```

```bash
IceMonster : 100
FireMonster : 150
```

```python
for monster in monsters:
    player.attack(monster, 'Fire')
for monster in monsters:
    print(monster)
```

```bash
IceMonster : 50
FireMonster : 200
```

## 4. 연산자 오버로딩
**연산자 오버로딩(operator overloading)** 은 클래스안에서 메소드로 **연산자(operator)** 를 새롭게 구현하는 것으로 다형성의 특별한 형태이다. Python에서는 클래스를 정의할 때, ***산술 연산자와 논리 연산자 등 다양한 연산자들을 메소드 오버라이딩하여 재정의하면 된다.*** 예를 들어 Python에서 `__add__` 메소드에 대해서 메소드오버라이딩을 하면 `+` operator로 인스턴스간의 연산을 할 수 있다.

```python
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def __add__(self, other):
        return Point(self._x + other._x, self._y + other._y)
    
    def __str__(self):
        return '({}, {})'.format(self._x, self._y)
```

```python
p1 = Point(1,2)
p2 = Point(3,4)
print(p1, p2)
```

```bash
(1, 2) (3, 4)
```

```python
p3 = p1 + p2
print(p3)
```

```bash
(4, 6)
```