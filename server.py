from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {
        'id': 1,
        'first_name': 'Davi',
        'second_name': 'Avelino',
        'age': 17
    },
    {
        "id": 2,
        "first_name": "wesley",
        "second_name": "Jefferson",
        "age": 25
    },
]

#------- GET --------# 
@app.route('/users',methods=['GET'])
def obter_videos():
    return jsonify(users)

#------- GET (specific user) --------# 
@app.route('/users/<int:id>', methods=['GET'])
def get_users_id(id):
    for user in users:
        if user.get('id') == id:
            return jsonify(user)
        
#------- UPDATE --------# 
@app.route('/users/update/<int:id>', methods=['PUT'])
def update_users(id):
    nova_informacao = request.get_json()

    for indice,user in enumerate(users):
        if user.get('id') == id:
            users[indice].update(nova_informacao)
            return jsonify(users[indice])

#------- CREATE --------# 
@app.route('/users/create', methods=['POST'])
def create_users():
    informations = request.get_json()
    users.append(informations)

    return jsonify(users)

#------- DELETE --------# 
@app.route('/users/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    for indice,user in enumerate(users):
        if user.get('id') == id:
            del users[indice]

    return jsonify(users) 

app.run(port=5000,host="localhost",debug=True)







# Enumerate in Python is used to loop over an iterable and automatically provide an index for each item. It returns tuples with the index and corresponding value from the iterable. Example:

# my_list = ['apple', 'banana', 'cherry']
# for index, value in enumerate(my_list):
#     print(index, value)
# Output:
# 0 apple
# 1 banana
# 2 cherry
# This allows you to easily access both the index and the value of each item in the iterable during iteration.