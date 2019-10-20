
PLAIN = "plain"
PLAIN_UP = "plain_uppercase"
PLAIN_LO = "plain_lowercase"
JSON = "json"

SUPPORTED = [PLAIN, PLAIN_UP, PLAIN_LO, JSON]


def get_formatted(msg, imie, format):
    result = ""
    if format == PLAIN:
        result = plain_text(msg, imie)
    elif format == PLAIN_UP:
        result = plain_text_upper_case(msg, imie)
    elif format == PLAIN_LO:
        result = plain_text_lower_case(msg, imie)
    elif format == JSON:
        result = format_to_json(msg, imie)
    return result


def format_to_json(msg, imie):
    msg, imie = msg.replace('\\','\\\\'), imie.replace('\\','\\\\')
    msg, imie = msg.replace("{","\{"), imie.replace("{","\{")
    msg, imie = msg.replace("}","\}"), imie.replace("}","\}")
    msg, imie = msg.replace('"',r'\"'), imie.replace('"',r'\"')

    text = ('{ "imie":"' + imie + '", "mgs":"' +
     msg + '"}')
    return text


def plain_text(msg, imie):
    concat= str(imie) + ' ' + str(msg)
    remove_space= " ".join(concat.split())
    escape_strings = remove_space
    escape_unicode = remove_space.encode('ascii', 'ignore').decode("utf-8")
    return escape_unicode


def plain_text_upper_case(msg, imie):
    a = plain_text(msg.upper(), imie.upper())
    return a


def plain_text_lower_case(msg, imie):
    return plain_text(msg.lower(), imie.lower())

