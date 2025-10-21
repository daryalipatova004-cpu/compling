from tokenizer import TextTokenizer

def main():
    tokenizer = TextTokenizer()

    # Пример текста для токенизации
    sample_text = "There is nobody to blame, but I would really love to... Why are you here today? \nget out!"

    # Применяем все методы токенизации
    results = tokenizer.tokenize_all(sample_text)

    # Выводим результаты
    for method, tokens in results.items():
        print(f"{method}: {tokens}")

if __name__ == "__main__":
    main()