import random
import time
from iqoptionapi.stable_api import IQ_Option
Iq=IQ_Option("shivxforex@gmail.com","IDEAPAD300")
Iq.connect()
print(Iq.check_connect())
balance_type="PRACTICE"
print(Iq.change_balance(balance_type))
print(Iq.get_balance())
ACTIVES="EURUSD"
duration=1#minute 1 or 5
amount=1
action="put"#put
polling_time = 5
Iq.subscribe_strike_list(ACTIVES,duration)
_,id=Iq.buy_digital_spot(ACTIVES,amount,action,duration)

while True:
    PL=Iq.get_digital_spot_profit_after_sale(id)
    if PL!=None:
        print(PL)
        print(Iq.check_win_digital(id,polling_time))#get the id from Iq.buy_digital
        break
if Iq.check_win_digital(id,polling_time) > 0:
  print("win")
  amount = amount * 2.5
else:
  print("loss")
