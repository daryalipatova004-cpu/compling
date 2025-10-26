# TextTokenizer

Модуль для токенизации текста разными методами: простая токенизация по пробелам и знакам препинания, токенизация из библиотек nltk и spacy

## Установка

```python
# Создание виртуального окружения (рекомендуется)
python -m venv tokenizer_env
source tokenizer_env/bin/activate  # Linux/Mac (также работает в VS Code на Windows)

# Установка зависимостей
pip install -r requirements.txt

# Дополнительно для spaCy (после установки spaCy)
python3 -m spacy download en_core_web_sm
```

## Пример использования

```python
from tokenizer import TextTokenizer

tokenizer = TextTokenizer()

# Пример текста для токенизации
sample_text = "Hello, world! This is a test sentence. How are you today?"

# Применяем все методы токенизации
results = tokenizer.tokenize_all(sample_text)

# Выводим результаты
for method, tokens in results.items():
    print(f"{method}: {tokens}")
```

## Описание методов

- simple_tokenize() - Простая токенизация по пробелам и знакам препинания
- nltk_tokenize() - Токенизация с использованием NLTK
- spacy_tokenize() - Токенизация с использованием spaCy
- tokenize_all() - Применяет все доступные методы токенизации