<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css" href="/static/styles7.css">
	<title>Síða</title>
</head>
<body background="/static/theyblock1.jpg">
	<header>
		<h1>TheyBlock</h1>
	</header>
	<div class="nedri">
		<img src="/static/theyblock1.jpg">

		<div class="fjoldi">
      		<label for="fjoldi" class="fjoldin">Fjöldi</label>  
      		<select name="fjoldi" required>
          		<option value="1" selected>1</option>
          		<option value="2">2</option>
          		<option value="3">3</option>
          		<option value="4">4</option>
          		<option value="5">5</option>
      		</select>
      	</div>

    	<div class="input">
			<form action="/keypt">
     			<input type="submit" value="Kaupa">
 			</form>
 			<form action="/verslun">
     			<input type="submit" value="Til baka">
 			</form>
 		</div>
 
      
</body>
</html>