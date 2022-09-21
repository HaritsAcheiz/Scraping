"""
Earthquake Detection
"""


def extract():
    """
    Waktu: 21 September 2022, 18:57:53 WIB
    Magnitudo: 5.1
    Kedalaman: 59 km
    Lokasi: LS = 6.06, BT = 131.18
    Pusat Gempa: 178 km BaratDaya MALUKUTENGGARA
    Keterangan: tidak berpotensi TSUNAMI
    :return:
    """
    eq_data = {}
    eq_data['datetime'] = {'date':'21 September 2022','time': '18:57:53 WIB'}
    eq_data['magnitude'] = 5.1
    eq_data['depth'] = 59
    eq_data['location'] = {'ls':6.06,'bt':131.18}
    eq_data['center'] = '178 km BaratDaya MALUKUTENGGARA'
    eq_data['remark'] = 'tidak berpotensi TSUNAMI'

    return eq_data


def view(result):
    print("Last earthquake detected")
    print(f"Date: {result['datetime']['date']}")
    print(f"Time: {result['datetime']['time']}")
    print(f"Magnitude: {result['magnitude']}")
    print(f"Depth: {result['depth']}")
    print(f"Location: LS = {result['location']['ls']}, BT = {result['location']['bt']}")
    print(f"Center: {result['center']}")
    print(f"Remark: {result['remark']}")

if __name__ == '__main__':
    print('main_application')
    eq_result = extract()
    view(eq_result)