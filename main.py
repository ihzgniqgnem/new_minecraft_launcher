import ui
import launcher
w=ui.Window()
b1=ui.Button(w,20,315,260,55,4,"启动游戏",launcher.lauch)
b2=ui.Button(w,20,380,120,35,4,"版本选择",launcher.lauch)
w.loop()
