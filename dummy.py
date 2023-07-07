from firebase import firebase
import time

firebase = firebase.FirebaseApplication('https://cmudigitaltwin-default-rtdb.asia-southeast1.firebasedatabase.app/', None)
dummy = 0
while True:
    firebase.put('https://cmudigitaltwin-default-rtdb.asia-southeast1.firebasedatabase.app/','dummy',dummy)
    print('Record Updated')
    dummy+=1
    time.sleep(30)