##MineMain.py

#############################
##   Mine   Main           ##
##                         ##
##              by Bean    ##
#############################

from graphics_edit_lite_v2 import *
from MineMapMain_Class import *
import time

class Qdraw:
    def __init__(self,win):
        self.win = win
    def Qpicdraw(self,elemName,x,y,picName,picwidth = None,picheight = None):
        point = 'Point('+str(x)+','+str(y)+')'
        picsite = 'res/'+picName
        exec('self.'+elemName+' = Image('+point+',"'+picsite+'")')
        exec('self.'+elemName+'.draw(self.win)')
        exec('self.'+elemName+'xy = (x,y)')
        if picheight != None:
            exec('self.'+elemName+'size = (picwidth,picheight)')
        else:
            exec('self.'+elemName+'size = None')
            
    def Qchange(self,elemName,picName = None,picwidth = None,picheight = None):
        try:
            exec('self.'+elemName+'.undraw()')
        except:
            pass
        if picName == 'del':
            exec('del self.'+elemName)
            exec('del self.'+elemName+'xy')
            exec('del self.'+elemName+'size')
            return
        if picName != None:
            exec('x,y = self.'+elemName+'xy')
            point = 'Point('+str(x)+','+str(y)+')'
            picsite = 'res/'+picName
            exec('self.'+elemName+' = Image('+point+',"'+picsite+'")')
            exec('self.'+elemName+'.draw(self.win)')
            if picheight != None:
                exec('self.'+elemName+'size = (picwidth,picheight)')

    def Qmove(self,elemName,x,y,picName = None,picwidth = None,picheight = None):
        try:
            exec('self.'+elemName+'.undraw()')
        except:
            pass
        if picName != None:
            point = 'Point('+str(x)+','+str(y)+')'
            picsite = 'res/'+picName
            exec('self.'+elemName+' = Image('+point+',"'+picsite+'")')
            exec('self.'+elemName+'.draw(self.win)')
            exec('self.'+elemName+'xy = (x,y)')
            if picheight != None:
                exec('self.'+elemName+'size = (picwidth,picheight)')
            
    def isClicked(self,elemName,point):
        try:
            exec('picsize = self.'+elemName+'size')
        except:
            return
        if picsize == None:
            return False
        else:
            exec('picx,picy = self.'+elemName+'xy')
            picwidth,picheight = picsize
            x = point.getX()
            y = point.getY()
            if x < picx+picwidth/2 and x > picx-picwidth/2 and y < picy+picheight/2 and y > picy-picheight/2:
                return True
            else:
                return False

    def slidebar(self,elemName,x1,x2,y,Slablename = None,Sx = None,Sy = None,Smax = 100,Scolor = 'yellow',Ssize = 12,Sfamily = 'courier',Svalue = '00'):
        point = 'Point('+str(x1)+','+str(y)+')'
        x = x1
        picsite = 'res/slidebar'
        picwidth,picheight = 10,8
        exec('self.'+elemName+' = Image('+point+',"'+picsite+'")')
        exec('self.'+elemName+'.draw(self.win)')
        exec('self.'+elemName+'xx = (x1,x2)')
        exec('self.'+elemName+'xy = (x,y)')

        if Slablename != None:
            Lpoint = 'Point('+str(Sx)+','+str(Sy)+')'
            exec('self.'+Slablename+' = Text('+Lpoint+',"'+Svalue+'")')
            exec('self.'+Slablename+'.setTextColor("'+Scolor+'")')
            exec('self.'+Slablename+'.setSize('+str(Ssize)+')')
            exec('self.'+Slablename+'.setFace("'+Sfamily+'")')
            exec('self.'+Slablename+'.draw(self.win)')

            exec('self.'+Slablename+'Smax = '+str(Smax))
        

    def slideclicked(self,elemName,point):
        
        try:
            exec('picx,picy = self.'+elemName+'xy')
            picwidth,picheight = 8,10
            x = point.getX()
            y = point.getY()
            if x < picx+picwidth/2 and x > picx-picwidth/2 and y < picy+picheight/2 and y > picy-picheight/2:
                return True
            else:
                return False
        except:
            return False

    def resetSmax(self,elemName,Slablename,NSmax = 100):
        exec('Smax = self.'+Slablename+'Smax')
        exec('numN = self.'+Slablename+'.getText()')
        exec('x1,x2 = self.'+elemName+'xx')
        exec('x,y = self.'+elemName+'xy')
        
        if NSmax != 0 :
            Smax = Smax*1.00
            point = Point(x1+int(int(numN)*1.00*Smax/NSmax),y)
        else:
            point = Point(x1,y)

        #exec('self.'+Slablename+'.setText('+percentage+')')
        exec('self.'+Slablename+'Smax = '+str(NSmax))
        percentage = self.slide(elemName,point,Slablename)
        return percentage

    def slide(self,elemName,point,Slablename = None):
        if point == 'del':
            exec('self.'+elemName+'.undraw()')
            exec('del self.'+elemName)
            exec('del self.'+elemName+'xx')
            exec('del self.'+elemName+'xy')
            if Slablename != None:
                exec('self.'+Slablename+'.undraw()')
                exec('del self.'+Slablename)
                exec('del self.'+Slablename+'Smax')
            return

        dx = point.getX()
        exec('x1,x2 = self.'+elemName+'xx')
        exec('x,y = self.'+elemName+'xy')
        if dx<x1:
            dx = x1
        elif dx>x2:
            dx = x2
        if dx != x:
            x = dx
            exec('self.'+elemName+'.undraw()')
            point = 'Point('+str(x)+','+str(y)+')'
            picsite = 'res/slidebar'
            exec('self.'+elemName+' = Image('+point+',"'+picsite+'")')
            exec('self.'+elemName+'.draw(self.win)')
            exec('self.'+elemName+'xy = (x,y)')

        percentage = int(((dx-x1)*100.0)/(x2-x1))
        if Slablename != None:
            exec('Smax = self.'+Slablename+'Smax')
            percentage = int(percentage/100.0*Smax)
            exec('self.'+Slablename+'.setText('+str(percentage)+')')
        return percentage

        
def main():
    Menu = GraphWin('Mine Menu')
    Menu.setBackground("black")
    Menu.setIcon('res/icon')
    
    MenuQD = Qdraw(Menu)

    MenuQD.Qpicdraw('menubkg',100,100,'menubkg',picwidth = 200,picheight = 200)

    page = 'main'

    mainstop = 0
    while mainstop == 0:
        if page == 'main':
            time.sleep(0.2)
            MenuQD.Qpicdraw('menu1',100,60,'qgame',picwidth = 120,picheight = 15)
            time.sleep(0.2)
            MenuQD.Qpicdraw('menu2',100,95,'cgame',picwidth = 137,picheight = 15)
            time.sleep(0.2)
            MenuQD.Qpicdraw('menu3',100,130,'topscore',picwidth = 115,picheight = 15)
            time.sleep(0.2)
            MenuQD.Qpicdraw('menu4',100,165,'help',picwidth = 51,picheight = 15)
            time.sleep(0.22)
            MenuQD.Qpicdraw('quit',160,25,'quit',picwidth = 36,picheight = 13)

            stop = 0
            while stop == 0:
                clicked = Menu.getMouse()
                if MenuQD.isClicked('menu1',clicked):
                    stop = 1
                    page = 'quickgame'
                    MenuQD.Qchange('menu2')
                    MenuQD.Qchange('menu3')
                    MenuQD.Qchange('menu4')
                    MenuQD.Qchange('quit')
                    time.sleep(0.2)
                    MenuQD.Qchange('menu1')
                elif MenuQD.isClicked('menu2',clicked):
                    stop = 1
                    page = 'custom'
                    MenuQD.Qchange('menu1')
                    MenuQD.Qchange('menu3')
                    MenuQD.Qchange('menu4')
                    MenuQD.Qchange('quit')
                    time.sleep(0.2)
                    MenuQD.Qchange('menu2')
                elif MenuQD.isClicked('menu3',clicked):
                    stop = 1
                    page = 'topscore'
                    MenuQD.Qchange('menu1')
                    MenuQD.Qchange('menu2')
                    MenuQD.Qchange('menu4')
                    MenuQD.Qchange('quit')
                    time.sleep(0.2)
                    MenuQD.Qchange('menu3')
                elif MenuQD.isClicked('menu4',clicked):
                    stop = 1
                    page = 'help'
                    MenuQD.Qchange('menu1')
                    MenuQD.Qchange('menu2')
                    MenuQD.Qchange('menu3')
                    MenuQD.Qchange('quit')
                    time.sleep(0.2)
                    MenuQD.Qchange('menu4')
                elif MenuQD.isClicked('quit',clicked):
                    stop = 1
                    page = 'quit'
                    MenuQD.Qchange('menu1')
                    MenuQD.Qchange('menu2')
                    MenuQD.Qchange('menu3')
                    MenuQD.Qchange('menu4')
                    MenuQD.Qchange('quit')
                    time.sleep(0.2)
                    MenuQD.Qpicdraw('thanks',100,100,'TFP',picwidth = 200,picheight = 200)
                    time.sleep(0.5)
                    MenuQD.Qchange('thanks')
                    time.sleep(0.2)
                    MenuQD.Qpicdraw('Bmark',100,100,'Bmark',picwidth = 200,picheight = 200)
                    time.sleep(0.52)
                    MenuQD.Qchange('Bmark')
                    time.sleep(0.2)
                                   
        elif page == 'quit':
                Menu.close()
                exit()

        elif page == 'help':
            MenuQD.Qpicdraw('Phelp',100,100,'Phelp',picwidth = 200,picheight = 200)        
            MenuQD.Qpicdraw('help1',71,80,'help1',picwidth = 103,picheight = 12)
            MenuQD.Qpicdraw('help2',71,100,'help2',picwidth = 93,picheight = 12)
            MenuQD.Qpicdraw('help3',71,120,'help3',picwidth = 83,picheight = 12)
            MenuQD.Qpicdraw('help4',71,139,'help4',picwidth = 62,picheight = 12)
            MenuQD.Qpicdraw('help5',71,160,'help5',picwidth = 76,picheight = 12)
            MenuQD.Qpicdraw('back',160,25,'back',picwidth = 40,picheight = 12)
            stop = 0
            while stop == 0:
                clicked = Menu.getMouse()
                if MenuQD.isClicked('help1',clicked):
                    stop = 1
                    page = 'help1'
                    MenuQD.Qchange('Phelp','del')
                    MenuQD.Qchange('help2','del')
                    MenuQD.Qchange('help3','del')
                    MenuQD.Qchange('help4','del')
                    MenuQD.Qchange('help5','del')
                    time.sleep(0.2)
                    MenuQD.Qchange('help1','del')
                elif MenuQD.isClicked('help2',clicked):
                    stop = 1
                    page = 'help2'
                    MenuQD.Qchange('Phelp','del')
                    MenuQD.Qchange('help1','del')
                    MenuQD.Qchange('help3','del')
                    MenuQD.Qchange('help4','del')
                    MenuQD.Qchange('help5','del')
                    time.sleep(0.2)
                    MenuQD.Qchange('help2','del')
                elif MenuQD.isClicked('help3',clicked):
                    stop = 1
                    page = 'help3'
                    MenuQD.Qchange('Phelp','del')
                    MenuQD.Qchange('help1','del')
                    MenuQD.Qchange('help2','del')
                    MenuQD.Qchange('help4','del')
                    MenuQD.Qchange('help5','del')
                    time.sleep(0.2)
                    MenuQD.Qchange('help3','del')
                elif MenuQD.isClicked('help4',clicked):
                    stop = 1
                    page = 'help4'
                    MenuQD.Qchange('Phelp','del')
                    MenuQD.Qchange('help1','del')
                    MenuQD.Qchange('help2','del')
                    MenuQD.Qchange('help3','del')
                    MenuQD.Qchange('help5','del')
                    time.sleep(0.2)
                    MenuQD.Qchange('help4','del')
                elif MenuQD.isClicked('help5',clicked):
                    stop = 1
                    page = 'help5'
                    MenuQD.Qchange('Phelp','del')
                    MenuQD.Qchange('help1','del')
                    MenuQD.Qchange('help2','del')
                    MenuQD.Qchange('help3','del')
                    MenuQD.Qchange('help4','del')
                    time.sleep(0.2)
                    MenuQD.Qchange('help5','del')
                elif MenuQD.isClicked('back',clicked):
                    stop = 1
                    page = 'main'
                    MenuQD.Qchange('Phelp','del')
                    MenuQD.Qchange('help1','del')
                    MenuQD.Qchange('help2','del')
                    MenuQD.Qchange('help3','del')
                    MenuQD.Qchange('help4','del')
                    MenuQD.Qchange('help5','del')
                    MenuQD.Qchange('back','del')

        elif page == 'help1':
            MenuQD.Qpicdraw('Pbasic',100,100,'Pbasic',picwidth = 200,picheight = 200)
            stop = 0
            while stop == 0:
                clicked = Menu.getMouse()
                if MenuQD.isClicked('back',clicked):
                    stop = 1
                    page = 'help'
                    MenuQD.Qchange('Pbasic','del')
                    MenuQD.Qchange('back','del')

        elif page == 'help2':
            MenuQD.Qpicdraw('Pinterface',100,100,'Pinterface',picwidth = 200,picheight = 200)
            stop = 0
            while stop == 0:
                clicked = Menu.getMouse()
                if MenuQD.isClicked('back',clicked):
                    stop = 1
                    page = 'help'
                    MenuQD.Qchange('Pinterface','del')
                    MenuQD.Qchange('back','del')
                    
        elif page == 'help3':
            MenuQD.Qpicdraw('Pcontrol',100,100,'Pcontrol',picwidth = 200,picheight = 200)
            stop = 0
            while stop == 0:
                clicked = Menu.getMouse()
                if MenuQD.isClicked('back',clicked):
                    stop = 1
                    page = 'help'
                    MenuQD.Qchange('Pcontrol','del')
                    MenuQD.Qchange('back','del')
                    
        elif page == 'help4':
            MenuQD.Qpicdraw('Ptype',100,100,'Ptype',picwidth = 200,picheight = 200)
            MenuQD.Qpicdraw('faceretro',50,92,'retrosmile',picwidth = 20,picheight = 20)
            MenuQD.Qpicdraw('facebox',50,146,'boxsmile',picwidth = 22,picheight = 22)
            MenuQD.Qpicdraw('facehex',150,92,'hexsmile',picwidth = 24,picheight = 24)
            MenuQD.Qpicdraw('facetri',150,146,'trismile',picwidth = 28,picheight = 28)
            stop = 0
            while stop == 0:
                clicked = Menu.getMouse()
                if MenuQD.isClicked('faceretro',clicked):
                    stop = 1
                    page = 'faceretro'
                    MenuQD.Qchange('faceretro','retrooops')
                    time.sleep(0.5)
                    MenuQD.Qchange('Ptype','del')
                    MenuQD.Qchange('faceretro','del')
                    MenuQD.Qchange('facebox','del')
                    MenuQD.Qchange('facehex','del')
                    MenuQD.Qchange('facetri','del')

                if MenuQD.isClicked('facebox',clicked):
                    stop = 1
                    page = 'facebox'
                    MenuQD.Qchange('facebox','boxoops')
                    time.sleep(0.5)
                    MenuQD.Qchange('Ptype','del')
                    MenuQD.Qchange('faceretro','del')
                    MenuQD.Qchange('facebox','del')
                    MenuQD.Qchange('facehex','del')
                    MenuQD.Qchange('facetri','del')

                if MenuQD.isClicked('facehex',clicked):
                    stop = 1
                    page = 'facehex'
                    MenuQD.Qchange('facehex','hexoops')
                    time.sleep(0.5)
                    MenuQD.Qchange('Ptype','del')
                    MenuQD.Qchange('faceretro','del')
                    MenuQD.Qchange('facebox','del')
                    MenuQD.Qchange('facehex','del')
                    MenuQD.Qchange('facetri','del')

                if MenuQD.isClicked('facetri',clicked):
                    stop = 1
                    page = 'facetri'
                    MenuQD.Qchange('facetri','trioops')
                    time.sleep(0.5)
                    MenuQD.Qchange('Ptype','del')
                    MenuQD.Qchange('faceretro','del')
                    MenuQD.Qchange('facebox','del')
                    MenuQD.Qchange('facehex','del')
                    MenuQD.Qchange('facetri','del')

                if MenuQD.isClicked('back',clicked):
                    stop = 1
                    page = 'help'
                    MenuQD.Qchange('faceretro','retrooops')
                    MenuQD.Qchange('facebox','boxoops')
                    MenuQD.Qchange('facehex','hexoops')
                    MenuQD.Qchange('facetri','trioops')
                    time.sleep(1.2)
                    MenuQD.Qchange('Ptype','del')
                    MenuQD.Qchange('faceretro','del')
                    MenuQD.Qchange('facebox','del')
                    MenuQD.Qchange('facehex','del')
                    MenuQD.Qchange('facetri','del')
                    MenuQD.Qchange('back','del')
                    
        elif page == 'help5':
            MenuQD.Qpicdraw('Pcredits',100,100,'Pcredits',picwidth = 200,picheight = 200)
            stop = 0
            while stop == 0:
                clicked = Menu.getMouse()
                if MenuQD.isClicked('back',clicked):
                    stop = 1
                    page = 'help'
                    MenuQD.Qchange('Pcredits','del')
                    MenuQD.Qchange('back','del')
                    
        elif page == 'faceretro':
            MenuQD.Qpicdraw('typeretro',100,100,'typeretro',picwidth = 200,picheight = 200)
            stop = 0
            while stop == 0:
                clicked = Menu.getMouse()
                if MenuQD.isClicked('back',clicked):
                    stop = 1
                    page = 'help4'
                    MenuQD.Qchange('typeretro','del')

            
        elif page == 'facebox':
            MenuQD.Qpicdraw('typebox',100,100,'typebox',picwidth = 200,picheight = 200)
            stop = 0
            while stop == 0:
                clicked = Menu.getMouse()
                if MenuQD.isClicked('back',clicked):
                    stop = 1
                    page = 'help4'
                    MenuQD.Qchange('typebox','del')
        elif page == 'facehex':
            MenuQD.Qpicdraw('typehex',100,100,'typehex',picwidth = 200,picheight = 200)
            stop = 0
            while stop == 0:
                clicked = Menu.getMouse()
                if MenuQD.isClicked('back',clicked):
                    stop = 1
                    page = 'help4'
                    MenuQD.Qchange('typehex','del')
        elif page == 'facetri':
            MenuQD.Qpicdraw('typetri',100,100,'typetri',picwidth = 200,picheight = 200)
            stop = 0
            while stop == 0:
                clicked = Menu.getMouse()
                if MenuQD.isClicked('back',clicked):
                    stop = 1
                    page = 'help4'
                    MenuQD.Qchange('typetri','del')
        elif page == 'custom':
            CGtype = ['',0,0,0,0,0]
            
            MenuQD.Qpicdraw('cgamesel',100,100,'cgamesel',picwidth = 200,picheight = 200)
            MenuQD.slidebar('slidebar1',60,150,73,'widthNo',172,72,30)
            MenuQD.slidebar('slidebar2',60,150,84,'heightNo',172,83,40)
            MenuQD.slidebar('slidebar3',60,150,107,'mineNo',172,106,0)
            MenuQD.slidebar('slidebar4',60,150,130,'lockNo',172,129,0)
            MenuQD.slidebar('slidebar5',60,150,153,'empNo',172,152,0)
            
            MenuQD.Qpicdraw('facebox',80,56,'boxsmile',picwidth = 22,picheight = 22)
            MenuQD.Qpicdraw('facehex',112,56,'hexsmile',picwidth = 24,picheight = 24)
            MenuQD.Qpicdraw('facetri',144,54,'trismile',picwidth = 28,picheight = 28)
            MenuQD.Qpicdraw('stgame',100,180,'stgame')
            MenuQD.Qchange('stgame')
            MenuQD.Qpicdraw('back',160,25,'back',picwidth = 40,picheight = 12)
            stop = 0
            while stop == 0:
                #print CGtype
                if CGtype[0] == '' or CGtype[1]<5 or CGtype[2]<5 or CGtype[3]<5 or CGtype[3]+CGtype[4]+CGtype[5] >= CGtype[1]*CGtype[2]-2:
                    MenuQD.Qchange('stgame')
                elif CGtype[0] != '' and CGtype[1] != 0 and CGtype[2] != 0:
                    MenuQD.Qchange('stgame','stgame',picwidth = 117,picheight = 16)
                    
                clicked = Menu.getMouse()

                minemax=lockmax=empmax=0
                
                if MenuQD.isClicked('back',clicked):
                    stop = 1
                    page = 'main'
                    MenuQD.Qchange('facebox','boxoops')
                    MenuQD.Qchange('facehex','hexoops')
                    MenuQD.Qchange('facetri','trioops')
                    time.sleep(0.5)
                    
                    MenuQD.Qchange('cgamesel','del')
                    MenuQD.Qchange('facebox','del')
                    MenuQD.Qchange('facehex','del')
                    MenuQD.Qchange('facetri','del')
                    MenuQD.Qchange('stgame','del')
                    MenuQD.slide('slidebar1','del','widthNo')
                    MenuQD.slide('slidebar2','del','heightNo')
                    MenuQD.slide('slidebar3','del','mineNo')
                    MenuQD.slide('slidebar4','del','lockNo')
                    MenuQD.slide('slidebar5','del','empNo')

                    MenuQD.Qchange('back','del')

                elif MenuQD.isClicked('facebox',clicked):
                    CGtype[0] = 'box'
                    MenuQD.Qchange('facebox','boxwin')
                    MenuQD.Qchange('facehex','hexdie')
                    MenuQD.Qchange('facetri','tridie')
                elif MenuQD.isClicked('facehex',clicked):
                    CGtype[0] = 'hex'
                    MenuQD.Qchange('facebox','boxdie')
                    MenuQD.Qchange('facehex','hexwin')
                    MenuQD.Qchange('facetri','tridie')
                elif MenuQD.isClicked('facetri',clicked):
                    CGtype[0] = 'tri'
                    MenuQD.Qchange('facebox','boxdie')
                    MenuQD.Qchange('facehex','hexdie')
                    MenuQD.Qchange('facetri','triwin')
                    
                elif MenuQD.slideclicked('slidebar1',clicked):
                    clickedtype = 'C1'
                    while clickedtype != 'R1':
                        if clicked != None :
                            percent = MenuQD.slide('slidebar1',clicked,'widthNo')
                        rawclick = Menu.eyeMouse()
                        if rawclick!= None:
                            clicked,clickedtype=rawclick
                        else:
                            clicked,clickedtype=None,None
                    if percent>=5 and CGtype[2]>=5:
                        minemax = percent*CGtype[2]-(CGtype[4]+CGtype[5]+5)
                        if minemax <0:
                            minemax =0
                        elif minemax >99:
                            minemax =99
                        CGtype[3]=MenuQD.resetSmax('slidebar3','mineNo',minemax)
                        lockmax = minemax/2+2
                        CGtype[4]=MenuQD.resetSmax('slidebar4','lockNo',lockmax)
                        empmax = minemax
                        CGtype[5]=MenuQD.resetSmax('slidebar5','empNo',empmax)
                    CGtype[1] = percent
                        
                elif MenuQD.slideclicked('slidebar2',clicked):
                    clickedtype = 'C1'
                    while clickedtype != 'R1':
                        if clicked != None :
                            percent = MenuQD.slide('slidebar2',clicked,'heightNo')
                        rawclick = Menu.eyeMouse()
                        if rawclick!= None:
                            clicked,clickedtype=rawclick
                        else:
                            clicked,clickedtype=None,None
                    if percent>=5 and CGtype[1]>=5:
                        minemax = CGtype[1]*percent-(CGtype[4]+CGtype[5]+5)
                        if minemax <0:
                            minemax =0
                        elif minemax >99:
                            minemax =99
                        CGtype[3]=MenuQD.resetSmax('slidebar3','mineNo',minemax)
                        lockmax = minemax/2+2
                        CGtype[4]=MenuQD.resetSmax('slidebar4','lockNo',lockmax)
                        empmax = minemax
                        CGtype[5]=MenuQD.resetSmax('slidebar5','empNo',empmax)
                    CGtype[2] = percent
                        
                elif MenuQD.slideclicked('slidebar3',clicked):
                    clickedtype = 'C1'
                    while clickedtype != 'R1':
                        if clicked != None :
                            percent = MenuQD.slide('slidebar3',clicked,'mineNo')
                        rawclick = Menu.eyeMouse()
                        if rawclick!= None:
                            clicked,clickedtype=rawclick
                        else:
                            clicked,clickedtype=None,None
                    if lockmax > minemax/2+2:
                        lockmax=minemax/2+2
                        if lockmax>CGtype[1]*CGtype[2]-CGtype[5]-percent-5:
                            lockmax=CGtype[1]*CGtype[2]-CGtype[5]-percent-5
                        if lockmax < 0 :
                            lockmax = 0
                        CGtype[4]=MenuQD.resetSmax('slidebar4','lockNo',lockmax)
                    if empmax > minemax+2:
                        empmax = minemax+2
                        if empmax>CGtype[1]*CGtype[2]-CGtype[4]-percent-5:
                            empmax=CGtype[1]*CGtype[2]-CGtype[4]-percent-5
                        if empmax < 0 :
                            empmax = 0
                        CGtype[5]=MenuQD.resetSmax('slidebar5','empNo',empmax)
                    CGtype[3] = percent

                elif MenuQD.slideclicked('slidebar4',clicked):
                    clickedtype = 'C1'
                    while clickedtype != 'R1':
                        if clicked != None :
                            percent = MenuQD.slide('slidebar4',clicked,'lockNo')
                        rawclick = Menu.eyeMouse()
                        if rawclick!= None:
                            clicked,clickedtype=rawclick
                        else:
                            clicked,clickedtype=None,None
                    if empmax > minemax+2:
                        empmax = minemax+2
                        if empmax>CGtype[1]*CGtype[2]-CGtype[3]-percent-5:
                            empmax=CGtype[1]*CGtype[2]-CGtype[3]-percent-5
                        if empmax < 0 :
                            empmax = 0
                        CGtype[5]=MenuQD.resetSmax('slidebar5','empNo',empmax)
                    CGtype[4] = percent
                elif MenuQD.slideclicked('slidebar5',clicked):
                    clickedtype = 'C1'
                    while clickedtype != 'R1':
                        if clicked != None :
                            percent = MenuQD.slide('slidebar5',clicked,'empNo')
                        rawclick = Menu.eyeMouse()
                        if rawclick!= None:
                            clicked,clickedtype=rawclick
                        else:
                            clicked,clickedtype=None,None
                    CGtype[5] = percent
                    
                elif MenuQD.isClicked('stgame',clicked):
                    stop = 1
                    page = 'cstart'
                    MenuQD.Qchange('cgamesel','del')
                    MenuQD.Qchange('facebox','del')
                    MenuQD.Qchange('facehex','del')
                    MenuQD.Qchange('facetri','del')
                    MenuQD.Qchange('stgame','del')
                    MenuQD.slide('slidebar1','del','widthNo')
                    MenuQD.slide('slidebar2','del','heightNo')
                    MenuQD.slide('slidebar3','del','mineNo')
                    MenuQD.slide('slidebar4','del','lockNo')
                    MenuQD.slide('slidebar5','del','empNo')

                    MenuQD.Qchange('back','del')

        elif page == 'quickgame':
            QGtype = ''
            QGlevel = ''
            MenuQD.Qpicdraw('qgamesel',100,100,'qgamesel',picwidth = 200,picheight = 200)
            MenuQD.Qpicdraw('faceretro',80,60,'retrosmile',picwidth = 20,picheight = 20)
            MenuQD.Qpicdraw('facebox',105,60,'boxsmile',picwidth = 22,picheight = 22)
            MenuQD.Qpicdraw('facehex',133,60,'hexsmile',picwidth = 24,picheight = 24)
            MenuQD.Qpicdraw('facetri',162,58,'trismile',picwidth = 28,picheight = 28)
            MenuQD.Qpicdraw('stgame',100,180,'stgame')
            MenuQD.Qchange('stgame')
            MenuQD.Qpicdraw('easy',128,110,'easy',picwidth = 36,picheight = 11)
            MenuQD.Qpicdraw('medium',140,130,'medium',picwidth = 61,picheight = 11)
            MenuQD.Qpicdraw('hard',131,150,'hard',picwidth = 42,picheight = 11)
            MenuQD.Qpicdraw('arrow1',100,110,'arrow')
            MenuQD.Qchange('arrow1')
            MenuQD.Qpicdraw('arrow2',100,130,'arrow')
            MenuQD.Qchange('arrow2')
            MenuQD.Qpicdraw('arrow3',100,150,'arrow')
            MenuQD.Qchange('arrow3')
            MenuQD.Qpicdraw('back',160,25,'back',picwidth = 40,picheight = 12)
            stop = 0
            while stop == 0:
                
                if QGlevel != '' and QGtype != '' :
                    MenuQD.Qchange('stgame','stgame',picwidth = 117,picheight = 16)
                    
                clicked = Menu.getMouse()
                
                if MenuQD.isClicked('back',clicked):
                    stop = 1
                    page = 'main'
                    MenuQD.Qchange('faceretro','retrooops')
                    MenuQD.Qchange('facebox','boxoops')
                    MenuQD.Qchange('facehex','hexoops')
                    MenuQD.Qchange('facetri','trioops')
                    time.sleep(0.5)
                    
                    MenuQD.Qchange('qgamesel','del')
                    MenuQD.Qchange('faceretro','del')
                    MenuQD.Qchange('facebox','del')
                    MenuQD.Qchange('facehex','del')
                    MenuQD.Qchange('facetri','del')
                    MenuQD.Qchange('stgame','del')
                    MenuQD.Qchange('easy','del')
                    MenuQD.Qchange('medium','del')
                    MenuQD.Qchange('hard','del')
                    MenuQD.Qchange('back','del')
                    MenuQD.Qchange('arrow1','del')
                    MenuQD.Qchange('arrow2','del')
                    MenuQD.Qchange('arrow3','del')
                elif MenuQD.isClicked('faceretro',clicked):
                    QGtype = 'retro'
                    MenuQD.Qchange('faceretro','retrowin')
                    MenuQD.Qchange('facebox','boxdie')
                    MenuQD.Qchange('facehex','hexdie')
                    MenuQD.Qchange('facetri','tridie')
                elif MenuQD.isClicked('facebox',clicked):
                    QGtype = 'box'
                    MenuQD.Qchange('faceretro','retrodie')
                    MenuQD.Qchange('facebox','boxwin')
                    MenuQD.Qchange('facehex','hexdie')
                    MenuQD.Qchange('facetri','tridie')
                elif MenuQD.isClicked('facehex',clicked):
                    QGtype = 'hex'
                    MenuQD.Qchange('faceretro','retrodie')
                    MenuQD.Qchange('facebox','boxdie')
                    MenuQD.Qchange('facehex','hexwin')
                    MenuQD.Qchange('facetri','tridie')
                elif MenuQD.isClicked('facetri',clicked):
                    QGtype = 'tri'
                    MenuQD.Qchange('faceretro','retrodie')
                    MenuQD.Qchange('facebox','boxdie')
                    MenuQD.Qchange('facehex','hexdie')
                    MenuQD.Qchange('facetri','triwin')
                    
                elif MenuQD.isClicked('easy',clicked):
                    QGlevel = 'easy'
                    MenuQD.Qchange('arrow1','arrow')
                    MenuQD.Qchange('arrow2')
                    MenuQD.Qchange('arrow3')
                elif MenuQD.isClicked('medium',clicked):
                    QGlevel = 'medium'
                    MenuQD.Qchange('arrow1')
                    MenuQD.Qchange('arrow2','arrow')
                    MenuQD.Qchange('arrow3')
                elif MenuQD.isClicked('hard',clicked):
                    QGlevel = 'hard'
                    MenuQD.Qchange('arrow1')
                    MenuQD.Qchange('arrow2')
                    MenuQD.Qchange('arrow3','arrow')
                elif MenuQD.isClicked('stgame',clicked):
                    stop = 1
                    page = 'qstart'
                    MenuQD.Qchange('qgamesel','del')
                    MenuQD.Qchange('faceretro','del')
                    MenuQD.Qchange('facebox','del')
                    MenuQD.Qchange('facehex','del')
                    MenuQD.Qchange('facetri','del')
                    MenuQD.Qchange('stgame','del')
                    MenuQD.Qchange('easy','del')
                    MenuQD.Qchange('medium','del')
                    MenuQD.Qchange('hard','del')
                    MenuQD.Qchange('back','del')
                    MenuQD.Qchange('arrow1','del')
                    MenuQD.Qchange('arrow2','del')
                    MenuQD.Qchange('arrow3','del')

                

        elif page == 'topscore':
            scorelist = open('res/scosv', 'r')
            scorelistS = scorelist.read()
            scorelist.close()
            slist = eval(scorelistS)
            Plist = ''
            for i in range(len(slist)):
                sline = slist[i]
                for ii in range(len(sline)):
                    sTemp = sline[ii]
                    if sTemp == '/':
                        sTemp = ' '
                    Plist += sTemp
                Plist += '\n'
                    
            MenuQD.Qpicdraw('back',160,25,'back',picwidth = 40,picheight = 12)
            scoreboard = Text(Point(100,121),'')
            scoreboard.setFace('times roman')
            scoreboard.setTextColor('yellow')
            scoreboard.setSize(7)
            scoreboard.draw(Menu)
            scoreboard.setText(Plist)
            stop = 0
            while stop == 0:
                clicked = Menu.getMouse()
                if MenuQD.isClicked('back',clicked):
                    stop = 1
                    page = 'main'
                    MenuQD.Qchange('back','del')
                    scoreboard.undraw()
                    del scoreboard
                    
        elif page == 'qstart':
            MenuQD.Qpicdraw('lockscr',100,100,'lockscr',picwidth = 200,picheight = 200)
            if QGtype == 'retro':
                if QGlevel == 'easy':
                    Mwidth = 9
                    Mheight = 9
                    Mtype = 'retro'
                    Mine_number = 10
                    Empty_number = 0
                    Lock_number = 0
                elif QGlevel == 'medium':
                    Mwidth = 16
                    Mheight = 16
                    Mtype = 'retro'
                    Mine_number = 40
                    Empty_number = 0
                    Lock_number = 0
                elif QGlevel == 'hard':
                    Mwidth = 30
                    Mheight = 16
                    Mtype = 'retro'
                    Mine_number = 99
                    Empty_number = 0
                    Lock_number = 0
            elif QGtype == 'box':
                if QGlevel == 'easy':
                    Mwidth = 12
                    Mheight = 12
                    Mtype = 'box'
                    Mine_number = 10
                    Empty_number = 5
                    Lock_number = 2
                elif QGlevel == 'medium':
                    Mwidth = 20
                    Mheight = 20
                    Mtype = 'box'
                    Mine_number = 40
                    Empty_number = 5
                    Lock_number = 5
                elif QGlevel == 'hard':
                    Mwidth = 34
                    Mheight = 20
                    Mtype = 'box'
                    Mine_number = 99
                    Empty_number = 10
                    Lock_number = 10
            elif QGtype == 'hex':
                if QGlevel == 'easy':
                    Mwidth = 9
                    Mheight = 9
                    Mtype = 'hex'
                    Mine_number = 10
                    Empty_number = 5
                    Lock_number = 2
                elif QGlevel == 'medium':
                    Mwidth = 20
                    Mheight = 16
                    Mtype = 'hex'
                    Mine_number = 40
                    Empty_number = 5
                    Lock_number = 5
                elif QGlevel == 'hard':
                    Mwidth = 34
                    Mheight = 20
                    Mtype = 'hex'
                    Mine_number = 99
                    Empty_number = 10
                    Lock_number = 10
            elif QGtype == 'tri':
                if QGlevel == 'easy':
                    Mwidth = 8
                    Mheight = 16
                    Mtype = 'tri'
                    Mine_number = 10
                    Empty_number = 2
                    Lock_number = 2
                elif QGlevel == 'medium':
                    Mwidth = 16
                    Mheight = 30
                    Mtype = 'tri'
                    Mine_number = 40
                    Empty_number = 5
                    Lock_number = 8
                elif QGlevel == 'hard':
                    Mwidth = 20
                    Mheight = 40
                    Mtype = 'tri'
                    Mine_number = 80
                    Empty_number = 10
                    Lock_number = 12

            GameS = StartGame(Mwidth,Mheight,Mtype,Mine_number,Empty_number,Lock_number)
            outcome,gametime = GameS.getOAT()

            scorelist = open('res/scosv', 'r')
            scorelistS = scorelist.read()
            scorelist.close()
            
            slist = eval(scorelistS)
            if outcome == 'win':
                hh,mm,ss = gametime
                if QGtype == 'retro':
                    LT = 0
                elif QGtype == 'box':
                    LT = 1
                elif QGtype == 'hex':
                    LT = 2
                elif QGtype == 'tri':
                    LT = 3
                if QGlevel == 'easy':
                    LV = 0
                elif QGlevel == 'medium':
                    LV = 2
                elif QGlevel == 'hard':
                    LV = 3
                lastbestNO = LT*3 + LV
                lastbestscore = slist[lastbestNO]
                lbhh = int(lastbestscore[13]+lastbestscore[14])
                lbmm = int(lastbestscore[16]+lastbestscore[17])
                lbss = int(lastbestscore[19]+lastbestscore[20])
                if hh*10000+mm*100+ss < lbhh*10000+lbmm*100+lbss :
                    page = 'bestwin'
                else:
                    page = 'win'
            elif outcome == 'lose':
                page = 'lose'
            elif outcome == 'stopped':
                page = 'quickgame'
                GameS.aftergame()
                del GameS

            MenuQD.Qchange('lockscr','del')
            
        elif page == 'cstart':
            Mwidth,Mheight,Mtype,Mine_number,Empty_number,Lock_number=CGtype[1],CGtype[2],CGtype[0],CGtype[3],CGtype[5],CGtype[4]
            MenuQD.Qpicdraw('lockscr',100,100,'lockscr',picwidth = 200,picheight = 200)
            
            GameS = StartGame(Mwidth,Mheight,Mtype,Mine_number,Empty_number,Lock_number)
            outcome,gametime = GameS.getOAT()

            if outcome == 'win':
                page = 'customwin'
            elif outcome == 'lose':
                page = 'lose'
            elif outcome == 'stopped':
                page = 'custom'
                GameS.aftergame()
                del GameS

            MenuQD.Qchange('lockscr','del')
            
        elif page == 'bestwin':
            time.sleep(0.52)
            GameS.aftergame()
            del GameS
            time.sleep(0.52)
            MenuQD.Qpicdraw('winbest',100,100,'winbest',picwidth = 200,picheight = 200)
            nameget = Entry(Point(100,132), 12)
            nameget.setFill("black")
            nameget.setTextColor("yellow")
            nameget.setSize(15)
            nameget.setFace("courier")
            nameget.setText("click & edit")
            nameget.draw(Menu)
            Menu.getMouse()
            unformedname = nameget.getText()
            nameget.undraw()
            Nlen = len(unformedname)
            if Nlen == 0:
                unformedname = 'Mystery     '
            elif Nlen <= 12:
                unformedname = unformedname+' '*(12-Nlen)
            elif Nlen > 12:
                unformedname = unformedname[0:12]
            if len(str(hh))==1:
                shh = '0'+str(hh)
            else:
                shh = str(hh)
            if len(str(mm))==1:
                smm = '0'+str(mm)
            else:
                smm = str(mm)
            if len(str(ss))==1:
                sss = '0'+str(ss)
            else:
                sss = str(ss)

            formedscore = unformedname+'/'+shh+':'+smm+':'+sss+lastbestscore[21:]
            slist[lastbestNO] = formedscore
            sfile = open('res/scosv','w')
            scoSTR = str(slist)
            sfile.write(scoSTR)
            sfile.close()
            MenuQD.Qchange('winbest','del')
            page = 'topscore'
        elif page == 'win':
            time.sleep(0.52)
            GameS.aftergame()
            del GameS
            time.sleep(0.52)
            MenuQD.Qpicdraw('winnormal',100,100,'winnormal',picwidth = 200,picheight = 200)
            time.sleep(1.52)
            MenuQD.Qchange('winnormal','del')
            page = 'topscore'
        elif page == 'customwin':
            time.sleep(0.52)
            GameS.aftergame()
            del GameS
            time.sleep(0.52)
            MenuQD.Qpicdraw('wincustom',100,100,'wincustom',picwidth = 200,picheight = 200)
            time.sleep(1.52)
            MenuQD.Qchange('wincustom','del')
            page = 'custom'
        elif page == 'lose':
            time.sleep(0.52)
            GameS.aftergame()
            del GameS
            time.sleep(0.52)
            MenuQD.Qpicdraw('nexttime',100,100,'nexttime',picwidth = 200,picheight = 200)
            time.sleep(1.52)
            MenuQD.Qchange('nexttime','del')
            page = 'main'
        








    
class StartGame:
    def __init__(self,Mwidth,Mheight,Mtype,Mine_number,Empty_number,Lock_number):        
        Mwin = Mtype+' block mine'

        if Mtype == 'retro':
            Mtitleheight = 36
            Mleftwidth = 5
            if Mwidth<=5 :
                Mwidth = 5
            if Mheight<=1 :
                Mheight = 1

        if Mtype == 'box':
            Mtitleheight = 36
            Mleftwidth = 5
            if Mwidth<=5 :
                Mwidth = 5
            if Mheight<=1 :
                Mheight = 1
                
        elif Mtype == 'hex':
            Mtitleheight = 30
            Mleftwidth = 4
            if Mwidth<=5 :
                Mwidth = 5
            if Mheight<=1 :
                Mheight = 1
                
        elif Mtype == 'tri':
            Mtitleheight = 30
            Mleftwidth = 0
            if Mwidth<=5 :
                Mwidth = 5
            if Mheight<=1 :
                Mheight = 1

        self.startgame(Mwin,Mwidth,Mheight,Mtype,Mine_number,Empty_number,Lock_number,Mtitleheight,Mleftwidth)
    
    
    def startgame(self,Mwin,Mwidth,Mheight,Mtype,Mine_number,Empty_number,Lock_number,Mtitleheight,Mleftwidth):
        
        self.Mine = MineMapMain(Mwin,Mwidth,Mheight,Mtype,Mine_number,Empty_number,Lock_number,Mtitleheight,Mleftwidth)
        self.OutcomeAndTime = self.Mine.MMMrun()

    def getOAT(self):
        return self.OutcomeAndTime
    
        if outcome == 'win':
            print 'win'
        elif outcome == 'lose':
            print 'lose'
        elif outcome == 'stopped':
            print 'stopped'

    def aftergame(self):
        self.Mine.close()
        del self.Mine

    

main()


 



    

    
