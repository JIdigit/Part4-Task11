def error_dec(func):
    def wrapper(*args, **kwargs):
        print(func())
        if func() == True:
            raise Exception('No username defined!')
        elif func() == False:
            raise Exception("No password to change!")
        elif func() == 'hey':
            raise Exception('hahahah lashara')
        return ''
    return wrapper

def get_return(func):
    def wrapper():
        if func() == 'account':
            return True
        elif func() == 'password':
            return False 
        return 'hey'

    return wrapper

class User:

    @error_dec
    @get_return
    def get_account_balance():
        return 'account'

    @error_dec
    @get_return
    def change_password():
        return 'password'
user = User()
# print(user.get_account_balance()) 

print(user.change_password())


    
