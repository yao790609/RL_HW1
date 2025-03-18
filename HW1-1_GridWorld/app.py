# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 12:12:13 2025

@author: yao79
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    n = 5  # 預設值
    if request.method == 'POST':
        try:
            n = int(request.form.get('grid_size', 5))
            if n < 3 or n > 10:
                n = 5  # 超出範圍則回到預設值
        except ValueError:
            n = 5  # 非法輸入則回到預設值
    return render_template('app.html', n=n)

if __name__ == '__main__':
    app.run(debug=True)