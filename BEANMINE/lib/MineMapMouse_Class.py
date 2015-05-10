##MineMapMouse_Class.py

#############################
##                         ##
##  Mine Map Mouse  ver2   ##
##                         ##
##              by Bean    ##
##                         ##
#############################

from graphics_edit_lite_v2 import *

class MineMapMouse:
    def __init__(self,win,width,height,Ltype,titleheight = 20,leftwidth = 12):
        self.win = win
        self.height = height
        self.width = width
        self.THeight = titleheight
        self.LWidth = leftwidth
        self.Ltype = Ltype

    def reset(self,win,width,height,Ltype,titleheight = 20,leftwidth = 12):
        self.win = win
        self.height = height
        self.width = width
        self.THeight = titleheight
        self.LWidth = leftwidth
        self.Ltype = Ltype
        
    def mouselocate(self,point):
        ##Ltype: box hex tri
        dx = point.getX()
        dy = point.getY()
        if self.Ltype == "box":
            x,y = self.boxlocate(dx,dy)
        elif self.Ltype == "hex":
            x,y = self.hexlocate(dx,dy)
        elif self.Ltype == "tri":
            x,y = self.trilocate(dx,dy)

        return x,y

    def boxlocate(self,dx,dy):
        boxx = (dx - self.LWidth + 11)/22
        boxy = (dy - self.THeight + 11)/22
        
        return boxx,boxy

    def hexlocate(self,dx,dy):
        hexx = (dx - self.LWidth + 10 - 7)/20
        if (dx - self.LWidth + 10 - 7)%20 >= 13:
            edge = 1
        else:
            edge = 0
        if hexx%2 :
            ytype = 1
            hexy = (dy - self.THeight + 11 - 12)/24
        else:
            ytype = 0
            hexy = (dy - self.THeight + 11)/24
            
        if edge == 1 :
            if ytype == 0:
                'line 2n'
                a,b,c=(self.LWidth+hexx*20,self.THeight+hexy*24),(self.LWidth+hexx*20+20,self.THeight+hexy*24-12),(self.LWidth+hexx*20+20,self.THeight+12+hexy*24)
                org = (dx,dy)
                retu = self.hexblockcheck(a,b,c,org)
                if retu == 'b':
                    hexx = hexx + 1
                    hexy = hexy - 1
                elif retu == 'c':
                    hexx = hexx + 1
                elif retu == 'edge':
                    hexx = hexy = 0
   
            elif ytype == 1:
                'line 2n+1'
                a,b,c=(self.LWidth+hexx*20,self.THeight+12+hexy*24),(self.LWidth+hexx*20+20,self.THeight+hexy*24),(self.LWidth+hexx*20+20,self.THeight+24+hexy*24)
                org = (dx,dy)
                retu = self.hexblockcheck(a,b,c,org)
                if retu == 'b':
                    hexx = hexx + 1
                elif retu == 'c':
                    hexx = hexx + 1
                    hexy = hexy + 1
                elif retu == 'edge':
                    hexx = hexy = 0
           
        return hexx,hexy
        
            
    def hexblockcheck(self,a,b,c,org):
        ax,ay = a
        bx,by = b
        cx,cy = c
        x,y = org
        disa = (ax-x)**2+(ay-y)**2
        disb = (bx-x)**2+(by-y)**2
        disc = (cx-x)**2+(cy-y)**2
        if disa<disb and disa<disc:
            return 'a'
        if disb<disa and disb<disc:
            return 'b'
        if disc<disb and disc<disa:
            return 'c'
        return 'edge'

    def trilocate(self,dx,dy):
        trixx = (dx - self.LWidth)/18
        triyy = (dy - self.THeight + 15)/30
        tx = (dx - self.LWidth)%18
        ty = (dy - self.THeight + 15)%30
        if triyy%2:
            if trixx%2 :
                if 30*(18-tx) + 18*ty < 540:
                    triy = triyy*2 - 1
                    trix = trixx/2 + 1
                else:
                    triy = triyy*2
                    trix = trixx/2
                
            else:
                if 30*tx + 18*ty < 540:
                    triy = triyy*2 - 1
                    trix = trixx/2
                else:
                    triy = triyy*2
                    trix = trixx/2
        else:
            if trixx%2 :
                if 30*tx + 18*ty < 540:
                    triy = triyy*2 - 1
                    trix = trixx/2
                else:
                    triy = triyy*2
                    trix = trixx/2 + 1
                
            else:
                if 30*(18-tx) + 18*ty < 540:
                    triy = triyy*2 - 1
                    trix = trixx/2
                else:
                    triy = triyy*2
                    trix = trixx/2
                    
        return trix,triy
