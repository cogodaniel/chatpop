from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()

synthesis_input = texttospeech.SynthesisInput(
    text="Digite 1 para ouvir o número de participantes da sala..."
)

voice = texttospeech.VoiceSelectionParams(
    language_code="pt-BR",
    name="pt-BR-Neural2-B"
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16,
    sample_rate_hertz=8000
)

response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config
)

with open("menu.wav", "wb") as out:
    out.write(response.audio_content)
