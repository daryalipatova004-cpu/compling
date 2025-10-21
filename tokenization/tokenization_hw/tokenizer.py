"""
Модуль для токенизации текста различными способами
"""

import re

class TextTokenizer:
    def __init__(self):
        """Инициализация токенизатора: не изменяйте эту строчку кода"""
        pass

    def simple_tokenize(self, text):
        """
        Простая токенизация по пробелам и знакам препинания

        Args:
            text (str): Входной текст

        Returns:
            list: Список токенов
        """
        # Реализация простой токенизации
        return re.findall(r"\w+", text)

    def nltk_tokenize(self, text):
        """
        Токенизация с использованием NLTK

        Args:
            text (str): Входной текст

        Returns:
            list: Список токенов или сообщение об ошибке
        """
        # Реализация NLTK токенизации
        try:
            import nltk
            nltk.download('punkt_tab')
            from nltk.tokenize import word_tokenize
            return word_tokenize(text)
        except:
            print('Error occured')
            return None

    def spacy_tokenize(self, text):
        """
        Токенизация с использованием spaCy

        Args:
            text (str): Входной текст

        Returns:
            list: Список токенов или сообщение об ошибке
        """
        # Реализация spaCy токенизации
        try:
            import spacy
            nlp = spacy.load("en_core_web_sm")
            return [t.text for t in nlp(text)]
        except:
            print('Error occured')
            return None

    def tokenize_all(self, text):
        """
        Применяет все доступные методы токенизации

        Args:
            text (str): Входной текст

        Returns:
            dict: Словарь с результатами всех методов
        """
        # Реализация вызова всех методов
        result = {}
        result['simple'] = self.simple_tokenize(text)
        result['nltk'] = self.nltk_tokenize(text)
        result['spacy'] = self.spacy_tokenize(text)
        return result