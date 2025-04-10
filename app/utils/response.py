from flask import jsonify

def success_response(data, message="Success"):
    """Return a success response"""
    return jsonify({
        "status": "success",
        "message": message,
        "data": data
    }), 200

def error_response(message, status_code=400):
    """Return an error response"""
    return jsonify({
        "status": "error",
        "message": message
    }), status_code 