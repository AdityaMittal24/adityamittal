from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    """
    Processes an array of data to identify and categorize numbers, alphabets,
    and special characters.
    Method: POST
    Route: /bfhl
    """
    try:
        # Get data from the request body
        data = request.get_json().get('data')

        # Basic validation
        if not isinstance(data, list):
            return jsonify({
                "is_success": False,
                "user_id": "aryan_garg_29072025",
                "error": "Input data must be an array."
            }), 400

        # Initialize response lists and variables
        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        all_alpha_chars = []
        total_sum = 0

        # Process each item in the input array 
        for item in data:
            if isinstance(item, str):
                # Check if item is a number
                if item.isnumeric():
                    num = int(item)
                    total_sum += num
                    if num % 2 == 0:
                        even_numbers.append(str(num)) # Numbers must be returned as strings 
                    else:
                        odd_numbers.append(str(num)) # Numbers must be returned as strings 
                # Check if item is an alphabet or a word
                elif item.isalpha():
                    alphabets.append(item.upper()) # Convert alphabets to uppercase 
                    all_alpha_chars.extend(list(item))
                # Otherwise, it's a special character
                else:
                    special_characters.append(item)
            else:
                # Handle non-string elements if necessary, here we consider them special characters
                special_characters.append(str(item))


        # Generate the concatenated string with alternating caps 
        all_alpha_chars.reverse()
        concat_list = []
        for i, char in enumerate(all_alpha_chars):
            if i % 2 == 0:
                concat_list.append(char.upper())
            else:
                concat_list.append(char.lower())
        concat_string = "".join(concat_list)


        # Construct the successful response object
        response = {
            "is_success": True, [cite: 5]
            "user_id": "aryan_garg_29072025", [cite: 4]
            "email": "aryan.garg.official@chitkara.edu.in", [cite: 8]
            "roll_number": "2110991901", [cite: 8]
            "odd_numbers": odd_numbers, [cite: 1]
            "even_numbers": even_numbers, [cite: 1]
            "alphabets": alphabets, [cite: 1]
            "special_characters": special_characters, [cite: 1]
            "sum": str(total_sum), # Return sum as a string 
            "concat_string": concat_string [cite: 1]
        }

        # Return the JSON response with a 200 status code for success 
        return jsonify(response), 200

    except Exception as e:
        # Graceful exception handling
        return jsonify({
            "is_success": False,
            "user_id": "aryan_garg_29072025",
            "error": f"An error occurred: {str(e)}"
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)