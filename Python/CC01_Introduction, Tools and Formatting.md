# Clean code in Python
본 내용은 **파이썬 클린코드 (유지보수가 쉬운 파이썬 코드를 만드는 비결)** 를 읽고 간략하게 내용을 정리한 것입니다.
* link : https://github.com/rmariano/Clean-code-in-Python/tree/master/book/src/ch01
## Chapter01 소개, 코드 포매팅과 도구
이 장에서 다루는 주제는 다음과 같다.
* 클린 코드는 포매팅 이상의 훨씬 중요한 것을 의미한다.
* 떄문에 표준 포매팅을 유지하는 것이 유지보수성의 핵심 유의사항이다.
* 파이썬이 제공하는 기능을 사용하여 자체 문서화된 코드를 작성하는 방법
* 코드의 레이아웃을 일정하게 유지하여 팀 멤버들이 문제의 본질을 해결하는 데 초점을 맞출 수 있도록 도구를 설정하는 방법

### 클린 코드의 의미
프로그래밍 언어라는 것은 인간의 아이디어를 컴퓨터에 전달하기위해 사용한다는 의미도 있지만 뿐만 더 중요한 의미는 ***아이디어를 다른 개발자에게 전달한다는 것***에 있다. 고로 클린 코드인 지 아닌 지는 ***다른 엔지니어가 코드를 읽고 유지 관리할 수 있는 지 여부에 달려있다.*** 그러므로 전문가인 우리 자신이 클린 코드를 판단할 수 있는 유일한 사람이다.

### 클린 코드의 중요성
* 유지보수성 향상
	+ 코드가 유지보수 가능한 상태로 가독성이 높으면, 민첩한 개발과 지속적인 배포가 가능하다.
* 기술부채(나쁜 결정이나 적당한 타협의 결과로 생긴 소프트웨어적 결함)의 감소
	+ 코드가 유지보수 가능한 상태로 가독성이 높으면, 코드를 수정하고 리팩토링하는 시간을 줄 일 수 있다. -> 기술 부채에 대한 비용이 싸진다.

### 클린 코드에서의 포매팅의 역할
클린 코드는 ***품질 좋은 소프트웨어를 개발하고, 견고하고 유지보수가 쉬운 시스템을 만들고, 기술 부채를 회피하는 것을 말한다.*** 즉 유지보수성이나 소프트웨어 품질에 관한 것을 의미하며, 올바르게 포매팅 하는 것을 이와 같은 작업을 효율적으로 하는 데에 있어 중요한 역할을 한다.

### 프로젝트 코딩 스타일 가이드 준수
코딩 가이드라인은 품질 표준을 지키기 위해 프로젝트에서 따라야만 하는 최소한의 요구사항이다. 좋은 코드레이 아웃에서 가장 필요한 특성은 일관성이다. 코드가 일관되게 구조화되어 있으면 가독성이 높아지고 이해하기 쉬워진다. 특히 ***파이썬이 따라야하는 코딩 스타일은 [PEP-8](https://www.python.org/dev/peps/pep-0008/)이며***, 작업하는 프로젝트의 특수성(예: 한 줄의 길이, 들여쓰기의 간격 등)을 확장하거나 일부만 채택할 수 있다. 다른 표준을 고민하기보다는 그대로 사용하기나 확장해서 사용할 것을 권장한다.

### Docstring과 Annotation
코드를 문서화하는 것은 주석을 추가하는 것과는 다르다. 주석(comment)는 가급적 피하는 것이 좋다. 문서화를 통해 데이터 타입이 무엇인 지 설명하고, 예제를 제공할 수 있다.

#### Docstring

***docstring은 소스 코드에 포함된 주석(comment)가 아니라 문서(documentation)이다.*** 코드에 주석을 다는 것은 여러가지 이유로 나쁜 습관이며 대표적으로 아래와 같다. (드물긴하지만 외부 라이브러리에 오류가 있다면 짧은 주석을 다는 것은 괜찮다.)

1. 주석은 코드로 아이디어를 제대로 표현하지 못했음을 나타내는 것이다.
2. 오해의 소지가 있다.

docstring은 주석을 다는 것이 아니라 코드의 특정 컴포넌트(모듈, 클래스, 메서드 또는 함수)에 대한 문서화이며, 이런 컴포넌트에 사용하는 것은 매우 권장되는 부분이다. ***가능한 많은 docstring을 추가하는 것이 좋다.*** docstring을 코드에 포함시키는 것이 좋은 이유는 ***파이썬이 동적 타이핑을 하기 때문이다.*** 예를 들어 함수는 파라미터의 값으로 무엇이든 사용할 수 있다. 파이썬은 파라미터의 타입을 체크하거나 강요하지 않는다. 따라서 함수를 수정해야 하는데 함수의 이름과 파라미터의 이름이 충분히 설명적이라면 굉장히 운이 좋은 것이다. 그렇다 해도 아직 정확히 어떤 타입을 사용해야 하는 지 알 수 없다. 이런 경우 docstring이 도움이 될 것이다. 예상되는 함수의 입력과 출력을 문서화하면 사용자가 사용할 때 함수가 어떻게 동작하는 지 이해하기 쉽다. 표준 라이브러리에 docstring을 사용하는 좋은 예가 있다.

```python
Docstring:
D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
In either case, this is followed by: for k in F:  D[k] = F[k]
Type:      method_descriptor
```

docstring은 코드에서 분리되거나 독립된 것이 아니다. 코드의 일부가 되어 접근할 수 있어야한다. 객체에 docstring이 정의되어 있으면 `__doc__` 속성을 통해 접근이 가능하다. 

```python
print(dict.__doc__)
```
```python
dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
    for k, v in iterable:
        d[k] = v
dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)
```

#### Annotation

***[PEP-3107](<https://www.python.org/dev/peps/pep-3107/>)에는 annotation을 소개하고 있다. 기본 아이디어는 코드 사용자에게 함수 인자로 어떤 값이 와야 하는지 힌트를 주자는 것이다. 정말 힌트를 주는 것이며, 어노테이션은 타입 힌팅(type hinting)을 활성화한다.*** annotation을 사용해 변수의 예상 타입을 지정할 수 있다. 실제로는 타입 뿐 아니라 변수를 이해하는 데 도움이 되는 어떤 형태의 메타데이터라도 지정할 수 있다. 아래의 예제를 살펴보자.

```python
class Point:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        
def locate(latitude: float, longitude: float) -> Point:
    """맵에서 좌표에 해당하는 객체를 검색"""
```

여기서 `latitude`와 `longitude`는 `float` 타입의 변수이다. 이 것을 통해 함수 사용자는 예상되는 타입을 알 수 있다. 하지만 파이썬이 타입을 검사하거나 강제하지는 않는다. 또한 함수 반환 값에 대한 예상 타입을 지정할 수도 있다. 위 예제에서 `Point`는 사용자 정의 클래스이므로 반환되는 값이 `Point`의 인스턴스라는 것을 의미한다. 그러나 annotation으로 타입만 지정할 수 있는 것은 아니다. 파이썬 인터프리터에서 유효한 어떤 것도 사용할 수 있다. 예를 들어 변수의 의도를 설명하는 문자열, 콜백이나 유효소어 검사 함수로 사용할 수 있는 `callable`등이 있다. annotation을 사용하면 `__annotations__`라는 특수한 속성이 생긴다. 이 속성은 annotation의 이름과 값을 매핑한 사전 타입의 값이다. 앞의 예제에서는 다음과 같이 출력된다.

```python
print(locate.__annotations__)
```
```python
{'latitude': <class 'float'>, 'longitude': <class 'float'>, 'return': <class '__main__.Point'>}
```

***[PEP-484](https://www.python.org/dev/peps/pep-0484/)를 적용하면 annotation을 통해 코드를 확인할 수 있다. 이 PEP는 타입 힌팅의 기본 원리를 정의한 것으로 annotation을 통해 함수의 타입을 체크할 수 있다.  타입 힌팅은 인터프리터와 독립된 추가 도구를 사용하여 코드 전체에 올바른 타입이 사용되었는 지 확인하고 호환되지 않는 타입이 발견되었을 때 사용자에게 힌트를 주는 것이다.*** 타입 힌팅은 코드의 타입을 확인하기 위한 도구 이상의 것을 의미한다. 파이썬 3.5부터는 새로운 `typing` 모듈이 소개되었고 파이썬 코드에서 타입과 annotation을 정의하는 방법이 크게 향상 되었다. 기본 개념은 코드의 시맨틱이 보다 의미 있는 개념을 갖게 되면 코드를 이해하기 쉽고 특정 시점에 어떻게 될 지 예측할 수 있다는 것이다. 파이썬 3.6부터는 함수 파라미터와 리턴 타입뿐만 아니라 변수에 직접 타입 힌팅을 할 수 있다. 이것은 [PEP-526](<https://www.python.org/dev/peps/pep-0526/>)에서 소개 되었으며, 다음과 같이 값을 지정하지 않은 채로 변수의 타입을 선언할 수 있다.

```python
class Point:
    lat: float
    long: float

print(Point.__annotations__)
```
```python
{'lat': <class 'float'>, 'long': <class 'float'>}
```

### Annotation은 Docstring을 대체하는 것일까?
docstring에 포함된 정보의 일부(eg. 함수의 파라미터 또는 속성의 타입을 문서화할 때 docstring을 사용하는 경우)는 annotation으로 이동시킬 수 있는 것이 사실이다. 그러나 ***docstring을 통해 보다 나은 문서화를 위한 여지를 남겨두어야 한다. 특히 동적 데이터 타입과 중첩 데이터 타입의 경우 예상 데이터의 예제를 제공하여 어떤 형태의 데이터를 다루는 지 제공하는 것이 좋다.*** 아래의 예제를 통해 확인해보자.

```python
def data_from_response(response: dict) -> dict:
    """response에 문제가 없다면 reponse의 payload를 반환
    
    - response 사전의 예제::
    {
        'status': 200, # <int>
        'timestamp': '...', # 현재 시간의 ISO 포맷 문자열
        'payload': {...} # 반환하려는 사전 데이터
    }
    
    - 반환 사전 값의 예제::
    {'data': {...}}
    
    - 발생 가능한 예외:
    - HTTP status가 200이 아닌 경우 ValueError 발생
    """
    if response['status'] != 200:
        raise ValueError
    return {'data': response['payload']}
```

### 기본 품질 향상을 위한 도구 설정

동료가 작성한 코드를 살펴볼 때는 다음 질문을 해야 한다.

* 이 코드를 동료 개발자가 쉽게 이해하고 따라갈 수 있을까?
* 업무 도메인에 대해서 말하고 있는가?
* 팀에 새로합류하는 사람도 쉽게 이해하고 효과적으로 작업할 수 있을까?

이전에 살벼보았듯이 코드 포매팅, 일관된 레이아웃, 적절한 들여쓰기를 검사하는 것만으로는 충분하지 않다. 더군다나 높은 수준의 엔지니어에게 이것은 당연한 것이므로 레이아웃의 개념을 뛰어넘는 그 이상의 것을 읽고 쓸 수 있어야한다. 따라서 이런 것들을 살펴보는 데 시간을 낭비하기보다는 실제 어떤 패턴이 사용되었는 지 살펴서 코드의 실제 의미와 가치를 이해하는 데 시간을 투자하는 것이 효과적이다. 이 모든 검사는 자동화해야한다. 테스트 또는 체크리스트의 일부가 되어 지속적인 통합 빌드(continuous integration build)의 하나가 되어야한다. 이러한 검사에 실패하면 빌드도 실패하야 한다. 이렇게 하는 것만이 코드 구조의 연속성을 확보할 수 있는 유일한 방법이다. 이것은 팀에서 참고할 수 있는 객관적인 지표 역할도 한다. ***일부 엔지니어 또는 팀 리더가 코드 리뷰 시 PEP-8에 대한 동일한 의견을 항상 말하도록 하게 만드는 대신, 빌드 시 자동으로 실패하도록 해야 객관성을 얻을 수 있다.*** 이를 위해 아래와 같은 것을 도입할 수 있다.

* `Mypy`를 사용한 타입 힌팅
* `Pylint`를 사용한 코드 검사
* 자동 검사 설정
  * eg. 리눅스 개발환경에서 빌드를 자동화하기위해 Makefile을 사용, 빌드 외에도 포매팅 검사나 코딩 컨벤션 검사를 자동화하기 위해 사용할 수 있다.

