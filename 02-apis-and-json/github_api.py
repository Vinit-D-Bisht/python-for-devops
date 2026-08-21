import requests,json

def get_info():
    name = str(input("Enter your Github Username: "))
    header={"Accept":"application/json"}
    g_url =f"https://api.github.com/users/{name}"

    try:
        response = requests.get(url = g_url, headers = header)
        response.raise_for_status()
        
        user=response.json()

        print("name:", user["name"])
        print("public_repos:", user["public_repos"])
        print("followers:", user["followers"])
        print("location:", user["location"])
        with open("github_user.json", "w", encoding="utf-8") as f:
            json.dump(user, f, indent=2)
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"GitHub user '{name}' not found Enter valid name.")
        else:
            print(f"HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

get_info()
