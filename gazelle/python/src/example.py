import requests


def call_hello_world():
  url = "http://localhost:8080"
  response = requests.get(url)
  if response.status_code == 200:
    print("Response from server:", response.text)
  else:
    print("Failed to get response from server", response.status_code)


if __name__ == "__main__":
  call_hello_world()
