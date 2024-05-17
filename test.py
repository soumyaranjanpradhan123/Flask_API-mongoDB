from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB configuration
client = MongoClient("mongodb+srv://inventhom:pnq1Xc5eLJtjclWJ@cluster0.fimvkc7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['books']
collection = db["list"]

# Sample data
sample_data = [
    {
        "name": "Harry Potter and the Order of the Phoenix",
        "img": "https://bit.ly/2IcnSwz",
        "summary": "Harry Potter and Dumbledore's warning about the return of Lord Voldemort is not heeded by the wizard authorities who, in turn, look to undermine Dumbledore's authority at Hogwarts and discredit Harry."
    },
    {
        "name": "The Lord of the Rings: The Fellowship of the Ring",
        "img": "https://bit.ly/2tC1Lcg",
        "summary": "A young hobbit, Frodo, who has found the One Ring that belongs to the Dark Lord Sauron, begins his journey with eight companions to Mount Doom, the only place where it can be destroyed."
    },
    {
        "name": "Avengers: Endgame",
        "img": "https://bit.ly/2Pzczlb",
        "summary": "Adrift in space with no food or water, Tony Stark sends a message to Pepper Potts as his oxygen supply starts to dwindle. Meanwhile, the remaining Avengers -- Thor, Black Widow, Captain America, and Bruce Banner -- must figure out a way to bring back their vanquished allies for an epic showdown with Thanos -- the evil demigod who decimated the planet and the universe."
    }
]

# Insert sample data into MongoDB
collection.insert_many(sample_data)

# Create operation
@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    result = collection.insert_one(data)
    return jsonify({'message': 'Book created successfully', 'name': data['name']})

# Read operation
@app.route('/books', methods=['GET'])
def get_books():
    books = list(collection.find({}, {'_id': 0, 'name': 1}))  # Exclude _id field and include name field in response
    return jsonify(books)

# Update operation
@app.route('/books/<book_name>', methods=['PUT'])
def update_book(book_name):
    data = request.json
    result = collection.update_one({'name': book_name}, {'$set': data})
    if result.modified_count:
        return jsonify({'message': 'Book updated successfully'})
    else:
        return jsonify({'message': 'Book not found'})

# Delete operation
@app.route('/books/<book_name>', methods=['DELETE'])
def delete_book(book_name):
    result = collection.delete_one({'name': book_name})
    if result.deleted_count:
        return jsonify({'message': 'Book deleted successfully'})
    else:
        return jsonify({'message': 'Book not found'})

if __name__ == '__main__':
    app.run(debug=True)
