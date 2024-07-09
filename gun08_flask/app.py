from flask import render_template
from orm_db import *


@app.route('/')
def index():  # put application's code here
    mesaj = "Merhaba Dünya"
    
    return render_template('index.html', mesaj = mesaj)

@app.route('/yonetici')
def yonetici():  # put application's code here
    return 'Yönetici Sayfası'



if __name__ == '__main__':
    app.run()
