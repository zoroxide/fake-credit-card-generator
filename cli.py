import api
import time

print(""" 

   __      _                       _ _ _                    _                              _           
  / _|__ _| |_____   __ _ _ ___ __| (_) |_   __ __ _ _ _ __| |  __ _ ___ _ _  ___ _ _ __ _| |_ ___ _ _ 
 |  _/ _` | / / -_) / _| '_/ -_) _` | |  _| / _/ _` | '_/ _` | / _` / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|
 |_| \__,_|_\_\___| \__|_| \___\__,_|_|\__| \__\__,_|_| \__,_| \__, \___|_||_\___|_| \__,_|\__\___/_|  
                                                               |___/                                   
""")
time.sleep(1)
print("Created by https://github.com/zoroxide")
time.sleep(1)

print("""
    Card Detials:
    =============
    card id: {api.id}
	card number: {api.cardnumber}
	card type: {api.cardtype}
	expire date: {api.expire}
	CVV: {api.cvv}
""")
