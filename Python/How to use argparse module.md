# How to use argparse module
argparse module은 command line parsing module로써 CLI program 또는 tool을 만들 때 사용하며, 아래와 같은 방법으로 module을 활용한다. 상세한 내용은 아래의 Reference를 참고

* Reference
	+ <https://docs.python.org/3/library/argparse.html?highlight=argparse>
	+ <https://docs.python.org/3/howto/argparse.html#id1>
	+ <https://soooprmx.com/archives/5756>
	+ <https://blog.naver.com/cjh226/220997049388> 

### Parser 생성
argparse module을 이용하여 parser instance를 생성한다.
* `argparse.ArgumentParser` : ***ArgumentParser class의 instance를 생성, 필요시 여러 argument에 값을 전달하나 아래와 같이만 활용해도 충분하다.*** instance의 method를 이용하여 실제로 parsing을 함

```python
import argparse
parser = argparse.ArgumentParser() # parser instance를 생성
```

### Parser 활용
생성된 parser instance의 method를 활용하여 CLI를 통해 입력받는 parameter를 parsing한다.

***notice***
1. 아래의 설명에서 argument로 통칭할 때는 positional argument와 optional argument를 둘다 가리킴
2. 아래의 설명에서의 variable의 name은 `args = parser.parse_args()`에서 `args`의 member variable의 name을 의미

* `argparse.ArgumentParser.add_argument` : CLI에서 입력받을 argument를 설정한다. 해당 method에는 여러 argument가 있지만 중요한 몇 개는 아래와 같다.
  + `name of flags` : argument를 등록한다. postional argument와 optional argument로 나누어져 있으며 아래와 같은 특징이 있음
    - positional argument : `name of flags`에 `-`없이 값을 전달하며, `dest` argument에 variable의 name을 전달할 수 없다. 이는 `name of flags`라는 의미대로 positional argument를 활용할 때, 바로 variable name이 되기 때문
    ```python
    # test.py
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('p')
    args = parser.parse_args()
    print(args)
    ```
    ```bash
    $ python test.py -h
    usage: test.py [-h] p
    
    positional arguments:
      p
    
    optional arguments:
      -h, --help  show this help message and exit
    ```
    ```bash
    $ python test.py hello
    Namespace(p='hello')
    ```

    - optional argument : `name of flags`에 `-`, `--`를 붙여 값을 전달하며, 해당 method의 `dest` argument에 값을 전달하여 명시적으로 variable의 name을 결정할 수 있다. `dest` argument에 값을 전달하지않으면, `--string` 에서 string에 해당하는 문자열을 variable의 name으로 한다.
    ```python
    # test.py
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--optional', dest = 'o', type = str)
    args = parser.parse_args()
    print(args)
    ```
    ```bash
    $ python test.py -h
    usage: test.py [-h] [-o O] # -o O에 O는 O에 해당하는 부분에 값을 전달하라는 것
    
    optional arguments:
      -h, --help          show this help message and exit
      -o O, --optional O
    ```
    ```bash
    $ python test.py -o hello
    Namespace(o='hello')
    ```

  + `nargs` : argument가 전달받을 수 있는 값의 개수를 가리킴. 이 값보다 많은 값이 들어오는 경우는 무시되며, `+`를 전달할 경우 1개 이상의 값을 받는다는 의미이다. 전달받은 여러 값은  list의 형태로 저장

  + `default` : optional argument를 추가할 때, 해당 optional argument가 필수적으로 값을 전달받아야할 argument가 아닐 경우, `default` argument에 값을 전달하면 말그대로 default 값을 설정가능

  + `type` : argument에 전달받은 parameter를 parsing하여 저장할 때, type을 설정

  + `choices` : argument가 받을 수 있는 값의 목록을 list형태로 전달, argument에 전달받은 값이 list의 element 중 하나가 아니면 error 발생

  + `help` : `-h` 또는 `--help` option으로 script를 실행했을 때, argument에 대한 설명을 설정

  + `required` : 필수적으로 값을 전달받아야할 optional argument인 경우 True로 설정, 없으면 알아서 error message를 표시하고 자동으로 exit (positional argument일 때는 해당 argument를 사용하지 않음)

  + `metavar` : usage message를 출력할 때 표시할 name을 지정 (`dest` argument에 전달한 name보다 우선순위가 높음, 하지만 딱히 쓰지않는 게 좋을 듯하다.)

  + `dest` : optional argument를 사용 시 variable의 name을 명시적으로 지정할 때 사용
