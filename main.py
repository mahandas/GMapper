from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'


@app.route('/')
def sessions():
    return render_template('disclaimer.html')
    
@app.route('/MapApp/<latty0>/<longy0>')
def handle_my_custom_event(latty0,longy0):
    print(str(latty0))
    print(str(longy0))
    return render_template('waiter.html', latty=latty0, longy=longy0)   

if __name__ == '__main__':
    app.run(debug=True)

