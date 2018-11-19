import pyrebase
config = {
    "apiKey" : "AIzaSyCb8xRzfsic8CRqdRr1FBdnSfPrnbg_nIc",
    "authDomain" : "softdev18-a2b9c.firebaseapp.com",
    "databaseURL" : "https://softdev18-a2b9c.firebaseio.com",
    "storageBucket" : "softdev18-a2b9c.appspot.com"
}

firebase = pyrebase.initialize_app(config)