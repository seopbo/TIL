# Git github
Remote repository로 [Github](https://github.com/)를 이용하는 방법을 정리

* Reference
	+ [지옥에서 온 Git](https://opentutorials.org/module/2676) 
	+ https://git-scm.com/book/en/v2
	+ https://www.rlee.ai/apt/git
	+ https://github.com/Gyubin/TIL/blob/master/ETC/git_gitflow.md
---

### Using Github as remote repository
#### Preliminary
* [Github](https://github.com/) 가입
	+ [SSH public key 생성](https://git-scm.com/book/ko/v1/Git-%EC%84%9C%EB%B2%84-SSH-%EA%B3%B5%EA%B0%9C%ED%82%A4-%EB%A7%8C%EB%93%A4%EA%B8%B0)
	+ <https://github.com/settings/keys>에서 생성한 SSH public key를 등록

#### Creating remote repository using Github
Github에서 remote repository를 생성하면, 두 가지 방식으로 Github의 remote repository와 local repository를 연동할 수 있음

* Github에서 remote repository를 생성하고, `git clone` 을 활용 (추천)

```bash
# user_name : Github에서의 유저이름
# repository_name : remote repository의 이름
git clone git@github.com:user_name/repository_name.git
```

* Local에서 repository를 생성하고, remote repository와 연동 (이미 local repository에서 version control을 하고 있는 것을 remote repository로 backup 할 때 활용)
	1. project directory를 `git init` 으로 version control 선언 (working directory 화)
		- ***이미 version control 하고 있던 project라면 위 과정 불필요***
	2. Github에 project directory의 이름과 같은 이름으로 remote repository 생성, 그 후 아래와 같이

```bash
# origin은 뒷 부분 (remote repository의 alias)
git remote add origin git@github.com:user_name/repository_name.git
```

#### Interlocking local repository with remote repository
##### push
* local repository를 기준으로 하기 때문에, ***"local repository를 remote repository로 push한다."*** 라고 통칭함
	+ local repository의 특정 branch의 version (commit)을 remote repository의 특정 branch로 push

```bash
git push origin local_branch_name:remote_branch_name
```

* 일반적으로 local repository의 master branch를 remote repository의 master branch로 push하는 게 일반적, 따라서 아래와 같이 설정

```bash
# local repository의 master branch를 remote repository의 master branch로 push하는 경우에는
# 한번 아래의 명령어로 연결해놓으면 그 다음은 git push로 그냥 활용 
git push -u origin master
```

* remote repository에 없는 branch를 local repository에서 만들어서 push하는 경우, remote repository에 해당 branch가 생성됨

```bash
git push origin branch_not_in_remote_repository
```

##### pull
* remote repository의 master branch를 local repository로 master branch로 가져오기

```bash
git pull
```

* remote repository의 specific branch를 local repository의 specific branch로 가져오기

```bash
git pull origin remote_branch_name:local_branch_name
```
