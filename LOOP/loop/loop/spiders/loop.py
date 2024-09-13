import json
import requests

# Načítanie JSON súboru
with open('dataClean2.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Skontrolujeme, či je načítaný súbor zoznam a získame prvý prvok
if isinstance(data, list) and len(data) > 0:
    first_item = data[0]  # Prvý prvok zoznamu

    # Získanie údajov o eventoch
    events = first_item.get('events', [])

    # Tvoj Telegram bot token
    token = '6928160486:AAFwy-vcEhLiUw6_mWDaykPBn90evij-WOM'
    method = "sendMessage"
    chat_id = -1002381362019  # ID Telegram skupiny

    # Inicializácia prázdneho zoznamu pre uloženie neúspešných odoslaní
    failed_events = []

    # Spracovanie každého eventu
    for event in events:
        title = event.get('title', 'No Title')  # Ošetríme chýbajúce kľúče
        event_date = event.get('date', 'No Date')
        image_url = event.get('image', 'No Image')
        location = event.get('location', 'No location')

        # Kombinovaná správa s názvom, dátumom a odkazom na obrázok
        message = f"Title: {title}\nDate: {event_date}\nImage: {image_url}"
        requests.post('https://api.telegram.org/botID/sendMessage?chat_id=-1002145717073&text=%s' % message)

    # Výpis neúspešných odoslaní (ak nejaké sú)
    if failed_events:
        print("Failed to send messages for the following events:")
        for failed in failed_events:
            print(failed)
    else:
        print("All messages were successfully sent!")

else:
    print("The JSON structure is not as expected or the list is empty.")
