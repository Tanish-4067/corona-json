from bs4 import BeautifulSoup
import urllib.request
import json
from datetime import date
import subprocess

url = "https://covidindia.org/  "
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "lxml")
state_data = soup.find_all("td", class_="column-1")
confirmed = soup.find_all("td", class_="column-2")
recov = soup.find_all("td", class_="column-3")
death = soup.find_all("td", class_="column-4")
m = len(state_data)
state_list = []
for i in range(m-1):
    temp = {"serial_no": str(i+1),
            "state": state_data[i].text,
            "active_cases": str(int(confirmed[i].text) - int(recov[i].text) - int(death[i].text)),
            "recovered_cases": recov[i].text,
            "death": death[i].text,
            "total_cases": confirmed[i].text}
    state_list.append(temp)
final_tot = soup.find_all("th", class_="column-2")[1].text
final_death = soup.find_all("th", class_="column-4")[1].text
final_rec = soup.find_all("th", class_="column-3")[1].text
temp = {"serial_no": "",
        "state": "Total",
        "active_cases": str(int(final_tot) - int(final_rec)- int(final_death)),
        "recovered_cases": final_rec,
        "death": final_death ,
        "total_cases": final_tot }
state_list.append(temp)
print(state_list)
json_list = json.dumps(state_list, indent=2)
print(json_list)
file = open("coronadata.json", "w")
file.write(json_list)
file.close()
d1 = date.today().strftime("%d_%m_%Y")
print(d1)
file = open("coronadata"+d1+".json", "w")
file.write(json_list)
file.close()
subprocess.call([r'D:\Study\untitled2\Commit.bat'])