# Git basics
[지옥에서 온 Git](https://opentutorials.org/module/2676)의 내용을 command 위주로 정리, 그 외 참고한 Reference는 아래와 같음.

* Reference
	* https://git-scm.com/book/en/v2
	+ https://www.rlee.ai/apt/git
	+ https://github.com/Gyubin/TIL/blob/master/ETC/git_gitflow.md
---

### Basic commands
#### Applying version control to project
* `git config` : git의 configuration을 설정, 예를 들면 아래처럼 version control을 하는 주체의 정보를 설정할 수 있다.

```bash
# example
git config --global user.name 'aisolab' # 자신의 nickname
git config --global user.email 'bsk0130@gmail.com' # 자신의 email
```

* `git init` : version control을 할 project의 directory로 이동 후 입력 (working directory로 만들기)
	+ 해당 directory 밑에 **.git** directory가 생성되며, ***이 directory는 version control을 위한 여러 파일을 담고 있음***

* `git status` : project의 directory의 상태확인

	+ 어떤 파일을 git이 version control을 하는 지 확인 가능하며, **staging area (ready to commit, index)** 에 어떤 파일이 있는 지 확인 가능

* `git add` : version control을 할 project의 directory 내의 파일들을 추가하여 해당 파일을 git이 tracking, 또는 이미 변경된 파일의 경우 **staging area (ready to commit, index)** 에 넣는 역할을 함

	+ 이미 작업한 내용들 중에서 선택적으로 commit을 하여, version을 만들 수 있음

* `git commit` : version을 생성하며, commit message (version message)를 기록할 수 있는 editor (eg. vim)을 실행함. commit message를 기록하면 version을 만들어 **repository** 에 넣음

	+ `git commit -m 'message'` : commit과 동시에 commit message를 작성

	+ 하나의 작업당 하나의 version을 하나 만드는 것이 rule

#### Checking the changes in commit history
* `git log` : commit history를 조회, 여러 옵션을 줄 수 있으나 다음의 아래가 유용

	+ `git log commit_id` : commit_id (commit message에 해당하는 version을 가리키는 id)를 입력하면 해당 version이전부터 해당 version가지의 commit message를 확인할 수 있음

	+ `git log -p` : 전체 version간의 source 상의 변경점을 확인할 수 있음

	+ `git log -p -n` : 최근 n개의 version간의 source 상의 변경점을 확인할 수 있음

		- Git에서는 **.git/objects** directory에서 object의 형태 (사실상 파일)로 version control을 하는 데에 있어서 필요한 내역을 관리

		- object id가 파일 내용을 기반으로 **sha1 hash** 방식으로 암호화되어 생성되고, 이를 이름으로하는 object가 생성됨. `git add`, `git commit` 등의 command가 **.git/objects** directory에 발생시키는 내용은 아래와 같음

		- `git add` : **.git/objects** directory에 파일의 내용을 담은 object를 추가함, 이를 **blob** object라고함

		- `git commit` : **.git/objects** directory에 **parent** 에 해당하는 version의 object id와 **tree** 에 해당하는 version의 object id를 담은 object를 추가함, 이를 **commit** object라고함

		- **.git/objects** directory에 생성되는 object는 모두 **commit** object, **blob** object, **tree** object 중 하나

			- **commit** object는 **tree** object의 object id와 **parent** object의 object id를 기록

			- **blob** object는 실제 파일의 내용을 기록

			- **tree** object는 **blob** object의 object id를 기록

```bash
#git log 실행한 결과 (example)
commit 1457925822c829fdd998a17ac3860fbae61f44d6 # commit id (object id)
Author: aisolab <bsk0130@gmail.com> # user.name user.email
Date:   Thu Jul 12 17:24:38 2018 +0900
    1 # commit message
```

* `git diff` : `git add` 이전의 source상의 변경점을 확인, +++에 해당하는 것이 더 최신의 version

	+  ***commit을 하기전에 시행한 작업에 대해서 변경점을 확인가능한 용도로도 사용할 수 있음***
	
		-  이전 version이 있고, 어떤 작업을 했을 때, `git add` 하기전에 변경점을 확인가능

	+ `git diff commit_id1..commit_id2` : commit_id1에 해당하는 version의 source와 commit_id2에 해당하는 version의 source간의 변경점을 확인

		- commit_id2에 최신의 version에 해당하는 commit_id를 써야 +++에 최신 version의 source의 변경점이 기록됨

#### Back to the past
* `git reset` : 특정 과거 시점 이후의 version을 날려서 특정 과거 시점의 version을 최신 version으로 만듦, 아래와 같은 command로 활용

	+ `git reset commit_id --hard` : 이 때 commit_id에는 과거 특정 시점의 version의 commit_id를 전달

	+ ***remote repository를 활용하지 않을 때, 즉 local repository를 활용할 때만 사용할 것***, 왜냐하면 이 command는 local repository만 과거시점으로 돌리기 때문

* `git revert` : 최신 version이 잘 못 되었을 때, 해당 version의 한 시점 과거의 것과 동일한 source인 새로운 version을 만듦, 아래와 같은 command로 활용

	+ `git revert commmit_id` : commit_id에 가장 최근 commit_id를 넣음, 중간시점의 commit_id를 넣으면 conflict 발생

	+ ***remote repository를 활용할 때 사용할 것***, remote repository의 시점도 과거로 돌아감

### Branching commands
#### Branching 
* `git branch` : branch의 목록을 확인하는 command, option을 주어 여러가지로 방법으로 사용

	+ `git branch branch_name` : branch_name에 해당하는 branch를 생성

	+ `git branch -d branch_name` : branch_name에 해당하는 branch를 삭제

	+ `git branch -D branch_name` : 병합하지않은 branch_name에 해당하는 branch를 강제삭제

* `git checkout` : branch를 전환하는 command, 아래처럼 사용

	+ `git checkout branch_name` : branch_name에 해당하는 branch로 전환

	+ ` git checkout -b branch_name` : branch_name에 해당하는 branch를 생성하고, 해당 branch로 전환

#### Checking the changes between branches
* `git log --branches` : branch들의 commit history를 확인, Head가 가리키는 것이 현재 머물고 있는 branch, option을 주어 여러가지 방법으로 사용

	+ `git log --branches --graph --decorate` : 각각의 branch들의 commit history에 graph option을 주어 확인하기 편하게

	+ `git log --branches --graph -p` : 각각의 branch들의 commit history에서 source상의 변경점들을 확인

* `git log branch_name1..branch_name2` : branch 간의 변경점 확인, branch_name2에 기준으로부터 변화한 대상의 branch의 이름을 넣는 것이 유용, option을 주어 여러가지 방법으로 사용

	+ `git log branch_name1..branch_name2 -p` : branch 간의 source상의 변경점을 확인

* `git diff branch_name1..branch_name2` : branch_name1에 해당하는 branch의 최신 version의 source와 branch_name2에 해당하는 branch의 최신 version간의 source상의 변경점을 확인

#### Merging
* `git merge` : merge는 source를 합치는 기준이 되는 branch로 checkout한 뒤, 해당 branch에서 아래와 같은 command로 merge

	+ `git checkout branch_name1` : branche_name1에 해당하는 branch로 checkout

	+ `git merge branch_name2` : ***(Head가 branch_name1인 상태에서)*** branch_name2의 source 변경점들을 branch_name1로 merge

		- template : master가 default branch이므로, Head가 master인 상태에서 `git merge master branch_name` 하면 branch_name에 해당하는 branch의 source 변경점들을 master로 merge

		- ***서로 다른 branch에서 같은 파일의 같은 부분을 수정하면? Conflict!***

			- 이 경우 merge시 editor가 나타나게되며 사용자가 알아서 잘 수정!

		- merging이 끝나면 `git branch -d branch_name2` 로 branch_name2에 해당하는 branch를 삭제

```bash
<<<<<<< HEAD # checkout한 branch (eg. master branch)
hi! master 
======= # branch의 경계, 이 예제에서는 서로 다른 브랜치에서 같은 파일의 같은 부분 (hi! 뒷 부분) 수정해서 충돌
hi! develop
>>>>>>> develop # checkout한 branch로 merge되는 branch (eg. develop branch)
```
```bash
*   commit 100c731567079c22620071ed3ece231a0f6a9531 (HEAD -> master)
|\  Merge: 8dcace3 2e33343
| | Author: aisolab <bsk0130@gmail.com>
| | Date:   Fri Jul 13 16:25:12 2018 +0900
| |
| |     Merge branch 'develop' # 위의 code block에서 master 부분을 지우고 git add, git commit
| |
| * commit 2e3334326fc883f8cd3c98b4dfaa8e4d7e180b79 (develop)
| | Author: aisolab <bsk0130@gmail.com>
| | Date:   Fri Jul 13 16:19:46 2018 +0900
| |
| |     develop v2
| |
* | commit 8dcace3636378e29a9d5b01f2fe89cbdec1dbd78
|/  Author: aisolab <bsk0130@gmail.com>
|   Date:   Fri Jul 13 16:20:16 2018 +0900
|
|       master v2
|
* commit ccd394d62cb6fcc4a7b2643a2dcbc615d9f85622
  Author: aisolab <bsk0130@gmail.com>
  Date:   Fri Jul 13 16:19:05 2018 +0900

      master v1
```

