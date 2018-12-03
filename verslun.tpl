<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="/static/styles6.css">
	<title>Síða</title>
</head>
<body background="static/gamlagamla.jpg">
	<h1>Verslun</h1>
    <table border="2">
    <thead>
    	<tr>
      		<th scope="col"> Vara </th>
      		<th scope="col"> Verð </th>
    	</tr>
  	</thead>
  	<tbody>
    %for row in rows:
      <tr>
      %for col in row:
        <td><a href="/kaupa">{{col}}</a></td>
      %end
      </tr>
    %end
	</tbody>
    </table>
    <a href="/">Aftur á skráningarsíðu</a>
</body>
</html>