from flask import Flask, request ,jsonify

app = Flask(__name__)

fruit_list = [
    {
        "kiwi": "🥝",
        "stawberry": "🍓",
        "pinapple": "🍍",
        "pear": "🍐",
        "banana": "🍌",
        "grapes": "🍇",
    } 
]

@app.route("/", methods=['GET'])
def ok():
    return {
        "message": "OK"
    }

@app.route("/fruits", methods=['GET'])
def get_fruits():
    if len(fruit_list) > 0:
        return jsonify(fruit_list)
    else:
        "No Fruits."

@app.route("/add-fruit", methods=['POST'])
def add_fruits():
    fruit_name = request.form['name']
    fruit_sticker = request.form['sticker']

    # new_obj = {
    #     fruit_name: fruit_sticker
    # }

    fruit_list[0][fruit_name]=fruit_sticker

    # iter(fruit_list).next()[fruit_name] = fruit_sticker

    return jsonify(fruit_list)



if __name__ == '__main__':
    app.run(debug=True)