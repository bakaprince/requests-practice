import requests

loops=int(input("how many website you want to check"))
for k in range(loops):
    try:
        url = input("Enter website to check: ")
        response = requests.get(url, timeout=5)
        status_code = response.status_code

        if status_code == 200:
            print("Website is working.")
        elif status_code == 404:
            print("Website not found (404).")
    except:
        print(f"Website might be down.")