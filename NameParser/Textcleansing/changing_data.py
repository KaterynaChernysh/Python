

def check_contry_code(phone):
    # This changes the begining of a phone according to rules
    if phone[0] == 'A':
        return phone

    if phone[0] == '0':
        if phone[1] == '0' and phone[2] == '4' and phone[3] == '9':
            pass
        else:
            phone = phone[1:]
            phone = '0049' + str(phone)
    else:
        phone = "00" + str(phone)
    return phone


