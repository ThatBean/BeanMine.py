##MineMapMain_Class.py

#############################
##                         ##
##  Mine Map Main  ver2    ##
##                         ##
##              by Bean    ##
##                         ##
#############################

from graphics_edit_lite_v2 import *
from MineMapMake_Class import *
from MineMapMouse_Class import *
from MineMapDraw_Class import *

class SetStatus:
    def __init__(self,win,width,Mtype):
        self.win = win
        
        self.hour=0
        self.minute=0
        self.sec=0
        self.Mine=0
        self.BlockMarked=0
        self.facex=0
        
        #print width

        faceN = Mtype
        if Mtype == 'retrobox':
            faceN = 'retro'

        self.faceN = faceN

        if width <= 180:
            self.Qpicdraw('face',width/2+12,25,faceN+'smile')
            self.facex=width/2+12

            self.Qpicdraw('minute1',12,25,'N0')
            self.Qpicdraw('minute2',32,25,'N0')
            self.Qpicdraw('split2',44,25,'Ni')
            self.Qpicdraw('sec1',56,25,'N0')
                  
            self.Qpicdraw('Mine1',width-30,25,'N0')
            self.Qpicdraw('Mine2',width-10,25,'N0')
            
        elif width <=250:
            self.Qpicdraw('face',width/2+2,25,faceN+'smile')
            self.facex=width/2+2
        
            self.Qpicdraw('minute1',12,25,'N0')
            self.Qpicdraw('minute2',30,25,'N0')
            self.Qpicdraw('split2',42,25,'Ni')
            self.Qpicdraw('sec1',54,25,'N0')
            self.Qpicdraw('sec2',72,25,'N0')
                   
            self.Qpicdraw('Mine1',width-68,25,'N0')
            self.Qpicdraw('Mine2',width-50,25,'N0')
                   
            self.Qpicdraw('BlockMarked1',width-26,25,'N0')
            self.Qpicdraw('BlockMarked2',width-8,25,'N0')
        elif width <= 330:
            self.Qpicdraw('face',width/2,25,faceN+'smile')
            self.facex=width/2

            self.Qpicdraw('time',12,25,'smalltime')        
            self.Qpicdraw('minute1',32,25,'N0')
            self.Qpicdraw('minute2',50,25,'N0')
            self.Qpicdraw('split2',62,25,'Ni')
            self.Qpicdraw('sec1',74,25,'N0')
            self.Qpicdraw('sec2',92,25,'N0')
            
            self.Qpicdraw('Mine',width-104,25,'smallmine')
            self.Qpicdraw('Mine1',width-84,25,'N0')
            self.Qpicdraw('Mine2',width-66,25,'N0')
            
            self.Qpicdraw('BlockMarked',width-44,25,'smallmarked')        
            self.Qpicdraw('BlockMarked1',width-26,25,'N0')
            self.Qpicdraw('BlockMarked2',width-8,25,'N0')
        elif width <= 400:
            self.Qpicdraw('face',width/2,25,faceN+'smile')
            self.facex=width/2

            self.Qpicdraw('time',12,25,'smalltime')
            self.Qpicdraw('hour1',32,25,'N0')
            self.Qpicdraw('hour2',50,25,'N0')
            self.Qpicdraw('split1',62,25,'Ni')
            self.Qpicdraw('minute1',74,25,'N0')
            self.Qpicdraw('minute2',92,25,'N0')
            self.Qpicdraw('split2',104,25,'Ni')
            self.Qpicdraw('sec1',116,25,'N0')
            self.Qpicdraw('sec2',134,25,'N0')
            
            self.Qpicdraw('Mine',width-114,25,'smallmine')
            self.Qpicdraw('Mine1',width-94,25,'N0')
            self.Qpicdraw('Mine2',width-76,25,'N0')
            
            self.Qpicdraw('BlockMarked',width-48,25,'smallmarked')        
            self.Qpicdraw('BlockMarked1',width-28,25,'N0')
            self.Qpicdraw('BlockMarked2',width-10,25,'N0')
        else :
            self.Qpicdraw('face',width/2,25,faceN+'smile')
            self.facex=width/2

            self.Qpicdraw('time',20,25,'bigtime')
            self.Qpicdraw('hour1',44,25,'N0')
            self.Qpicdraw('hour2',62,25,'N0')
            self.Qpicdraw('split1',74,25,'Ni')
            self.Qpicdraw('minute1',86,25,'N0')
            self.Qpicdraw('minute2',104,25,'N0')
            self.Qpicdraw('split2',116,25,'Ni')
            self.Qpicdraw('sec1',128,25,'N0')
            self.Qpicdraw('sec2',146,25,'N0')
            
            self.Qpicdraw('Mine',width-128,25,'bigmine')
            self.Qpicdraw('Mine1',width-104,25,'N0')
            self.Qpicdraw('Mine2',width-86,25,'N0')
            
            self.Qpicdraw('BlockMarked',width-52,25,'bigmarked')        
            self.Qpicdraw('BlockMarked1',width-28,25,'N0')
            self.Qpicdraw('BlockMarked2',width-10,25,'N0')

        
     
    def start(self,mine):
        self.StartTime = time.clock()
        Mine = str(mine)
        if len(str(Mine))==1:
            
            self.Qchange('Mine1','N0')
            self.Qchange('Mine2','N'+Mine)

        else:
            self.Qchange('Mine1','N'+Mine[0])
            self.Qchange('Mine2','N'+Mine[1])
            
    def Qpicdraw(self,elemName,x,y,picName):
        point = 'Point('+str(x)+','+str(y)+')'
        picsite = 'res/'+picName
        exec('self.'+elemName+' = Image('+point+',"'+picsite+'")')
        exec('self.'+elemName+'.draw(self.win)')
        exec('self.'+elemName+'xy = (x,y)')
             
    def Qchange(self,elemName,picName):
        try:
            exec('x,y = self.'+elemName+'xy')
        except:
            return
        point = 'Point('+str(x)+','+str(y)+')'
        picsite = 'res/'+picName
        exec('self.'+elemName+'.undraw()')
        exec('self.'+elemName+' = Image('+point+',"'+picsite+'")')
        exec('self.'+elemName+'.draw(self.win)')
        
    def close(self):
        self.win.close()

    def gettime(self):
        return (self.hour,self.minute,self.sec)

    def facechange(self,Ftype):
        self.Qchange('face',self.faceN+Ftype)

    def faceCckeck(self,point):
        x = point.getX()
        y = point.getY()
        if x < self.facex+12 and x > self.facex-12 and y < 37 and y > 13:
            return True
        else:
            return False
        
    def settime(self,BlockMarked):
        if BlockMarked != self.BlockMarked:
            self.BlockMarked=BlockMarked
            BMarked = str(BlockMarked)
            if len(str(BMarked))==1:
                self.Qchange('BlockMarked1','N0')
                self.Qchange('BlockMarked2','N'+BMarked)

            else:
                self.Qchange('BlockMarked1','N'+BMarked[0])
                self.Qchange('BlockMarked2','N'+BMarked[1])
            
        tmn = time.clock()
        tm = tmn-self.StartTime
        hour = int(tm/3600)
        minute = int(tm/60)
        sec = int((tm%60))
        if sec != self.sec:
            self.sec=sec
            Msec = str(sec)
            if len(str(Msec))==1:
                self.Qchange('sec1','N0')
                self.Qchange('sec2','N'+Msec)

            else:
                self.Qchange('sec1','N'+Msec[0])
                self.Qchange('sec2','N'+Msec[1])

        if minute != self.minute:
            self.minute=minute
            Mminute = str(minute)
            if len(str(Mminute))==1:
                self.Qchange('minute1','N0')
                self.Qchange('minute2','N'+Mminute)

            else:
                self.Qchange('minute1','N'+Mminute[0])
                self.Qchange('minute2','N'+Mminute[1])
            
        if hour != self.hour:
            self.hour=hour
            Mhour = str(hour)
            if len(str(Mhour))==1:
                self.Qchange('hour1','N0')
                self.Qchange('hour2','N'+Mhour)

            else:
                self.Qchange('hour1','N'+Mhour[0])
                self.Qchange('hour2','N'+Mhour[1])        
        
class MineMapMain:
    def __init__(self,win,width,height,Mtype,M,E,L,titleheight = 20,leftwidth = 12):
        self.win = win
        self.height = height
        self.width = width
        self.THeight = titleheight
        self.LWidth = leftwidth
        self.Mtype = Mtype
        self.MEL = (M,E,L)
        self.minemarked = 0
        self.blockmarked = 0
        self.totalfliped = 0
        self.die = 0
        self.outcome = ''
        self.flipedb = []
        for i in range(width*height):
            self.flipedb.append(0)
    def reset(self,win,width,height,Mtype,M,E,L,titleheight = 20,leftwidth = 12):
        try:
            if self.win.isOpen():
                self.win.close()
        except:
            pass

        self.win = win
        self.height = height
        self.width = width
        self.THeight = titleheight
        self.LWidth = leftwidth
        self.Mtype = Mtype
        self.MEL = (M,E,L)
        self.minemarked = 0
        self.blockmarked = 0
        self.totalfliped = 0
        self.die = 0
        self.outcome = ''
        self.flipedb = []
        for i in range(width*height):
            self.flipedb.append(0)
        

    def MMMrun(self):

        Mwidth = self.width
        Mheight = self.height
        Mtype = self.Mtype
        SSfix = ''
        if Mtype == 'retro':
            Mtype = 'box'
            self.Mtype = 'box'
            SSfix = 'retro'
        Mine_number,Empty_number,Lock_number = self.MEL
        Mwin = Mtype+'block mine'
        Mtitleheight = self.THeight
        Mleftwidth = self.LWidth
        self.TotalEmpBlock = 0
        self.TotalMineMarkable = 0

        self.mine = MineMapMake(Mwidth,Mheight,Mtype,Mine_number,Empty_number,Lock_number)

        self.UnFormed_Map = self.mine.get_orgMap()
        
        self.mine.mapForm()
        self.Formed_Map = self.mine.get_Map()
        #for i in range(Mheight):
            #print self.Formed_Map[i]
        
        for i in range(Mheight):
            for ii in range(Mwidth):
                if self.UnFormed_Map[i][ii] == 'M':
                    self.TotalMineMarkable += 1
                if self.UnFormed_Map[i][ii] == '0':
                    self.TotalEmpBlock += 1
        
        ######################################
        
        wid = Mwidth+1
        hei = Mheight+1
        if self.Mtype == 'box':
            Wwidth =22*wid+2*Mleftwidth-2
            Wheight = 22*hei+Mtitleheight+2
        if self.Mtype == 'hex':
            Wwidth =20*wid+2*Mleftwidth
            Wheight = 24*hei+Mtitleheight+5
        if self.Mtype == 'tri':
            Wwidth =36*wid+2*Mleftwidth+15
            Wheight = 30*(hei/2)+Mtitleheight+25
        self.win = GraphWin(Mwin,Wwidth,Wheight)
        self.win.setBackground("black")
        
        self.win.setIcon('res/icon')

        self.SS = SetStatus(self.win,Wwidth,SSfix+Mtype)

        self.screenmap = MineMapDraw(self.win,Mtype,self.Formed_Map,Mtitleheight,Mleftwidth)
        self.screenmap.Covered()
        self.screenmouse = MineMapMouse(self.win,Mwidth,Mheight,Mtype,Mtitleheight,Mleftwidth)

        self.stop = 0
                
        PointAndType = (self.win.getMouse(),'Bean')
        
        self.SS.start(Mine_number)
        
        while self.stop == 0:
            if PointAndType != None:
                point,ptype = PointAndType
                #print point,ptype
                locatedx,locatedy = self.screenmouse.mouselocate(point)
                #print locatedx,locatedy
                if locatedx>0 and locatedy>0 and locatedx<=self.width and locatedy<=self.height :
                    self.SS.facechange('oops')
                    if ptype[0] == 'C':
                        point,ptype = self.clickedblock(locatedx,locatedy)
                        locatedx,locatedy = self.screenmouse.mouselocate(point)
                        if locatedx<=0 or locatedy<=0 or locatedx>self.width or locatedy>self.height :
                            ptype = None
                    if ptype == 'R1':
                        self.flipblock(locatedx,locatedy)
                    elif ptype == 'R2':
                        self.detectblock(locatedx,locatedy)
                    elif ptype == 'R3':
                        self.markblock(locatedx,locatedy)
                    #print self.Formed_Map[locatedy-1][locatedx-1]
                    self.SS.facechange('smile')
                elif ptype[0] == 'R':
                    if self.SS.faceCckeck(point):
                        self.stop = 1
                        self.outcome = 'stopped'
            if self.minemarked == self.TotalMineMarkable and self.blockmarked == self.TotalMineMarkable:
                self.stop = 1
                self.outcome = 'win'
            if self.die == 1:
                self.stop = 1
                self.outcome = 'lose' 
            PointAndType = self.win.eyeMouse()

            self.SS.settime(self.blockmarked)
                
        if self.outcome != 'win':
            self.screenmap.ShowAll()

        gametime = self.SS.gettime()
        return self.outcome,gametime


    def close(self):
        self.win.close()

########################################################################
        
##Clicked Block############################################################
    def clickedblock(self,x,y):
        self.lastclicked = None
        if x>0 and y>0 and x<=self.width and y<=self.height :
            if self.flipedb[y*self.width-self.width+x-1] == 0:
                if self.UnFormed_Map[y-1][x-1] == '0' or self.UnFormed_Map[y-1][x-1] == 'M':
                    self.lastclicked = (x,y)
                    self.screenmap.blockchange(y,x,'clicked',self.Mtype)
        clickedstop = 0
        while clickedstop ==0 :
            self.SS.settime(self.blockmarked)
            
            PointAndType = self.win.eyeMouse()
            if PointAndType != None:
                point,ptype = PointAndType
                if ptype[0] == 'R':
                    clickedstop = 1
                elif ptype[0] == 'C':
                    self.ClickedMove(point)
        if self.lastclicked != None:
            lx,ly = self.lastclicked
            self.screenmap.blockchange(ly,lx,'grey',self.Mtype)
            self.lastclicked = None
        return point,ptype
                
    def ClickedMove(self,point):
        x,y = self.screenmouse.mouselocate(point)
        if self.lastclicked != None:
            lx,ly = self.lastclicked
            if x ==lx and y == ly :
                return
            self.screenmap.blockchange(ly,lx,'grey',self.Mtype)
            self.lastclicked = None
        if x>0 and y>0 and x<=self.width and y<=self.height :
            if self.flipedb[y*self.width-self.width+x-1] == 0:
                if self.UnFormed_Map[y-1][x-1] == '0' or self.UnFormed_Map[y-1][x-1] == 'M':
                    self.lastclicked = (x,y)
                    self.screenmap.blockchange(y,x,'clicked',self.Mtype)

        
##Mark Block############################################################
    def markblock(self,x,y):
        if self.flipedb[y*self.width-self.width+x-1] == 1:
            return 
        elif self.flipedb[y*self.width-self.width+x-1] == 0:
            tblock = self.Formed_Map[y-1][x-1]
            if  tblock== 'E':
                return 
            elif tblock == 'D':
                return 
            elif tblock == 'L':
                return 
            elif tblock == 'M':
                self.minemarked += 1
            self.blockmarked += 1     
            self.screenmap.blockchange(y,x,'marked',self.Mtype)        
            self.flipedb[y*self.width-self.width+x-1] = 2
            return
        elif self.flipedb[y*self.width-self.width+x-1] == 2:
            tblock = self.Formed_Map[y-1][x-1]
            if  tblock== 'E':
                return 
            elif tblock == 'D':
                return 
            elif tblock == 'L':
                return 
            elif tblock == 'M':
                self.minemarked += -1
            self.blockmarked += -1     
            self.screenmap.blockchange(y,x,'unmarked',self.Mtype)        
            self.flipedb[y*self.width-self.width+x-1] = 0
            return

##Flip Block###########################################################
    def flipblock(self,x,y):
        if self.flipedb[y*self.width-self.width+x-1] != 0:
            return 
        if self.Mtype == 'box':
            self.boxflip(x,y)
        elif self.Mtype == 'hex':
            self.hexflip(x,y)
        elif self.Mtype == 'tri':
            self.triflip(x,y)
        return 
    def chainflip(self,x,y):
        self.SS.settime(self.blockmarked)
        if x<=0 or y <=0 or x>self.width or y>self.height :
            return
        if self.flipedb[y*self.width-self.width+x-1] != 0 or self.UnFormed_Map[y-1][x-1] != '0':
            return
        if self.Mtype == 'box':
            self.boxflip(x,y)
        elif self.Mtype == 'hex':
            self.hexflip(x,y)
        elif self.Mtype == 'tri':
            self.triflip(x,y)
        return
    def boxflip(self,x,y):
        tblock = self.Formed_Map[y-1][x-1]
        if  tblock== 'E':
            return 
        elif tblock == 'D':
            return 
        elif tblock == 'L':
            return 
        elif tblock == 'M':
            self.die = 1
            return 
        self.screenmap.blockchange(y,x,self.Formed_Map[y-1][x-1],self.Mtype)
        #print '(',x,',',y,')fliped'
        
        self.flipedb[y*self.width-self.width+x-1] = 1
        self.totalfliped += 1
        if self.totalfliped == self.TotalEmpBlock:
            self.stop = 1
            self.outcome = 'win'

        if self.Formed_Map[y-1][x-1] == '0':
            self.chainflip(x-1,y-1)
            self.chainflip(x-1,y)
            self.chainflip(x-1,y+1)
            self.chainflip(x,y-1)
            self.chainflip(x,y+1)
            self.chainflip(x+1,y-1)
            self.chainflip(x+1,y)
            self.chainflip(x+1,y+1)
        
        return 
    def hexflip(self,x,y):
        tblock = self.Formed_Map[y-1][x-1]
        if  tblock== 'E':
            return 
        elif tblock == 'D':
            return 
        elif tblock == 'L':
            return 
        elif tblock == 'M':
            self.die = 1
            return 
        self.screenmap.blockchange(y,x,self.Formed_Map[y-1][x-1],self.Mtype)
        #print '(',x,',',y,')fliped'
        self.flipedb[y*self.width-self.width+x-1] = 1
        self.totalfliped += 1
        if self.totalfliped == self.TotalEmpBlock:
            self.stop = 1
            self.outcome = 'win'

        if self.Formed_Map[y-1][x-1] == '0':
            if y%2:
                self.chainflip(x-1,y)
                self.chainflip(x-1,y+1)
                self.chainflip(x,y-1)
                self.chainflip(x,y+1)
                self.chainflip(x+1,y)
                self.chainflip(x+1,y+1)
            else:
                self.chainflip(x-1,y-1)
                self.chainflip(x-1,y)
                self.chainflip(x,y-1)
                self.chainflip(x,y+1)
                self.chainflip(x+1,y-1)
        return 
    def triflip(self,x,y):
        tblock = self.Formed_Map[y-1][x-1]
        if  tblock== 'E':
            return 
        elif tblock == 'D':
            return 
        elif tblock == 'L':
            return 
        elif tblock == 'M':
            self.die = 1
            return 
        self.screenmap.blockchange(y,x,self.Formed_Map[y-1][x-1],self.Mtype)
        #print '(',x,',',y,')fliped'
        
        self.flipedb[y*self.width-self.width+x-1] = 1
        self.totalfliped += 1
        if self.totalfliped == self.TotalEmpBlock:
            self.stop = 1
            self.outcome = 'win'

        if self.Formed_Map[y-1][x-1] == '0':
            if y%4 == 1:
                self.chainflip(x-2,y-1)
                self.chainflip(x-2,y)
                self.chainflip(x-1,y-1)
                self.chainflip(x-1,y)
                self.chainflip(x-1,y+1)
                self.chainflip(x,y-1)
                self.chainflip(x,y+1)
                self.chainflip(x+1,y-1)
                self.chainflip(x+1,y)
                self.chainflip(x+2,y-1)
                self.chainflip(x+2,y)
                self.chainflip(x+3,y)
            elif y%4 == 2:
                self.chainflip(x-3,y)
                self.chainflip(x-2,y)
                self.chainflip(x-2,y+1)
                self.chainflip(x-1,y)
                self.chainflip(x-1,y+1)
                self.chainflip(x,y-1)
                self.chainflip(x,y+1)
                self.chainflip(x+1,y-1)
                self.chainflip(x+1,y)
                self.chainflip(x+1,y+1)
                self.chainflip(x+2,y)
                self.chainflip(x+2,y+1)
            elif y%4 == 3:
                self.chainflip(x-2,y)
                self.chainflip(x-2,y+1)
                self.chainflip(x-1,y-1)
                self.chainflip(x-1,y)
                self.chainflip(x-1,y+1)
                self.chainflip(x,y-1)
                self.chainflip(x,y+1)
                self.chainflip(x+1,y)
                self.chainflip(x+1,y+1)
                self.chainflip(x+2,y)
                self.chainflip(x+2,y+1)
                self.chainflip(x+3,y)
            else:
                self.chainflip(x-3,y)
                self.chainflip(x-2,y-1)
                self.chainflip(x-2,y)
                self.chainflip(x-1,y-1)
                self.chainflip(x-1,y)
                self.chainflip(x-1,y+1)
                self.chainflip(x,y-1)
                self.chainflip(x,y+1)
                self.chainflip(x+1,y-1)
                self.chainflip(x+1,y)
                self.chainflip(x+1,y+1)
                self.chainflip(x+2,y-1)
                self.chainflip(x+2,y)
        return 
       
##Detect Block###########################################################
    def detectblock(self,x,y):
        if self.flipedb[y*self.width-self.width+x-1] != 1:
            return 
        if self.Mtype == 'box':
            self.boxdetect(x,y)
        elif self.Mtype == 'hex':
            self.hexdetect(x,y)
        elif self.Mtype == 'tri':
            self.tridetect(x,y)
        return 
    def markeddetect(self,x,y):
        if x<=0 or y <=0 or x>self.width or y>self.height :
            return 0
        elif self.flipedb[y*self.width-self.width+x-1] == 2:
            return 1
        else:
            return 0
    def boxdetect(self,x,y):
        minemarked = self.markeddetect(x-1,y-1)+self.markeddetect(x-1,y)+self.markeddetect(x-1,y+1)+self.markeddetect(x,y-1)+self.markeddetect(x,y+1)+self.markeddetect(x+1,y-1)+self.markeddetect(x+1,y)+self.markeddetect(x+1,y+1)
        if self.Formed_Map[y-1][x-1] == str(minemarked):
            self.chainflip(x-1,y-1)
            self.chainflip(x-1,y)
            self.chainflip(x-1,y+1)
            self.chainflip(x,y-1)
            self.chainflip(x,y+1)
            self.chainflip(x+1,y-1)
            self.chainflip(x+1,y)
            self.chainflip(x+1,y+1)        
        return 
    def hexdetect(self,x,y):
        if y%2:
            minemarked = self.markeddetect(x-1,y)+self.markeddetect(x-1,y+1)+self.markeddetect(x,y-1)+self.markeddetect(x,y+1)+self.markeddetect(x+1,y)+self.markeddetect(x+1,y+1)
        else:
            minemarked = self.markeddetect(x-1,y-1)+self.markeddetect(x-1,y)+self.markeddetect(x,y-1)+self.markeddetect(x,y+1)+self.markeddetect(x+1,y-1)+self.markeddetect(x+1,y)

        if self.Formed_Map[y-1][x-1] == str(minemarked):
            if y%2:
                self.chainflip(x-1,y)
                self.chainflip(x-1,y+1)
                self.chainflip(x,y-1)
                self.chainflip(x,y+1)
                self.chainflip(x+1,y)
                self.chainflip(x+1,y+1)
            else:
                self.chainflip(x-1,y-1)
                self.chainflip(x-1,y)
                self.chainflip(x,y-1)
                self.chainflip(x,y+1)
                self.chainflip(x+1,y-1)
                self.chainflip(x+1,y)
        return 
    def tridetect(self,x,y):
        if y%4 == 1:
            minemarked = self.markeddetect(x-2,y-1)+self.markeddetect(x-2,y)+self.markeddetect(x-1,y-1)+self.markeddetect(x-1,y)+self.markeddetect(x-1,y+1)+self.markeddetect(x,y-1)+self.markeddetect(x,y+1)+self.markeddetect(x+1,y-1)+self.markeddetect(x+1,y)+self.markeddetect(x+2,y-1)+self.markeddetect(x+2,y)+self.markeddetect(x+3,y)
        elif y%4 == 2:
            minemarked = self.markeddetect(x-3,y)+self.markeddetect(x-2,y)+self.markeddetect(x-2,y+1)+self.markeddetect(x-1,y)+self.markeddetect(x-1,y+1)+self.markeddetect(x,y-1)+self.markeddetect(x,y+1)+self.markeddetect(x+1,y-1)+self.markeddetect(x+1,y)+self.markeddetect(x+1,y+1)+self.markeddetect(x+2,y)+self.markeddetect(x+2,y+1)
        elif y%4 == 3:
            minemarked = self.markeddetect(x-2,y)+self.markeddetect(x-2,y+1)+self.markeddetect(x-1,y-1)+self.markeddetect(x-1,y)+self.markeddetect(x-1,y+1)+self.markeddetect(x,y-1)+self.markeddetect(x,y+1)+self.markeddetect(x+1,y)+self.markeddetect(x+1,y+1)+self.markeddetect(x+2,y)+self.markeddetect(x+2,y+1)+self.markeddetect(x+3,y)
        else:
            minemarked = self.markeddetect(x-3,y)+self.markeddetect(x-2,y-1)+self.markeddetect(x-2,y)+self.markeddetect(x-1,y-1)+self.markeddetect(x-1,y)+self.markeddetect(x-1,y+1)+self.markeddetect(x,y-1)+self.markeddetect(x,y+1)+self.markeddetect(x+1,y-1)+self.markeddetect(x+1,y)+self.markeddetect(x+1,y+1)+self.markeddetect(x+2,y-1)+self.markeddetect(x+2,y)
        if self.Formed_Map[y-1][x-1] == str(minemarked):
            if y%4 == 1:
                self.chainflip(x-2,y-1)
                self.chainflip(x-2,y)
                self.chainflip(x-1,y-1)
                self.chainflip(x-1,y)
                self.chainflip(x-1,y+1)
                self.chainflip(x,y-1)
                self.chainflip(x,y+1)
                self.chainflip(x+1,y-1)
                self.chainflip(x+1,y)
                self.chainflip(x+2,y-1)
                self.chainflip(x+2,y)
                self.chainflip(x+3,y)
            elif y%4 == 2:
                self.chainflip(x-3,y)
                self.chainflip(x-2,y)
                self.chainflip(x-2,y+1)
                self.chainflip(x-1,y)
                self.chainflip(x-1,y+1)
                self.chainflip(x,y-1)
                self.chainflip(x,y+1)
                self.chainflip(x+1,y-1)
                self.chainflip(x+1,y)
                self.chainflip(x+1,y+1)
                self.chainflip(x+2,y)
                self.chainflip(x+2,y+1)
            elif y%4 == 3:
                self.chainflip(x-2,y)
                self.chainflip(x-2,y+1)
                self.chainflip(x-1,y-1)
                self.chainflip(x-1,y)
                self.chainflip(x-1,y+1)
                self.chainflip(x,y-1)
                self.chainflip(x,y+1)
                self.chainflip(x+1,y)
                self.chainflip(x+1,y+1)
                self.chainflip(x+2,y)
                self.chainflip(x+2,y+1)
                self.chainflip(x+3,y)
            else:
                self.chainflip(x-3,y)
                self.chainflip(x-2,y-1)
                self.chainflip(x-2,y)
                self.chainflip(x-1,y-1)
                self.chainflip(x-1,y)
                self.chainflip(x-1,y+1)
                self.chainflip(x,y-1)
                self.chainflip(x,y+1)
                self.chainflip(x+1,y-1)
                self.chainflip(x+1,y)
                self.chainflip(x+1,y+1)
                self.chainflip(x+2,y-1)
                self.chainflip(x+2,y)
        return
