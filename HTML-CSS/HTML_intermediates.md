# HTML intermediates
### Intermediate tags
#### table
`<table>` tag로 table을 생성하며 다음과 같은 tag를 활용하여, element를 만들 수 있다.

* `<tr>` : table row를 생성, 아래의 두 가지 tag를 < `<tr>` tag안에는 다음의 tag를 사용할 수 있다.
	+ `<th>` : table head를 의미하며, table에서 column의 name을 명시하는 부분
	+ `<td>` : table data를 의미하며, table에서 column에 넣어줄 data를 넣는 부분
* `<thead>` : HTML상에서 table head에 해당하는 `<tr>` tag에 대하여 명시적으로 선언, 구별해주는 용도
* `<tbody>` : HTML상에서 table data에 해당하는 `<tr>` tag들에 대하여 명시적으로 선언, 구별해주는 용도

```xml
<table>
    <thead>
        <tr>
            <th></th>
            <th></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>
```

#### Getting user inputs
* `<input>` : `<input>` tag는 user의 input을 받을 때 사용하는 tag로 type attribute를 이용하여 input의 type을 결정한다.
	+ `<input type='text'>`
	+ `<input type='date'>`
	+ `<input type='color'>`
	+ `<input type='file'>`
	+ `<input type='checkbox'>`
* `<form>` : `<form>` tag는 ***block level container로 user의 input을 getting 할 수 있는 여러 HTML tag들을 묶어서 관리할 때 사용한다.*** 아래의 두 개의 attribute를 주로 활용하며 더 자세한 내용은 아래의 link를 참고 
  + link : <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form>
  + action : data를 어느 url로 보낼 지 
  + method : HTTP의 어떤 method를 사용할 지 (get/post)

