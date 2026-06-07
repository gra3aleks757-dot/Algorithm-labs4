import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}      
        self.reverse_map = {}  

    def _generate_code(self, long_url):
        hash_obj = hashlib.md5(long_url.encode())
        return hash_obj.hexdigest()[:6] 

    def add_url(self, long_url):
        if long_url in self.reverse_map:
            return self.reverse_map[long_url]

        code = self._generate_code(long_url)
        while code in self.url_map:
            code = code + '0'
            if len(code) > 10:
                code = code[:10]

        self.url_map[code] = long_url
        self.reverse_map[long_url] = code
        return code

    def get_long_url(self, short_code):
        return self.url_map.get(short_code)

    def exists(self, short_code):
        return short_code in self.url_map

    def get_all_links(self):
        return dict(self.url_map)

    def update_long_url(self, short_code, new_long_url):
        if short_code not in self.url_map:
            return False
        
        old_long_url = self.url_map[short_code]
        self.url_map[short_code] = new_long_url
        del self.reverse_map[old_long_url]
        self.reverse_map[new_long_url] = short_code
        return True


def main():
    shortener = URLShortener()

    while True:
        print("\n" + "="*40)
        print("СОКРАЩАТЕЛЬ ССЫЛОК")
        print("1. Добавить ссылку")
        print("2. Получить длинную ссылку")
        print("3. Проверить существование кода")
        print("4. Показать все ссылки")
        print("5. Изменить длинную ссылку (№9)")
        print("0. Выход")
        print("="*40)

        choice = input("Выберите действие: ")

        if choice == '1':
            url = input("Введите длинную ссылку: ")
            code = shortener.add_url(url)
            print(f"Короткий код: {code}")

        elif choice == '2':
            code = input("Введите короткий код: ")
            url = shortener.get_long_url(code)
            if url:
                print(f"Длинная ссылка: {url}")
            else:
                print("Код не найден!")

        elif choice == '3':
            code = input("Введите короткий код: ")
            if shortener.exists(code):
                print("Код существует")
            else:
                print("Код не существует")

        elif choice == '4':
            links = shortener.get_all_links()
            if links:
                for code, url in links.items():
                    print(f"{code} -> {url}")
            else:
                print("Ссылок пока нет")

        elif choice == '5':
            code = input("Введите короткий код: ")
            new_url = input("Введите новую длинную ссылку: ")
            if shortener.update_long_url(code, new_url):
                print("Длинная ссылка успешно изменена!")
                print(f"Короткий код {code} теперь ведёт на: {new_url}")
            else:
                print("Код не найден!")

        elif choice == '0':
            print("До свидания!")
            break

        else:
            print("Неверный выбор!")


if __name__ == "__main__":
    main()
