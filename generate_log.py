import requests
from lib.generate_log import generate_log

def fetch_data():
    """Fetch data from a public API using requests."""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {}

if __name__ == "__main__":
    # Fetch data from public API
    post = fetch_data()
    title = post.get("title", "No title found")
    print("Fetched Post Title:", title)

    # Log data entries to be written
    log_data = [
        "User logged in",
        "User updated profile",
        f"Fetched API data - Post Title: {title}",
        "Report exported"
    ]

    # Generate log file using modular function
    generate_log(log_data)
