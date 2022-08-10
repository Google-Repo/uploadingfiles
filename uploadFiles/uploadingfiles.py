import dropbox

class uploadingfiles:
    def __init__(self,access_token):
        self.at=access_token

    def uploadFile(self,file_from,file_to):
        f=open(file_from,'rb')
        f=f.read()
        dbx=dropbox.Dropbox(self.at)

        if file_from!='' and file_to!='':
            dbx.files_upload(file_from,file_to)
            print("Your files have been uploaded")
        else:
            print("Sorry we need both the file location and file storage to proceed !")

def main():
    print("Welcome to python based dropbox cloud storage services!")
    print("")

    at=input("Enter your DB access token: ")
    user=uploadingfiles(at)
    print("")

    while True:
       yn=input("Would you like to upload files to dropbox ? (y/n): ").lower()
       print("")

       if yn=='y':
        ff=input("Enter the file name you would like to upload: ")
        ft=input("Enter the folder where you would like to upload your file on dropbox: ")
        ft='/'+ft+'/'+ff
        print("")

        user.uploadFile(ff,ft)
       elif yn=='n':
        print("Thanks for using our program!")
       else:
         print("Answer in y/n, not in any other character")

       print("") 

main()



