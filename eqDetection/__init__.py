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
                "Long": "",
                "Lat": ""
            },
        "Center": "",
        "Remark": ""
    }

    if result is not None:
        source = BeautifulSoup(result, "html.parser")
        classSpan = "col-md-6 col-xs-6 gempabumi-detail no-padding"
        source = source.find("div",{"class": classSpan})
        source = source.findChildren("li")
        print("Last earthquake detected")
        for i in range(len(source)):
            if i == 0:
                sourceList = source[i].text.split(", ")
                data["Date"] = sourceList[0]
                data["Time"] = sourceList[1]
            elif i == 1:
                data["Magnitude"] = source[i].text
            elif i == 2:
                data["Depth"] = source[i].text
            elif i == 3:
                sourceList = source[i].text.split(" - ")
                data["Location"]["Long"] = sourceList[0]
                data["Location"]["Lat"] = sourceList[1]
            elif i == 4:
                data["Center"] = source[i].text
            elif i == 5:
                data["Remark"] = source[i].text
        for i in data:
            print(f"{i}: {data[i]}")
        print("Finished")
    else:
        print("None")
        print("Finished")

    # print(f"Location: LS = {result['location']['ls']}, BT = {result['location']['bt']}")
    # print(f"Center: {result['center']}")
    # print(f"Remark: {result['remark']}")
