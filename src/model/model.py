from google.cloud import language_v1
import requests


def alwaysEmotes(token):
    client = language_v1.LanguageServiceClient()

    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": token, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type})
    tokens = []
    for entity in response.entities:
        tokens.append(entity.name)
    return tokens

def getEmojiCode(sentenceTokens, tokens): 
    emojis = {}
    for t in sentenceTokens:
        URL = "https://emoji-api.com/emojis?search=" + str(t) + "&access_key=66f8208d04c5039148d7be92bd42549a09d6bc38"
        r = requests.get(url = URL)
        data = r.json()
        if data == None and t in tokens:
            emojis[t.lower()] = (":" + t.lower() + ":")
        elif data == None or t not in tokens:
            emojis[t.lower()] = t
        else:
            emojis[t.lower()] = (data[0]['character'])
    return emojis

def tokenize(sentence): 
    tokens = alwaysEmotes(sentence)
    client = language_v1.LanguageServiceClient()
    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": sentence, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_syntax(request = {'document': document, 'encoding_type': encoding_type})
    sentenceTokens = []
    for t in response.tokens:
        text = t.text.content
        if text[0] == "\'":
            sentenceTokens[-1] = sentenceTokens[-1] + text.lower()
        else:
            sentenceTokens.append(text.lower())
    emojis = getEmojiCode(sentenceTokens, tokens)
    sentence = []
    for emoji in emojis.keys():
        sentence.append(emojis[emoji])
    return ' '.join(sentence)