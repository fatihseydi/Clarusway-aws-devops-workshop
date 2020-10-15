from flask import Flask, render_template, request

app = Flask(__name__)


converted_list = [(1000*60*60, "hour/s"), (1000*60, "minute/s"), (1000, "second/s"), (1, "milisecond/s")]
result = ""
while True:
    milisecond = input("Please enter a milisecond value: ")
    if milisecond == "exit":
        print("Exiting the program... Good Bye")
        break
    if not milisecond.isdigit() or int(milisecond) == 0:
        print("Print a valid milisecond value, please")
        continue
    else:
        milisecond = int(milisecond)
        for i, text in converted_list:
            division = milisecond // i
            if not division == 0:
                result += str(division) + " " + text + " "
                milisecond = milisecond - division * i
    break
print(result)

@app.route('/', methods=['GET'])
def main_get():
    return render_template('index.html', developer_name='Fatih', not_valid=False)
@app.route('/', methods=['POST'])
def main_post():
    alpha = request.form['number']
    if not alpha.isdecimal():
        return render_template('index.html', developer_name='Fatih', not_valid=True)
    number = int(alpha)
    if not 0 < number < 4000:
        return render_template('index.html', developer_name='Fatih', not_valid=True)
    return render_template('result.html', number_decimal = number , number_roman= convert(number), developer_name='Fatih')

if __name__ == '__main__':
    app.run(debug=True)
