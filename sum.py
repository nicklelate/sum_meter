from firebase import firebase
import datetime
import pytz
import time

firebase = firebase.FirebaseApplication('https://cmudigitaltwin-default-rtdb.asia-southeast1.firebasedatabase.app/', None)
power = []
energy = []
nameP = ['818 room/Switch/power_energy/L01_L02_L03_L07_L08_L09/Power','818 room/Switch/power_energy/L04_L05_L06/Power','dummy']
nameE = ['818 room/Switch/power_energy/L01_L02_L03_L07_L08_L09/Energy','818 room/Switch/power_energy/L04_L05_L06/Energy','dummy']

while True:
  timestamp = datetime.datetime.now(pytz.timezone('Asia/Bangkok'))
  timestamp = f'{timestamp.strftime("%Y")}-{timestamp.strftime("%m")}-{timestamp.strftime("%d")} {timestamp.strftime("%X")}'

  for i in range(3):
    power.append(firebase.get(f'https://cmudigitaltwin-default-rtdb.asia-southeast1.firebasedatabase.app/818 room/Airconditioner/A0{i+1}/Power', ''))
  for i in nameP:
    power.append(firebase.get(f'https://cmudigitaltwin-default-rtdb.asia-southeast1.firebasedatabase.app/{i}', ''))
  power.append(firebase.get(f'https://cmudigitaltwin-default-rtdb.asia-southeast1.firebasedatabase.app/818 room/Power/Power', ''))
  print(power)
  meter_power = sum(power)
  meter_power = round(meter_power, 4)
  power.clear()

  for i in range(3):
    energy.append(firebase.get(f'https://cmudigitaltwin-default-rtdb.asia-southeast1.firebasedatabase.app/818 room/Airconditioner/A0{i+1}/Energy', ''))
  for i in nameE:
    energy.append(firebase.get(f'https://cmudigitaltwin-default-rtdb.asia-southeast1.firebasedatabase.app/{i}', ''))
  energy.append(firebase.get(f'https://cmudigitaltwin-default-rtdb.asia-southeast1.firebasedatabase.app/818 room/Power/Energy', ''))
  print(energy)
  meter_energy = sum(energy)
  meter_energy = round(meter_energy, 4)
  energy.clear()

  firebase.put('https://cmudigitaltwin-default-rtdb.asia-southeast1.firebasedatabase.app/818 room/Meter','Datetime',timestamp)
  print(timestamp)
  firebase.put('https://cmudigitaltwin-default-rtdb.asia-southeast1.firebasedatabase.app/818 room/Meter','Power',meter_power)
  print('Power Updated',meter_power)
  firebase.put('https://cmudigitaltwin-default-rtdb.asia-southeast1.firebasedatabase.app/818 room/Meter','Energy',meter_energy)
  print('Energy Updated',meter_energy)
  print()
  time.sleep(60)