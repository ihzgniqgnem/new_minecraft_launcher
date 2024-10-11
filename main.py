import ui_
import launcher
#import rule
w=ui_.Window()
s1p1b1=ui_.Button(w,20,315,260,55,4,"启动游戏",launcher.lauch)
s1p1b2=ui_.Button(w,20,380,120,35,4,"版本选择",launcher.lauch)
s1p1b3=ui_.Button(w,160,380,120,35,4,"版本设置",launcher.lauch)
w.loop()
