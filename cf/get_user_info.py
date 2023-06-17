import requests
import json
from string import ascii_letters


class Parser:
    def __init__(self, handle: str) -> None:
        self.link = 'https://codeforces.com/api/user.info?'
        self.handle = handle
        self.HEADERS = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }

        self.data = None
        self.get_user_info()

    def validate(self) -> bool:
        return all(map(lambda c: c in ascii_letters, self.handle))

    def get_user_info(self) -> None:
        if not self.validate():
            return

        url = f"{self.link}handles={self.handle}"
        r = requests.get(url, headers=self.HEADERS)
        self.data = json.loads(r.text)

    def get_status(self) -> str:
        if self.data is None or self.data['status'] == 'FAILED':
            return "failed"
        else:
            return "ok"

    def get_comment(self) -> str:
        return self.data['comment'] if self.data is not None else "None"

    def get_user_city(self) -> str:
        return f"{self.data['result'][0]['country']}, {self.data['result'][0]['city']}"

    def get_user_rating(self) -> str:
        return self.data['result'][0]['rating']

    def get_user_max_rating(self) -> str:
        return self.data['result'][0]['maxRating']

    def get_user_friend_count(self) -> str:
        return self.data['result'][0]['friendOfCount']

    def get_user_title_photo(self) -> str:
        return self.data['result'][0]['titlePhoto']

    def answer(self) -> str:
        if self.get_status() == "failed":
            return self.get_comment()

        res = f'Результаты для {self.handle}:\n'
        res += f"Город: {self.get_user_city()}\n"
        res += f"Рейтинг: {self.get_user_rating()}\n"
        res += f"Максимальный рейтинг: {self.get_user_max_rating()}\n"
        res += f"Количество друзей: {self.get_user_friend_count()}"

        return res
