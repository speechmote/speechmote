from google.cloud import speech, language_v1
import io

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

#TODO: hardReplace will search, using a database, words that are always an emoji and immediately flag for replacement.
def hardReplace(token):
    return token

#TODO: emoteReplace will use an ML model to semantically flag words that can be replaced with an emote.
def emoteReplace(token):
    return token

def tokenize(filePath): 
    sentence = transcribe_file(filePath)

    client = language_v1.LanguageServiceClient()
    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": sentence, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_syntax(request = {'document': document, 'encoding_type': encoding_type})
    token = []
    for t in response.tokens:
        text = t.text.content
        if text[0] == "\'":
            token[-1] = token[-1] + text.lower()
        else:
            token.append(text.lower())

    token = hardReplace(token)
    token = emoteReplace(token)

    return ' '.join(token)