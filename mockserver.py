from flask import Flask, request, jsonify, abort
import random

app = Flask(__name__)  # 实例化一个Flask对象


@app.route("/api/user/reg/", methods=["POST"])
def reg():
    if not request.json or not 'name' in request.json or not 'password' in request.json:
        abort(404)
    res = [
        {
            "code": "100000",
            "msg": "成功"
        },
        {
            "code": "100001",
            "msg": "失败，用户已存在"
        },
        {
            "code": "100002",
            "msg": "失败，添加用户失败"
        }
    ]

    return jsonify(random.choice(res))


if __name__ == '__main__':
    app.run()
