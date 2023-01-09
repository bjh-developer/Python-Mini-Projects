# Random Activity Generator by bjh-developer, created in Visual Studio Code with Python 3
import json, requests, time

def get_data():
    r = requests.get('https://www.boredapi.com/api/activity/')
    data = r.json()
    print(f"You can try: {data['activity']}")
    if data['link'] == '':
        pass
    else:
        print(f"More info here: {data['link']}")

counter = 1

print("Feeling bored? Look no further, here's an activity you can try!")
time.sleep(2)

while True:
    print(f"----------------Random Activity {counter}-----------------")
    get_data()
    print()
    cont = input("Would you like to have another activity [y/n]: ")
    if cont.lower() == 'n':
        print("Byebye!")
        break
    else:
        counter += 1
        print(f"Round {counter}!")
        time.sleep(2)