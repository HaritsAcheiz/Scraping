from bs4 import BeautifulSoup
import requests

def extract():
    # Waktu: 21 September 2022, 18:57:53 WIB
    # Magnitudo: 5.1
    # Kedalaman: 59 km
    # Lokasi: LS = 6.06, BT = 131.18
    # Pusat Gempa: 178 km BaratDaya MALUKUTENGGARA
    # Keterangan: tidak berpotensi TSUNAMI
    # :return:

    # eq_data = {}
    # eq_data['datetime'] = {'date':'21 September 2022','time': '18:57:53 WIB'}
    # eq_data['magnitude'] = 5.1
    # eq_data['depth'] = 59
    # eq_data['location'] = {'ls':6.06,'bt':131.18}
    # eq_data['center'] = '178 km BaratDaya MALUKUTENGGARA'
    # eq_data['remark'] = 'tidak berpotensi TSUNAMI'

    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        print("Not-Responded")
        content = None
    if content == None:
        result = ("Failed")
    else:
        result = (content.text)

    return result


def view(result):
    data ={
        "Date": "",
        "Time": "",
        "Magnitude": "",
        "Depth": "",
        "Location":
            {
                "LS": "",
                "BT": ""
            },
        "Center": "",
        "Remark": ""
    }

    if result is not None:
        source = BeautifulSoup(result, "html.parser")
        classSpan = "col-md-6 col-xs-6 gempabumi-detail no-padding"
        data["Date"] = source.find("div", {"class": classSpan}).text.split("\n")[2].split(", ")[0]
        data["Time"] = source.find("div", {"class": classSpan}).text.split("\n")[2].split(", ")[1]
        data["Magnitude"] = source.find("div", {"class": classSpan}).text.split("\n")[3]
        data["Depth"] = source.find("div", {"class": classSpan}).text.split("\n")[4]
        data["Location"]['LS'] = source.find("div", {"class": classSpan}).text.split("\n")[5].split(" - ")[0]
        data["Location"]['BT'] = source.find("div", {"class": classSpan}).text.split("\n")[5].split(" - ")[1]
        data["Center"] = source.find("div", {"class": classSpan}).text.split("\n")[6]
        data["Remark"] = source.find("div", {"class": classSpan}).text.split("\n")[7]
        print("Last earthquake detected")
        print(data["Date"])
        print(data["Time"])
        print(data["Magnitude"])
        print(data["Depth"])
        print(data["Location"])
        print(data["Center"])
        print(data["Remark"])
        print("Finished")
    else:
        print("None")
        print("Finished")

    # print(f"Location: LS = {result['location']['ls']}, BT = {result['location']['bt']}")
    # print(f"Center: {result['center']}")
    # print(f"Remark: {result['remark']}")
