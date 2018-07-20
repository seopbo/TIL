# HTML basics
### HTML과 webpage를 구성하는 요소들
**HTML (HyperText Markup Language)** 은 기본적으로 문서를 구조화해주는 지극히 간단한 언어, 웹사이트를 만드는 데에 있어서 아래와 같은 요소들이 모여 하나의 웹페이지를 구성하게된다. 요소와 역할은 아래와 같다.

* html : language로 치면 noun, 뼈대를 잡는다.
* css : language로 치면 adjective, noun을 꾸민다.
* javascript : language로 치면 verb, webpage에 logic을 넣거나 interactivity를 부여한다.

### DOM
**DOM (Document Object Model)** 에 대한 설명은 아래의 link를 참고

* link : https://developer.mozilla.org/ko/docs/About_the_Document_Object_Model

### Boilerplate
HTML 문서는 아래와 같은 기본 뼈대를 두고 만들어진다. 어떤 HTML 문서이든지 간에 아래의 양식은 항상 default

* `<head>` : `<head>`  tag에는 webpage의 header 정보를 넣는다. 아래의 두 가지 tag를 활용한다.
	+ `<title>` : `<title>`tag에는 웹페이지의 이름을 결정한다. browser 상에서 tab에 표시된다.
	+ `<style>` : `<style>`tag에는 `<body>`tag안의 element들의 style을 지정한다. (css)
* `<body>` : `<body>`tag는 webpage에 보여준 실제 내용을 포함한다. 여러 element들로 구성된다.

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

### Basic tags
* `<body>` : `<body>` tag안에는 아래의 여러 tag들을 이용해서 element들을 만들 수 있다. 
  + heading : `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`를 활용하여 제목, 소제목 등을 지정
  + paragraph : `<p>`tag를 활용하여 paragraph를 명시적으로 지정가능
  + unordered list : `<ul>`tag를 활용하여, unordered list를 명시한 뒤, `<li>`tag를 활용하여 list를 만든다.

  ```xml
  <!--unordered list-->
  <ul>
  <li></li>
  <li></li>
  </ul>
  ```

  + ordered list : `<ol>`tag를 활용하여, ordered list를 명시한 뒤, `<li>`tag를 활용하여 list를 만든다.

  ```xml
  <!--ordered list-->
  <ol>
  <li></li>
  <li></li>
  </ol>
  ```

	+ `<img>` : src attibute를 이용하여 image를 넣을 수 있다.

	```xml
	<img src = 'image url'>
	```
	
	+ `<a>` : href attribute를 이용하여 linkㅇ를 생성할 수 있다.

	```xml
	<a href = 'link url'>link url</a>
	```
### Generic container
`<div>` 와 `<span>` 은 둘다 Generic conratiner로 customized structure를 만드는데 사용한다. (eg. element들을 모아서 일괄적으로 css 적용)

Reference : <http://www.clearboth.org/22-generic-containers-8212-the-div-and/>

* `<div>`  : block level container로 주로 block level element를 구조화하는데 사용
	+ ***block level element, block level container는 line당 하나만 들어갈 수 있음*** 
	+ link : <https://developer.mozilla.org/ko/docs/HTML/Block-level_elements> 
* `<span>` :  inline level container로 주로 inline level element를 구조화하는데 사용
	+ ***inline level element, inline level container는 line에 여러개 들어갈 수 있음***
	+ link : <https://developer.mozilla.org/ko/docs/Web/HTML/Inline_elements> 