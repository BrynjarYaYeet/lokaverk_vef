<!DOCTYPE html>
<html>
<head>
	<title>innskráning</title>
	<link rel="stylesheet" type="text/css" href="/static/styles2.css">
</head>
<body background="/static/ganka.jpg">
	<div class="efri">
		<h3>Búa Til Nedri</h3>
		<form method="post" action="/nyrnotandi" accept-charset="ISO-8859-1">
			Notendanafn: <br>
			<input type="text" name="user" required><br>
			Lykilorð:<br>
			<input type="text" name="pass" required><br>
			<input type="submit" value="Nýskrá">
			<input type="reset" value="Hreinsa">
		</form>
	</div>

	<div class="nedri">
		<h3>Innskráning</h3>
		<form method="post" action="/innskra" accept-charset="ISO-8859-1">
			Notendanafn: <br>
			<input type="text" name="user" required><br>
			Lykilorð:<br>
			<input type="text" name="pass" required><br>
			<input type="submit" value="Innskrá">
			<input type="reset" value="Hreinsa">
		</form>
		<a href="/">Tilbaka</a>
	</div>


</body>
</html>