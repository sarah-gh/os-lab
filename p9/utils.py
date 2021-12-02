from khayyam import JalaliDatetime
from datetime import datetime, timedelta
from gtts import gTTS
import qrcode


def checkInt(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def to_gregorian_strftime(moment):
    dt = JalaliDatetime.strptime(moment, "%Y/%m/%d")
    return dt.todatetime()

def compare_date(date1) -> bool:
    time1 = to_gregorian_strftime(date1)
    time2 = datetime.now()
    return int((time2 - time1).days / 365)

def text_to_speech(text):
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("voice.ogg")


def qrcode_generate(text):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")