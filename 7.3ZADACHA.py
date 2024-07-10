
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        symbols_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.replace('\n', '')
                    line = line.lower()
                    for symbol in symbols_to_remove:
                        line = line.replace(symbol, '')
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        dict1 = {}
        base_dict1 = self.get_all_words()
        for key, default in base_dict1.items():
            if word in default:
                dict1[key] = default.index(word) + 1
        return dict1


    def count(self, word):
        word = word.lower()
        dict2 = {}
        base_dict2 = self.get_all_words()
        for key, default in base_dict2.items():
            if word in default:
                dict2[key] = default.count(word)
        return dict2


finder2 = WordsFinder('7.3test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
