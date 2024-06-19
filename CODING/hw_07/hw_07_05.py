import re


def capital_text(text):
    # Паттерн для поиска предложений
    pattern = r'(?<=[.!?]) +'

    # Разбиваем текст на предложения по точке, восклицательному и вопросительному знакам
    sentences = re.split(pattern, text)

    # Проходимся по каждому предложению и делаем первую букву заглавной
    capitalized_sentences = []
    for sentence in sentences:
        # Если предложение состоит из пробелов, игнорируем его
        if not sentence.strip():
            capitalized_sentences.append(sentence)
            continue

        # Делаем первую букву заглавной
        capitalized_sentence = sentence.lstrip().capitalize()
        capitalized_sentences.append(capitalized_sentence)

    # Объединяем предложения в один текст и возвращаем его
    return ' '.join(capitalized_sentences)
