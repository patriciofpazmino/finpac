from bottle import route, get, post, run, template, request
from calc import monthlyPayment, financed

@route('/hello/<name>')
def index(name):
    return template('hack', name=name)


@route('/predictions')
def predictions():
    return template('hack3')


@route('/baruch')
def baruch():
    return template('hack2', tuition=10000)


@post('/calculate')
def calculate_tip():
    living_expenses = float(request.forms.get('living'))
    travel_expenses = float(request.forms.get('travel'))

    

    return template('<p>{{ tip }}</p>', tip=tip)


run(host='localhost', port=8080, reloader=True)
