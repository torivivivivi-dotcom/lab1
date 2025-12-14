import requests

url = 'https://dfedorov.spb.ru/python3/sport.txt'
response = requests.get(url)
response.encoding = 'cp1251'
data = response.text
lines = data.split('\n')

sport_count = {}
for line in lines[1:]:
    parts = line.split('\t')
    if len(parts) >= 4:
        sports = parts[3]
        for sport in sports.split(","):
            sport = sport.strip().lower()
            if sport:
                sport_count[sport] = sport_count.get(sport, 0) + 1

sorted_sports = sorted(sport_count.items(), key=lambda x: x[1], reverse=True)

print("Топ-3 самых популярных видов спорта по количеству объектов:")
for i, (sport, count) in enumerate(sorted_sports[:3], 1):
    print(f"{i}. {sport}: {count} объектов")

print("\nПолная статистика по всем видам спорта:")
for sport, count in sorted_sports:
    print(f"{sport}: {count} объектов")
