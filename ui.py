import pygame
class UIBase:
    def __init__(self):
        pygame.init()


class Window(UIBase):
    def __init__(self):
        super().__init__()
        self.window = pygame.display.set_mode((775, 435))
        pygame.display.set_caption("power")
        print(self.window)
        self.event_callback = []
        self.add_event([lambda: quit(0), pygame.QUIT])
        self.update_callback = []
        self.add_update(lambda: self.window.fill((244, 246, 250)))

    def update(self):
        for event in pygame.event.get():
            for i in self.event_callback:
                if event.type == i[1]:
                    i[0](event)
        for i in self.update_callback:i()
        pygame.display.flip()

    def loop(self):
        while True:
            self.update()
    def add_event(self, event):
        self.event_callback.append(event)
    def add_update(self, update):
        self.update_callback.append(update)


class Button(UIBase):
    def __init__(self, window, x, y, width, height, circle_width, text, callback):
        super().__init__()
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.circle_width = circle_width
        self.text= text
        self.callback = callback
        self.window.add_update(self.update)
        self.window.add_event([self.motion, pygame.MOUSEMOTION])
        self.window.add_event([self.click, pygame.MOUSEBUTTONUP])
        self.color = (255, 255, 255)
        self.flag = {"mouse_in_rect": False,"mouse_click": False,"show":True,"type":0}
        self.children=[]
        self.draw_init()

    def motion(self, event):
        if self.x <= event.dict["pos"][0] <= self.x + self.width and \
                self.y <= event.dict["pos"][1] <= self.y + self.height:
            self.flag["mouse_in_rect"] = True
        else:
            self.flag["mouse_in_rect"] = False

    def click(self, event):
        if self.x <= event.dict["pos"][0] <= self.x + self.width and \
                self.y <= event.dict["pos"][1] <= self.y + self.height:
            self.flag["mouse_click"] = True
        else:
            self.flag["mouse_click"] = False
    def draw_init(self):
        if self.flag["show"]:
            if self.flag["type"]==0:
                self.color = (52, 61, 74)
            temp=Text(self.window, self.x, self.y, self.width, self.height, self.text)
            temp.color=self.color
            self.children.append(temp)
    def update(self):
        if self.flag["show"]:
            if self.flag["type"]<=2:
                if self.flag["mouse_click"]:
                    self.callback()
                    self.flag["mouse_click"]=False
                if self.flag["mouse_in_rect"]:
                    if self.flag["type"]==0:
                        self.color = (max(self.color[0] - 1, 11), min(self.color[1] + 1, 91), min(self.color[2] + 1, 203))
                else:
                    if self.flag["type"]==0:
                        self.color = (min(self.color[0] + 1, 52), max(self.color[1] - 1, 61), max(self.color[2] - 1, 74))
                for i in self.children:i.update()
                pygame.draw.circle(self.window.window, self.color,
                                   (self.x + self.circle_width, self.y + self.circle_width), self.circle_width, 1,
                                   False, True, False, False)
                pygame.draw.line(self.window.window, self.color, (self.x + self.circle_width, self.y),
                                 (self.x + self.width - self.circle_width, self.y))
                pygame.draw.circle(self.window.window, self.color,
                                   (self.x + self.width - self.circle_width, self.y + self.circle_width),
                                   self.circle_width, 1, True, False, False, False)
                pygame.draw.line(self.window.window, self.color, (self.x + self.width, self.y + self.circle_width),
                                 (self.x + self.width, self.y + self.height - self.circle_width))
                pygame.draw.circle(self.window.window, self.color,
                                   (self.x + self.width - self.circle_width, self.y + self.height - self.circle_width),
                                   self.circle_width, 1, False, False, False, True)
                pygame.draw.line(self.window.window, self.color, (self.x, self.y + self.circle_width),
                                 (self.x, self.y + self.height - self.circle_width))
                pygame.draw.circle(self.window.window, self.color,
                                   (self.x + self.circle_width, self.y + self.height - self.circle_width),
                                   self.circle_width, 1, False, False, True, False)
                pygame.draw.line(self.window.window, self.color, (self.x + self.circle_width, self.y + self.height),
                                 (self.x + self.width - self.circle_width, self.y + self.height))
                temp=Text(self.window, self.x, self.y, self.width, self.height, self.text)
                temp.color=self.color

class Text(UIBase):
    def __init__(self, window, x, y, width,height, text,size=20):
        super().__init__()
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text= text
        self.size=size
        self.color=(255,255,255)
        self.window.update_callback.append(self.update)
        self.flag={}

    def update(self):
        text=pygame.font.Font("deng.ttf",self.size).render(self.text,False,self.color)
        text_rect = text.get_rect()
        text_rect.center=(self.x+self.width//2,self.y+self.height//2)
        self.window.window.blit(text,text_rect)
class Package(UIBase):
    def __init__(self,window,x,y,width,height):
        super().__init__()
        self.window=window
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    def add_update(self,update):
        self.window.add_update(update)
    def add_event(self,event):
        self.window.add_event(event)