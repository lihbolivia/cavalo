import pyautogui as pg

while True:
    a= pg.confirm("você é um cavalo?" , buttons=["sim","nao"])
    if a=="sim":
        break
   
    elif a=="nao":
         a= pg.confirm("voce tem certeza?" , buttons=["sim","nao"])
  
         if a=="sim":
          a=pg.confirm("isso é o que um cavalo diria🤔", buttons=["sim","tem razao"]) 
          
         elif a=="nao":
             a=pg.confirm("você é um cavalo mas não sabe.", buttons=["ok","ok"])
    if a=="ok":
         break
             

   
    if a=="sim":
           a= pg.confirm("então voce é um cavalo?", buttons=["sim", "sim"])
           break
    elif a=="tem razao":
         
            a= pg.confirm("então voce é um cavalo?", buttons=["sim", "sim"])
            break 
