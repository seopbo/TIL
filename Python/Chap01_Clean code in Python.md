# Clean code in Python
본 내용은 **파이썬 클린코드 (유지보수가 쉬운 파이썬 코드를 만드는 비결)**를 읽고 간략하게 내용을 정리한 것입니다.

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
* 기술부채의 감소
	+ 코드가 유지보수 가능한 상태로 가독성이 높으면, 코드를 수정하고 리팩토링하는 시간을 줄 일 수 있다. -> 기술 부채에 대한 비용이 싸진다.

### 클린 코드에서의 포매팅의 역할
클린 코드는 ***품질 좋은 소프트웨어를 개발하고, 견고하고 유지보수가 쉬운 시스템을 만들고, 기술 부채를 회피하는 것을 말한다.*** 즉 유지보수성이나 소프트웨어 품질에 관한 것을 의미하며, 올바르게 포매팅 하는 것을 이와 같은 작업을 효율적으로 하는 데에 있어 중요한 역할을 한다.

### 프로젝트 코딩 스타일 가이드 준수
코딩 가이드라인은 품질 표준을 지키기 위해 프로젝트에서 따라야만 하는 최소한의 요구사항이다. 좋은 코드레이 아웃에서 가장 필요한 특성은 일관성이다. 코드가 일관되게 구조화되어 있으면 가독성이 높아지고 이해하기 쉬워진다.