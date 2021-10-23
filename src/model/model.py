from google.cloud import speech, language_v1
import io
import requests

def transcribe_file(speech_file):

    client = speech.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        audio_channel_count=2,
        sample_rate_hertz=48000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    sentence = ""

    for result in response.results:
        sentence = format(result.alternatives[0].transcript)

    return sentence

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

#TODO: emoteReplace will use an ML model to semantically flag words that can be replaced with an emote.
def emoteReplace(token):
    return token

def getEmojiCode(token): 
    emojis = {}
    for t in token:
        URL = "https://emoji-api.com/emojis?search=" + str(t) + "&access_key=66f8208d04c5039148d7be92bd42549a09d6bc38"
        r = requests.get(url = URL)
        data = r.json()
        if data == None:
            emojis[t] = (":" + t + ":")
        else:
            emojis[t] = (data[0]['character'])
    return emojis

def replace(emojis, tokens):
    for emoji in emojis.keys():
        if emoji in tokens:
            emoteIndex = tokens.index(emoji)
            tokens[emoteIndex] = emojis[emoji]
    return tokens

def tokenize(filePath): 
    sentence = transcribe_file(filePath)
    tokens = alwaysEmotes(sentence)
    emojis = getEmojiCode(tokens)

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

    formatted = replace(emojis, sentenceTokens)
    return ' '.join(formatted)

# print(tokenize("src/model/sample.wav"))