<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Predictions</title>
</head>

<body>
 <a href="/hello/finpac">Home</a>

    <p>
    Loan: {{ tuition }}
    </p>

    <form action="/calculate" method="post">
      <p>
      Enter an interest rate: <input type="text" name="living" id="livingBox" size=10 value="">
      <br>
      </p>
      <p>
      Enter an amount of years to pay off the debt: <input type="text" name="travel" id="travelBox" size=10 value="">
      <br>
      </p>
      <input type="submit" value="Calculate Tip">
      <hr>
      <div id="outputDiv"></div>
    </form>
</body>
</html>
