# Git basics
Git에 관한 개념에 대한 자세한 설명은 아래의 Reference를 참고, 여기에서는 각 명령어들의 사용법과 flow만 다룸

- Reference
	- https://www.rlee.ai/apt/git
	- https://github.com/Gyubin/TIL/blob/master/ETC/git_gitflow.md
	- https://opentutorials.org/module/2676
- - -

### Basic commands
- `git config` : git의 configuration을 설정, 예를 들면 아래처럼 version control을 하는 주체의 정보를 설정할 수 있다.
```bash
# example
git config --global user.name 'aisolab' # 자신의 nickname
git config --global user.email 'bsk0130@gmail.com' # 자신의 email
```

- `git init` : version control을 할 project의 directory로 이동 후 입력
	- 해당 directory 밑에 **.git** directory가 생성되며, 이 directory는 version control을 위한 여러 파일을 담고 있음

- `git status` : project의 directory의 상태확인
	- 어떤 파일을 git이 version control을 하는 지 확인 가능하며, **stage area (ready to commit)** 에 어떤 파일이 있는 지 확인 가능

- `git add` : version control을 할 project의 directory 내의 파일들을 추가하여 해당 파일을 git이 tracking, 또는 이미 변경된 파일의 경우 **stage area (ready to commit)** 에 넣는 역할을 함
	- 이미 작업한 내용들 중에서 선택적으로 commit을 하여, version을 만들 수 있음

- `git commit` : version을 생성하며, commit message (version message)를 기록할 수 있는 editor (eg. vim)을 실행함. commit message를 기록하면 version을 만들어 **repository** 에 넣음
	- `git commit -m 'message'` : commit과 동시에 commit message를 작성
	- 하나의 작업당 하나의 version을 하나 만드는 것이 rule

- `git log` : commit history를 조회, 여러 옵션을 줄 수 있으나 다음의 아래가 유용
```bash
#git log 실행한 결과 (example)
commit 1457925822c829fdd998a17ac3860fbae61f44d6 # commit id
Author: aisolab <bsk0130@gmail.com> # user.name user.email
Date:   Thu Jul 12 17:24:38 2018 +0900
    1 # commit message
```
	- `git log commit_id` : commit id (commit message에 해당하는 version을 가리키는 id)를 입력하면 해당 version이전부터 해당 version가지의 commit message를 확인할 수 있음
	- `git log -p` : 전체 version간의 source 상의 변경점을 확인할 수 있음
	- `git log -p -n` : 최근 n개의 version간의 source 상의 변경점을 확인할 수 있음

- `git diff` : 최근 2개 version의 source상의 변경점을 확인, +++에 해당하는 것이 더 최신의 version
	- `git diff commit_id1 commit_id2` :

