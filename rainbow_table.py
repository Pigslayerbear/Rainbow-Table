import hashlib
rainbow_table = {}
stolen_data = {}
def hasher(password):
    b = bytes(password, 'utf-8')
    m = hashlib.sha256(b)
    m = m.hexdigest()
    return m

def make_RT():
    file = open("common_passwords.txt", "r")
    for password in file:
        hashed = hasher(password.strip('\n'))
        rainbow_table[hashed] = password.strip('\n')

def get_stolen_data():
    file = open("accounts.txt", "r")
    for accounts in file:
        words = accounts.split(" ")
        hashed = words[1]
        username = words[0]
        stolen_data[hashed] = username 
        print(words)

def crack_passwords():
    file = open("cracked_passwords.txt", "a+")
    for hashed_passwords in rainbow_table:
        if stolen_data.get(hashed_passwords):
            file.write("username: " + stolen_data[hashed_passwords] + " ")
            file.write("password: " + rainbow_table[hashed_passwords])
            file.write("\n")
        else:
            file.write("PASSWORD UNCRACKABLE!!!!!!!")
    file.close()
            
        
make_RT()
get_stolen_data()
crack_passwords()
print(stolen_data)
