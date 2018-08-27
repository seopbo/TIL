# Package manager

Linux 배포판에 따라 사용할 수 있는 Package manger(apt, yum 등)가 조금씩 다르지만 사용법은 대체로 비슷하다. 예를 들어, Linux 배포판 중 하나인 Ubuntu에서는 사용할 수 있는 Package manger로는 **apt** 가 있다.

## apt

Ubuntu에서 package manager인 **apt** 를 활용하기 위해서는 일단 package manger인 **apt** 를 통해서 설치할 수 있는 package의 목록을 최신화하여야한다. (package의 목록을 download) 이 때 사용하는 명령어는 `apt-get update` 이다.

```bash
$ apt-get update
```

 보통 root 권한이 아니라 user 권한으로 실행하고 있으므로 이때는 `sudo apt-get update` 를 해야한다.

```bash
$ sudo apt-get update
```

`sudo apt-cache search` 뒤에 package 이름을 입력하면 해당 package와 함께 관련된 package를 모두 보여준다.

```bash
$ sudo apt-cache search <package_name>
```

`sudo apt-get install` 뒤에 package 이름을 입력하면 해당 package를 install 한다. `sudo apt-get upgrade` 뒤에 package 이름을 입력하면 해당 package를 최신화한다.

```bash
$ sudo apt-get install <package_name>
```

```bash
$ sudo apt-get upgrade <package_name>
```

만약 `apt-get upgrade` 명령을 특정 package를 명시하지않고 실행하면, `apt-get install` 로 설치한 모든 package를 upgrade한다.

```bash
$ sudo apt-get upgrade
```

설치한 package를 삭제하고 싶다면, `apt-get remove <package_name>`

```bash
$ sudo apt-get remove <package_name>
```
