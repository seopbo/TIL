# Character and Strings
본 내용은 [양태환](https://github.com/ythwork)님의 저서 **컴퓨터 사이언스 부트캠프 with 파이썬** 을 읽고 요약정리한 내용

* Reference
	+ <http://norux.me/31> 
	+ <https://www.bsidesoft.com/?p=3435>
	+ <https://ko.wikipedia.org/wiki/%EB%AC%B8%EC%9E%90_%EC%9D%B8%EC%BD%94%EB%94%A9>

## 1. 아스키코드
* **문자 집합(character set)** : 문자(character)를 모아둔 집합,
  + eg. 라틴문자
* **문자 인코딩(character encoding)** : 문자 집합을 메모리에 저장하거나 통신하는데 사용하기위해 부호화하는 방식  
  + **코드 포인트(code point)** : 컴퓨터에 문자를 인식시키려면 문자를 정수에 매핑하고 이를 0과 1로 이루어진 2진수로 나타내야함. ***이때 매핑된 정수를 코드 포인트(code point)라고 함***
  + **부호화된 문자 집합(coded character set, ccs)** : 문자마다 매핑된 코드 포인트를 모아놓은 집합
    - 아스키코드(ASCII) : 7비트 활용, 0~127까지의 코드 포인트 활용, 128개의 문자 
    - 유니코드(UNICODE) : 16비트(2바이트) 활용, 0 ~ 65,535까지의 코드 포인트 활용, 65,536개의 문자

* **문자 인코딩 방식(character encoding scheme, ces)** : 특정 부호화된 문자집합에서 나온 코드 포인트를 2진수로 바꾸었을 때, 이를 코드 유닛으로 인코딩하는 방법
  - eg. UTF-8, UTF-16, UTF-32, CP949, EUC-KR
  + **코드 유닛(code unit)** : 코드 포인트를 2진수로 변환하고 이를 특정 방법(eg. UTF-8)으로 인코딩했을 대 얻어지는 비트의 나열 

    

