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

    def prepare_outreach(self, hr_message):
        """
        this method creates the message to be sent
        :return: message
        """
        if self.name:
            candidate_addressing_string = f"Dear {self.name}"
        else:
            candidate_addressing_string = "Dear Candidate"
        # TODO instead of a pre prepared message get message from user
        # final_message = f'''{candidate_addressing_string},
        # We are pleased to inform you about an open position suitable for your profile.
        # Please contact us at your earliest convenience at {self.email}.
        # Best regards,
        # XYZ Company'''
        final_message = f'''{candidate_addressing_string},
        {hr_message}.
        Please contact us via your registered email address - {self.email}'''

        return final_message


user_message = input("What is your message to candidate? ")

candidate_test2 = HRCandidate(name="Adam Smith", email="adamsmith@gugil.com")
y = candidate_test2.prepare_outreach(user_message)
print(y)
