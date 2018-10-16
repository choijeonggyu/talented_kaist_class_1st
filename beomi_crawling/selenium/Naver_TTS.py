# 아마존 polly 테스트 <- 네이버 할려다가 안되서 아마존 .TTS 하게 되었네..
from boto3 import client

polly = client("polly", region_name="ap-northeast-2")
response = polly.synthesize_speech(
        Text="안녕하세요. 제 이름은 서연이에요! 저는 새내기 아마존 폴리 음성 비서입니다. 텍스트를 입력하시면 읽어드릴께요.",
        OutputFormat="mp3",
        VoiceId="Seoyeon")

stream = response.get("AudioStream")

with open('aws_test_tts.mp3', 'wb') as f:
    data = stream.read()
    f.write(data)
