from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# Flaskアプリケーションの設定
app = Flask(__name__)

# アプリケーションと同じディレクトリにデータベースを配置
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "database.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# データベースのインスタンスを作成
db = SQLAlchemy(app)

# モデルを定義（テーブル構造）
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.name}, {self.number}>'

# データベースを初期化（最初に一度だけ実行する）
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    number = request.form['number']
    
    # 新しいユーザーをデータベースに追加
    new_user = User(name=name, number=number)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "データがデータベースに保存されました！", "name": name, "number": number})

if __name__ == "__main__":
    app.run(debug=True)
