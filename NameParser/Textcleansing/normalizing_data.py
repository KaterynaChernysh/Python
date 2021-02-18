import re

email = "Kuehnlenz.Daniel@dea.de"
email_list = ["(null)", "(null)", "Kräft.Ingo@dea.de", "(null)", "Kuehnlenz.Daniel@dea.de", 'jordan.moritz@sdema.com.de']
phone = "172/(282)96-7-28"


def change_umlaut(string):
    '''
    This normalizes umlauts in given text
    TODO look for build in library
    '''
    string = string.replace("ü", "ue")
    string = string.replace("Ü", "ue")
    # print(string)
    string = string.replace("ö", "oe")
    string = string.replace("Ö", "oe")
    # print(string)
    string = string.replace("ä", "ae")
    string = string.replace("Ä", "ae")
    # print(string)
    string = string.replace("ß", "ss")
    return string

def remove_nondigits(phone):
    '''
    This removes non-digits
    '''
    if phone is not None:
        for num in phone:
            if num in "+ -_.,/()":
                phone = phone.replace(num, '')
    return phone

def email_norm(email_string):
    # Error 'NoneType' if email_string don't match the regex
    '''TODO
        1) Check if in DB
        2) Check if valid (through site?)
    '''
    email_adress_regex = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
    em = email_adress_regex.search(email_string)    # finds right emails
    result = em.group()     # returns string
    return result

def phone_norm(phone):
    # Error 'NoneType' if phone don't match the regex
    '''
    TODO
        1) Check if in DB
        2) Check if matches the regex
        3) Change country code
    '''
    mobile_num_regex = re.compile(r'(((49)|0)+1(5*|6*|7*){2,4}\d{9,})')
    num = mobile_num_regex.search(phone)
    result = num.group()
    return result
