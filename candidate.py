class HRCandidate:
    def __init__(self, name=None, email=None):
        self.user_message = None
        self.name = name
        self.email = email
        self.check_email_validity()

    def check_email_validity(self):
        if self.email is None:
            print("please provide email")
            raise ValueError("Email not valid")

    def prepare_outreach(self, hr_message, final_message_template):
        """
        this method creates the message to be sent
        :return: message
        """

        final_message = final_message_template.format(name=self.name, email=self.email, hr_message=hr_message)

        return final_message


def get_user_message():
    hr_message = input("Please type your message. ")
    return hr_message


def get_user_template():
    hr_custom_template = input(
        "Please type your message template. Use {name} to place candidate's name."
        "Use {email} to place candidate's email."
        "Use {hr_message} to place you previously provided message. ")
    return hr_custom_template


test_candidate = HRCandidate(name="Adam Smith", email="adamsmith@gugil.com")
print(test_candidate.prepare_outreach(get_user_message(), get_user_template()))
