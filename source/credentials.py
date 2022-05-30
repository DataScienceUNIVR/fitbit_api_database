#used to get credential from the user

CLIENT_ID=''
CLIENT_SECRET=''

if __name__ == "__getCredentials__":
    pass

def getCredentials():
    global CLIENT_ID
    global CLIENT_SECRET
    CLIENT_ID = input("inserisci il CLIENT_ID : ")
    CLIENT_SECRET = input("inserisci il CLIENT_SECRET : ")




print(CLIENT_ID)
print(CLIENT_SECRET)