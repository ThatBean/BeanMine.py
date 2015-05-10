##MineMapDraw_Class.py

#############################
##                         ##
##  Mine Map Drawer ver2   ##
##                         ##
##              by Bean    ##
##                         ##
#############################

from graphics_edit_lite_v2 import *
        
class MineMapDraw:
    def __init__(self,window,Mtype,Map,titleheight = 20,leftwidth = 12):

        ##Reduce error rate#########################################
        try:
            #print 'here!!!\n',Map,type(Map)
            if str(type(Map)) != "<type 'list'>" :
                print 'error 1'
                return None
        except:
            print 'error 2'
            return None
        
        if Mtype != 'tri' and Mtype != 'box' and Mtype != 'hex':
            print '''Set map type error !!!\nReset to defult['box']'''
            Mtype = 'box'
        ##Set basic value###########################################
            
        self.Maptype = Mtype
        self.width = len(Map[0])
        self.height = len(Map)
        self.Map = Map
        self.win = window
        self.THeight = titleheight
        self.LWidth = leftwidth
        
        #blocknum = self.width*self.height
        
        #allblock = range(blocknum)


        ##Draw Map###########################################
    def Covered(self):
        for mh in range(self.height):
            for mw in range(self.width):
                self.blockdraw(mh+1,mw+1,self.Map[mh][mw],self.Maptype)


        ##reDraw&Uncover Map###########################################
    def ShowAll(self):
        for mh in range(self.height):
            for mw in range(self.width):
                try:
                    self.blockchange(mh+1,mw+1,self.Map[mh][mw],self.Maptype)
                except:
                    pass

                
    def picdraw(self,window,dx,dy,picn):
        self.picwin = window
        
        picroute = 'res/'+picn
        picname = 'pic_'+str(dx)+'_'+str(dy)

        exec('self.'+picname+' = Image(Point('+str(dx)+','+str(dy)+'),"'+picroute+'")')
        exec('self.'+picname+'.draw(self.picwin)')

    def picchange(self,window,dx,dy,picn = None):
        self.picwin = window
        
        picname = 'pic_'+str(dx)+'_'+str(dy)
        
        try:
            exec('self.'+picname+'.undraw()')
        except:
            return None
        
        if picn !=None:
            picroute = 'res/'+picn

            exec('self.'+picname+' = Image(Point('+str(dx)+','+str(dy)+'),"'+picroute+'")')
            exec('self.'+picname+'.draw(self.picwin)')

#############################################################
        
    def blockdraw(self,y,x,blocktype,Mtype):
        
        if blocktype == 'L':
            blocktype = 'lock'
        elif blocktype == 'D':
            blocktype = 'lock'
        elif blocktype == 'E':
            blocktype = 'empx'
        else:
            blocktype = 'grey'

        if Mtype == 'box':
            self.boxBD(x,y,blocktype)
        elif Mtype == 'tri':
            self.triBD(x,y,blocktype)
        elif Mtype == 'hex':
            self.hexBD(x,y,blocktype)
        else:
            return None

    def boxBD(self,x,y,blocktype):
        dx = self.LWidth+x*22
        dy = self.THeight+y*22
        picname = 'res/box'+blocktype
        blockname = 'box_'+str(x)+'_'+str(y)

        exec('self.'+blockname+' = Image(Point('+str(dx)+','+str(dy)+'),"'+picname+'")')
        exec('self.'+blockname+'.draw(self.win)')
        
    def hexBD(self,x,y,blocktype):
        dx = self.LWidth+x*20

        if x%2 :
            dy = self.THeight+12+y*24
        else:
            dy = self.THeight+y*24

        picname = 'res/hex'+blocktype
        blockname = 'hex_'+str(x)+'_'+str(y)
        
        exec('self.'+blockname+' = Image(Point('+str(dx)+','+str(dy)+'),"'+picname+'")')
        exec('self.'+blockname+'.draw(self.win)')
        
    def triBD(self,x,y,blocktype):
        
        if y%4 == 1 :
            dx = self.LWidth+x*36
            dy = self.THeight+((y+1)/2)*30
            tritype = 'tri2'
        elif y%4 == 2 :
            dx = self.LWidth+18+x*36
            dy = self.THeight+2+((y+1)/2)*30
            tritype = 'tri1'
        elif y%4 == 3 :
            dx = self.LWidth+18+x*36
            dy = self.THeight+((y+1)/2)*30
            tritype = 'tri2'
        else:
            dx = self.LWidth+x*36
            dy = self.THeight+2+((y+1)/2)*30
            tritype = 'tri1'
        picname = 'res/'+tritype+blocktype
        blockname = 'hex_'+str(x)+'_'+str(y)
        exec('self.'+blockname+' = Image(Point('+str(dx)+','+str(dy)+'),"'+picname+'")')
        exec('self.'+blockname+'.draw(self.win)')

#############################################################
        
    def blockchange(self,y,x,blocktype,Mtype):
        
        if blocktype == 'L':
            return
        elif blocktype == 'E':
            return
        elif blocktype == 'D':
            blocktype = 'mine'
        elif blocktype == 'M':
            blocktype = 'mine'
        elif blocktype == '0':
            blocktype = 'emp'
        elif blocktype == 'clicked':
            blocktype = 'CL'
        elif blocktype == 'marked':
            blocktype = 'MK'
        elif blocktype == 'unmarked':
            blocktype = 'grey'

        if Mtype == 'box':
            self.boxBC(x,y,blocktype)
        elif Mtype == 'tri':
            self.triBC(x,y,blocktype)
        elif Mtype == 'hex':
            self.hexBC(x,y,blocktype)
        else:
            return None

    def boxBC(self,x,y,blocktype):            
        dx = self.LWidth+x*22
        dy = self.THeight+y*22
        
        blockname = 'box_'+str(x)+'_'+str(y)
        exec('self.'+blockname+'.undraw()')
        exec('self.'+blockname+'emp = Image(Point('+str(dx)+','+str(dy)+'),"res/boxemp")')
        exec('self.'+blockname+'emp.draw(self.win)')
        
        if blocktype == 'mine':
            blocktype = 'mine'
            picname = 'res/mine'
            
        elif blocktype == 'CL':
            exec('self.'+blockname+'emp.undraw()')
            blocktype = 'dark'
            picname = 'res/box'+blocktype

        elif blocktype == 'MK':
            exec('self.'+blockname+'emp.undraw()')
            blocktype = 'mark'
            picname = 'res/box'+blocktype

        elif blocktype == 'grey':
            exec('self.'+blockname+'emp.undraw()')
            picname = 'res/box'+blocktype
            
        elif blocktype == 'emp':
            return

        else:
            picname = 'res/'+blocktype

        exec('self.'+blockname+' = Image(Point('+str(dx)+','+str(dy)+'),"'+picname+'")')
        exec('self.'+blockname+'.draw(self.win)')
        
    def hexBC(self,x,y,blocktype):
        dx = self.LWidth+x*20

        if x%2 :
            dy = self.THeight+12+y*24
        else:
            dy = self.THeight+y*24

        blockname = 'hex_'+str(x)+'_'+str(y)
        exec('self.'+blockname+'.undraw()')
        exec('self.'+blockname+'emp = Image(Point('+str(dx)+','+str(dy)+'),"res/hexemp")')
        exec('self.'+blockname+'emp.draw(self.win)')
                
        if blocktype == 'mine':
            blocktype = 'mine'
            picname = 'res/mine'
            
        elif blocktype == 'CL':
            blocktype = 'dark'
            picname = 'res/hex'+blocktype

        elif blocktype == 'MK':
            exec('self.'+blockname+'emp.undraw()')
            blocktype = 'mark'
            picname = 'res/hex'+blocktype

        elif blocktype == 'grey':
            exec('self.'+blockname+'emp.undraw()')
            picname = 'res/hex'+blocktype
            
        elif blocktype == 'emp':
            return

        else:
            picname = 'res/'+blocktype

        exec('self.'+blockname+' = Image(Point('+str(dx)+','+str(dy)+'),"'+picname+'")')
        exec('self.'+blockname+'.draw(self.win)')
        
    def triBC(self,x,y,blocktype):
        
        if y%4 == 1 :
            dx = self.LWidth+x*36
            dy = self.THeight+((y+1)/2)*30
            tritype = 'tri2'
            fix = -4
        elif y%4 == 2 :
            dx = self.LWidth+18+x*36
            dy = self.THeight+2+((y+1)/2)*30
            tritype = 'tri1'
            fix = +4
        elif y%4 == 3 :
            dx = self.LWidth+18+x*36
            dy = self.THeight+((y+1)/2)*30
            tritype = 'tri2'
            fix = -4
        else:
            dx = self.LWidth+x*36
            dy = self.THeight+2+((y+1)/2)*30
            tritype = 'tri1'
            fix = +4
        
        blockname = 'hex_'+str(x)+'_'+str(y)
        exec('self.'+blockname+'.undraw()')
        exec('self.'+blockname+'emp = Image(Point('+str(dx)+','+str(dy)+'),"res/'+tritype+'emp")')
        exec('self.'+blockname+'emp.draw(self.win)')

        isNum = 1        
        if blocktype == 'mine':
            blocktype = 'mine'
            picname = 'res/mine'
            isNum = 0
            
        elif blocktype == 'CL':
            blocktype = 'dark'
            picname = 'res/'+tritype+blocktype
            isNum = 0

        elif blocktype == 'MK':
            exec('self.'+blockname+'emp.undraw()')
            blocktype = 'mark'
            picname = 'res/'+tritype+blocktype
            isNum = 0

        elif blocktype == 'grey':
            exec('self.'+blockname+'emp.undraw()')
            picname = 'res/'+tritype+blocktype
            isNum = 0
            
        elif blocktype == 'emp':
            return

        else:
            picname = 'res/'+blocktype
            
        if isNum == 1:
            exec('self.'+blockname+' = Image(Point('+str(dx)+','+str(dy+fix)+'),"'+picname+'")')
            exec('self.'+blockname+'.draw(self.win)')
        else:
            exec('self.'+blockname+' = Image(Point('+str(dx)+','+str(dy)+'),"'+picname+'")')
            exec('self.'+blockname+'.draw(self.win)')
