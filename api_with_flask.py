from flask import Flask, jsonify



app = Flask(__name__)

@app.route('/factorial/<int:n>')
def factorial(n):
 
    a=1
 
    for i in range(1,n+1):

    

        a = a*i
        # print(a)
    result = {
        "Number": n,
        "Factorial": a,
    }

    return jsonify(result)
    



if __name__=="__main__":
    app.run(debug=True)