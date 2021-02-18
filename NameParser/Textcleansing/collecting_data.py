import normalizing_data
import pandas as pd

'''
This gets as an input worksheet of excel file and collects the 
data according to note(see beneath).
This also does the first step of the normalization using file normalizing_data
TODO
To create a data bank for the program to combine and learn how to fix same mistakes
Save in JSON for later working with the app
Save in excel to have clean output (through converting json)
'''
# Constants
ROW_POS = 0


# Note
# I = 8
# J = 9
# K = 10
# L = 11
# M = 12
# U = 20
# O = 14
# AA = 26

class Person(dict):
    num_of_accounts = 0

    # Creates a Person object
    def __init__(self, *args, **kwargs):
        super(Person, self).__init__(*args, **kwargs) # attributes are defined later
        self.__dict__ = self
        # self.id = id  # only correct thing
        # self.fname = fname  # orthographic mistakes, wrong position
        # self.lname = lname  # orthographic mistakes, wrong position
        # self.email = email  # contain multiple emails: private and global
        # self.company = company  # contain department specification or company name
        # self.address = comp_address  # the one that need be easily corrected
        # self.phone = phone  # contain multiple phones: private and global
        Person.num_of_accounts += 1

    def __str__(self):
        # This method makes a pretty output text representation of the account
        res = "*** Holder Info ***\n"
        res += "Num: " + str(Person.num_of_accounts) + "\n"
        res += "ID:" + str(self.id) + "\n"
        res += "Holder:" + self.fname + " " + self.lname + "\n"
        res += "Email: " + str(self.email) + "\n"
        res += "Company: " + str(self.company) + "\n"
        res += "Address: " + str(self.address) + "\n"
        res += "Phone: " + str(self.phone) + "\n"
        return res

    def set_fname(self, fname):
        self.fname = fname

    def set_lname(self, lname):
        self.lname = lname

    def set_id(self, id):
        self.id = id

    def set_email(self, email):
        self.email = email

    def set_company(self, company):
        self.company = company

    def set_address(self, address):
        self.address = address

    def set_phone(self, phone):
        self.phone = phone


# Collecting data
def parse_name_surname(ws): # TODO choose a better name for the function
    '''
    This reads the columns and assign the data to the object.
    TODO Check when Name x = Surname y -> combine
    '''

    user_data_lexicon = {}
    start_row = ROW_POS

    for obj in range(len(ws.index)):
        holder = Person(fname="Anonym", lname="Anonym", id=None, email=None, company=None, address=None, phone=None) # Don't like the code

        # Collect data from columns
        val_id = ws.iloc[start_row][0]

        val_name = ws.iloc[start_row][8] # Repetition in lname/fname fname/lname
        val_surname = ws.iloc[start_row][9]

        val_email = ws.iloc[start_row][10]
        val_gmdText = ws.iloc[start_row][26]
        holder.set_email(parse_email(val_email, val_gmdText))

        val_company = ws.iloc[start_row][12]
        val_department = ws.iloc[start_row][13]
        holder.set_company(parse_company(val_company, val_department))  # Parsing needed

        val_address = ws.iloc[start_row][14] # Parsing needed
        holder.set_address(val_address)

        val_phone = ws.iloc[start_row][11]
        holder.set_phone(parse_phones(val_phone))

        # Combine together
        if pd.notna(val_name):
            # Replace x's and o's with Anonym
            if val_name == "x" and val_surname == "x":
                holder.set_fname("Anonym")
                holder.set_lname("Anonym")
                holder.set_id(val_id)

            elif val_name == "o" and val_surname == "o":
                holder.set_fname("Anonym")# can do nothing because already defined
                holder.set_lname("Anonym")

            else:
                # user_data_lexicon.append(val_name + " " + val_surname)
                holder.set_fname(val_name)
                holder.set_lname(val_surname)
                holder.set_id(val_id)

        #TODO Write in JSON or whatever
        print(holder.__str__())
        start_row += 1

    return user_data_lexicon


def parse_email(val_email, val_gmdText):
    '''
    TODO
        Check the email form (regex) If no match then what?
        TODO
            1) see normalizing_data.email_norm()
    '''
    if val_email and val_gmdText is not None:
        if val_email == val_gmdText == "(null)":
            return "(null)"
        elif val_email == "(null)" and val_gmdText != "(null)":
            val_gmdText = normalizing_data.change_umlaut(str(val_gmdText))
            return val_gmdText
        elif val_email != "(null)" and val_gmdText == "(null)":
            val_email = normalizing_data.change_umlaut(str(val_email))
            return val_email
        else:
            return [val_email, val_gmdText]

def parse_company(val_company, val_department):
    '''
    This normalizes umlauts in given text and combine
    two texts(if K and AA full) in a list
    TODO
        Check company (MT)
        crawler?
        TODO
            1) see normalizing_data.company_norm()
    '''
    if val_company and val_department is not None:
        if val_company == val_department == "(null)":
            return "(null)"
        elif val_company == "(null)" and val_department != "(null)":
            return val_department
        elif val_company != "(null)" and val_department == "(null)":
            return val_company
        else:
            return [val_company, val_department]


def parse_phones(val_phone):
    '''
    TODO
        1) see normalizing_data.phone_norm()
    '''
    if val_phone == "(null)":
        return val_phone
    elif val_phone != "(null)":
        val_phone = normalizing_data.remove_nondigits(val_phone)
        return val_phone


