from tkinter import *

g = 0.01
width = 1000
height = 500

class Ball():
    def __init__(self,master,w,x=100,y=100,r=20):
        self.__vx = 1
        self.__vy = 1
        self.__ax = 0
        self.__ay = g
        self.__x = 100
        self.__y = 100
        self.__r = 20
        self.__root = master
        self.__w = w

        self.__i = w.create_circle(x,y,r)

        self.update()

    def updateVelocity(self,vi,a,pos,max,min):
        if (max - pos) <= self.__r:
            vi = -vi
        if (min + pos) <= self.__r:
            vi = -vi
        vf = vi + a
        return vf

    def update(self):
        self.__w.coords(self.__i, self.__x - self.__r, self.__y - self.__r, self.__x + self.__r, self.__y + self.__r)
        self.__x += self.__vx
        self.__y += self.__vy
        self.__vx = self.updateVelocity(self.__vx,self.__ax,self.__x,width,0)
        self.__vy = self.updateVelocity(self.__vy,self.__ay,self.__y,height,0)
        self.__root.after(1,self.update)





def main():
    root = Tk()

    w = Canvas(root, width=width,height=height)
    w.pack()

    def _create_circle(self,x,y,r,**kwargs):
        return self.create_oval(x-r,y-r,x+r,y+r,**kwargs)
    Canvas.create_circle = _create_circle

    b = Ball(root,w)

    root.mainloop()

if __name__=='__main__':
    main()
