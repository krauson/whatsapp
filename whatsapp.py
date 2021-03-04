import pywhatkit


def send_greet(contact_num: str):

    msg = 'כבר אמרו לך שאתה אהוב וטוב מספיק היום? ;)'
    hours = 10
    minutes = 0
    pywhatkit.sendwhatmsg(contact_num, msg, hours, minutes)


hagai = '+972546995552'
barak = '+972504081472'
send_greet(barak)