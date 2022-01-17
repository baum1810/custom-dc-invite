from flask import Flask, redirect
app = Flask(__name__)
@app.route('/')  
def dc():
  return redirect("YOUR DC INVTE")
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=8000)
