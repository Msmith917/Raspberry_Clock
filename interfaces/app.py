from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    current_date = "Current Date"
    current_time = "Current Time"
    indoor_temp = "Indoor Temp"
    outdoor_temp = "Outdoor Temp"
    jacket = "Do I need a Jacket?"

    return render_template('index.html', current_date=current_date, current_time=current_time, indoor_temp=indoor_temp, outdoor_temp=outdoor_temp, jacket=jacket)

if __name__ == '__main__':
    app.run()