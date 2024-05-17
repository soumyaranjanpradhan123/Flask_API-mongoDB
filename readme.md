# Run the Flask server:

python app.py

The server will start running at http://127.0.0.1:5000/.

## Endpoints
Create a Book

# URL: /books
# Method: POST
# Request Body:

{
    "name": "Book Title",
    "img": "https://example.com/image.jpg",
    "summary": "Book summary here."
}


# Response:

{
    "message": "Book created successfully",
    "name": "Book Title"
}

## Get All Books
# URL: /books
# Method: GET
# Response:

[
    {
        "name": "Book 1"
    },
    {
        "name": "Book 2"
    }
]

## Update a Book
# URL: /books/<book_name>
# Method: PUT
# Request Body:

{
    "img": "https://example.com/new-image.jpg",
    "summary": "Updated summary here."
}

# Response:

{
    "message": "Book updated successfully"
}

## Delete a Book
# URL: /books/<book_name>
# Method: DELETE
# Response:

{
    "message": "Book deleted successfully"
}


