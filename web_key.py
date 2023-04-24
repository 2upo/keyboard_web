import keyboard

a ="backtick,1,2,3,4,5,6,7,8,9,0,minus,equals,backspace,tab,q,w,e,r,t,y,u,i,o,p,left-brace,right-brace,backslash,caps-lock,a,s,d,f,g,h,j,k,l,semicolon,apostrophe,enter,left-shift,z,x,c,v,b,n,m,comma,period,slash,right-shift,left-ctrl,left-win,left-alt,spacebar,right-alt,right-win,num-divide,num-multiply,num-subtract,num-7,num-8,num-9,num-add,num-4,num-5,num-6,num-1,num-2,num-3,num-enter,num-0,num-decimal"

b = a.split(",")

ex = {'backtick': '`', 'minus': '-', 'equals': '=', 'left-brace': '[', 'right-brace': ']', 'caps-lock': 'caps lock', 'left-shift': 'left shift', 'right-shift': 'right shift', 'left-ctrl': 'left ctrl', 'left-win': 'left windows', 'left-alt': 'left alt', 'right-alt': 'right alt', 'right-win': 'right windows'}

keyboard.wait('enter')

# for i in b:
#     if i in ex:
#         i = ex.get(i)
#     try:
#         keyboard.press_and_release(i)
#     except:
#         print(i)

keyboard.press('d')
print(keyboard.is_pressed('d'))











