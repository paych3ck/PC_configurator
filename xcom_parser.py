import pandas as pd
import requests
import bs4

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

def parse_category(category, pages):
    names = []
    prices = []

    for page in range(pages):
        response = requests.get(f'https://www.xcom-shop.ru/catalog/kompyuternye_komplektyyuschie/{category}/?catalog=page-{page + 1}', headers=headers)
        soup = bs4.BeautifulSoup(response.content, 'html.parser')
        actual_names = soup.find_all('a', class_='catalog_item__name catalog_item__name--tiles')
        actual_prices = soup.find_all('div', class_='catalog_item__new_price')

        for name in actual_names:
            names.append(name.get('title'))

        for price in actual_prices:
            prices.append(''.join(price.text.split()[:-1]))

    return [names, prices]

hdds = parse_category('hdd_zhestkie_diski', 9)
ssds = parse_category('ssd_tverdotelnye_nakopiteliflesh-diski', 27)
power_units = parse_category('bloki_pitaniya', 15)
video_cards = parse_category('videokarty', 11)
sound_cards = parse_category('zvykovye_karty', 1)
cases = parse_category('korpysa_desktop_i_aksessyary', 20)
coolers = parse_category('kylery_i_sistemy_ohlazhdeniya', 28)
motherboards = parse_category('materinskie_platy', 12)
rams = parse_category('modyli_pamyati', 24)
cpus = parse_category('protsessory', 7)

hdds_df = pd.DataFrame({'name': hdds[0], 'price': hdds[1]})
ssds_df = pd.DataFrame({'name': ssds[0], 'price': ssds[1]})
power_units_df = pd.DataFrame({'name': power_units[0], 'price': power_units[1]})
video_cards_df = pd.DataFrame({'name': video_cards[0], 'price': video_cards[1]})
sound_cards_df = pd.DataFrame({'name': sound_cards[0], 'price': sound_cards[1]})
cases_df = pd.DataFrame({'name': cases[0], 'price': cases[1]})
coolers_df = pd.DataFrame({'name': coolers[0], 'price': coolers[1]})
motherboards_df = pd.DataFrame({'name': motherboards[0], 'price': motherboards[1]})
rams_df = pd.DataFrame({'name': rams[0], 'price': rams[1]})
cpus_df = pd.DataFrame({'name': cpus[0], 'price': cpus[1]})

accessories = {
    'Hdds': hdds_df,
    'Ssds': ssds_df,
    'PowerUnits': power_units_df,
    'Videocards': video_cards_df,
    'Soundcards': sound_cards_df,
    'Cases': cases_df,
    'Coolers': coolers_df,
    'Motherboards': motherboards_df,
    'Rams': rams_df,
    'Cpus': cpus_df
    }

writer = pd.ExcelWriter('pc_accessories.xlsx', engine='xlsxwriter')

for accessory in accessories.keys():
    accessories[accessory].to_excel(writer, sheet_name=accessory, index=False)

writer.save()