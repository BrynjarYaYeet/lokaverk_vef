<!DOCTYPE html>
<html> 
  <head>
    <meta charset="utf-8">
    <title>Félagaskrá</title>
  </head>
  <body>
    <h2>Félagaskrá</h2>
    <p>The member team are as follows:</p>
    <table border="1">
    %for row in rows:
      <tr>
      %for col in row:
        <td>{{col}}</td>
      %end
      </tr>
    %end
    </table>
    <a href="/">Aftur á skráningarsíðu</a>
  </body>
</html>  