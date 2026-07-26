# User: fullname, birthdate, username, email, password, gender
class User:
    def __init__(self, fullname, birthdate, username,email, password, gender):
        # khai bao bien can dung (private)
        self.__fullname = fullname
        self.__birthdate = birthdate
        self.__username = username
        self.__email = email
        self.__password = password
        self.__gender = gender

    #getter methods
        def get_full_name(self) -> Any:
            return self.__fullname

        def get_birthdate(self) -> Any:
            return self.__birthdate

        # implement getter mothods for username, email, password, and gender
        def get_username(self) -> Any:
            return self.__username

        def get_email(self) -> Any:
            return self.__email

        def get_password(self) -> Any:
            return self.__password

        def get_gender(self) -> Any:
            return self.__gender
    #setter methods
    # sua username (username > 6 ki tu)
    def set_username(self, username) -> None:
        if len (username) > 6:
            self.__username = username # thay doi gia tri moi cho thuoc tinh username
        else:
            print("Username must be longer than 6 characters.")

    # sua password (password > 6 ki tu)
    def set_password(self, old_password, new_password) -> None:
        if old_password == self.__password:
            if len(new_password) > 6:
                self.__password = new_password # thay doi gia tri moi cho thuoc tinh password
            else:
                print("New password must be longer than 6 characters.")
        else:
            print("Old password is incorrect.")


    # gender (male, female, other)
    # gender (male, female, other)
    def set_gender(self, gender):
        if gender in ['male', 'female', 'other']:
            self.__gender = gender # thay doi gia tri moi cho thuoc tinh gender
        else:
            print("Invalid gender. Please choose from 'male', 'female', or 'other'.")