import flask
from firebase import Firebase

class FBUsage():
    
    def Post():
        config = {
              "apiKey": "AIzaSyDJIZK3ZCPPu3KNK0-1TuPULfbFGUn0aqI",
              "authDomain": "raspberry-pi-571ec.firebaseapp.com",
              "databaseURL": "https://raspberry-pi-571ec.firebaseio.com/",
              "storageBucket": "raspberry-pi-571ec.appspot.com"
            }
        
        firebase = Firebase(config)
        db = firebase.database()
        storage = firebase.storage()

        try:
            storage.child("Kris' Inbox").child("Image").put("C:/Users/khern/Desktop/Python/Practice.jpg")
            print("Image in storage")
            db.child("Kris' Inbox").child("New").set("1")
            
        except:
            print("Unable to upload image")
            
        
        
    def Retrieve():

        config = {
              "apiKey": "AIzaSyDJIZK3ZCPPu3KNK0-1TuPULfbFGUn0aqI",
              "authDomain": "raspberry-pi-571ec.firebaseapp.com",
              "databaseURL": "https://raspberry-pi-571ec.firebaseio.com/",
              "storageBucket": "raspberry-pi-571ec.appspot.com"
            }
        
        firebase = Firebase(config)
        db = firebase.database()
        storage = firebase.storage()
        
        #new = db.child("Angelica's Inbox").child("New").get()
        new = db.child("Kris' Inbox").child("New").get()
        print(new.val())
        if(new.val() == '1'):
            try:
                storage.child("Kris' Inbox").child("Image").download("Image.jpg")
                print("image found")
                newImg = True
                return newImg
                
            except:
                print("No image")
        else:
            return False

    def Reset():

        config = {
              "apiKey": "AIzaSyDJIZK3ZCPPu3KNK0-1TuPULfbFGUn0aqI",
              "authDomain": "raspberry-pi-571ec.firebaseapp.com",
              "databaseURL": "https://raspberry-pi-571ec.firebaseio.com/",
              "storageBucket": "raspberry-pi-571ec.appspot.com"
            }
        
        firebase = Firebase(config)
        db = firebase.database()

        db.child("Kris' Inbox").child("New").set("0")
        
