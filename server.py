from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', row_count = 8, column_count = 8, color_white = "ivory", color_black="black")

@app.route('/<int:row>')
def board_custom_row(row):
  return render_template('index.html', row_count = row, column_count = 8, color_white = "ivory", color_black="black")

@app.route('/<int:row>/<int:column>')
def board_custom_size(row, column):
  return render_template('index.html', row_count = row, column_count = column, color_white = "ivory", color_black="black")

@app.route('/<int:row>/<int:column>/<color1>/<color2>')
def board_custom_full(row, column, color1, color2):
  return render_template('index.html', row_count = row, column_count = column, color_white = color1, color_black = color2)


if __name__=="__main__":
    app.run(debug=True)