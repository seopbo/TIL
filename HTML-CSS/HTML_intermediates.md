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
