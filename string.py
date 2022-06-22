#Convert half of string into capital 
def full():
   user="childrenareplaying"
   userlen=len(user)
   
   low=user.lower()
   
   uper=user.upper()
   
   split=userlen-(userlen//2)
   
   print (uper[:split]+low[split:])
full()    