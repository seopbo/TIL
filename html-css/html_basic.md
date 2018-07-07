# HTML basics
### Notion
**HTML (HyperText Markup Language)** 은 기본적으로 문서를 구조화해주는 지극히 간단한 언어, 웹사이트를 만드는 데에 있어서 아래와 같은 요소들이 모여 하나의 웹페이지를 구성하게된다. 요소와 역할은 아래와 같다.

- html : language로 치면 noun, 뼈대를 잡는다.
- css : language로 치면 adjective, noun을 꾸민다.
- javascript : language로 치면 verb, webpage에 logic을 넣거나 interactivity를 부여한다.

### boilerplate
HTML 문서는 아래와 같은 기본 뼈대를 두고 만들어진다. 어떤 HTML 문서이든지 간에 아래의 양식은 항상 default

- head : `<head>` tag에는 webpage의 header 정보를 넣는다. 아래의 두 가지가 tag를 활용한다.

	- title : `<title>` tag에는 웹페이지의 이름을 결정한다. browser 상에서 tab에 표시된다.
	- style : `<style>` tag에는 `<body>` tag안의 element들의 style을 지정한다. (css)

- body : `<body>` tag는 webpage에 보여준 실제 내용을 포함한다. 여러 element들로 구성된다.

```xml
<!DOCTYPE html>
<html>
<head>
	<title></title>
    <style></style>
</head>
<body>
</body>
</html>
```