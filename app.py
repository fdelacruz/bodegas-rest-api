from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': 'Dollar Store',
        'items': [
            {
                'name': 'Cheap Item',
                'price': .99
            }
        ]
    }
]

# POST - used to RECEIVE data
# GET  - used to SEND data back only


# POST /store data: {name :}
@app.route('/store', methods=['POST'])
def create_store():
    pass


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass


# GET /store
@app.route('/store')
def get_stores():
    pass


# POST /store/<string:name>/item data: {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store():
    pass


if __name__ == '__main__':
    app.run()
