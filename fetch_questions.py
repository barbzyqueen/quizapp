import requests

def fetch_questions(amount=10, difficulty="easy", category=None):
    """
    Fetch trivia questions from the Open Trivia Database API.

    Args:
        amount (int): Number of questions to fetch.
        difficulty (str): Difficulty level ('easy', 'medium', 'hard').
        category (int): Trivia category ID (optional).

    Returns:
        list: A list of question dictionaries.
    """
    base_url = "https://opentdb.com/api.php"
    params = {
        "amount": amount,
        "difficulty": difficulty,
        "type": "boolean",
    }
    if category:
        params["category"] = category
    
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    data = response.json()
    return data.get("results", [])
