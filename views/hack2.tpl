<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Predictions</title>
</head>

<body>
 <a href="hack.htm">Home</a> 
   
    <p>
    Tuition: {{ tuition }}
    </p>   
      
I   <form action="/calculate" method="post">
      <p>
      Enter living expenses: $<input type="text" name="living" id="livingBox" size=10 value="">
      <br>
      Tip percentage: 15%
      </p> 
      <p>
      Enter travel expenses: $<input type="text" name="travel" id="travelBox" size=10 value="">
      <br>
      Tip percentage: 15%
      </p> 
      <input type="submit" value="Calculate Tip"> 
      <hr>
      <div id="outputDiv"></div>
    </form>
</body>
</html>
