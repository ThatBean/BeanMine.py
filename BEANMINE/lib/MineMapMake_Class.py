##MineMapMake_Class.py

#############################
##                         ##
##  Mine Map Maker ver2.2  ##
##                         ##
##              by Bean    ##
##                         ##
#############################
import random

class MineMapMake:
    def __init__(self,width,height,Mtype = 'box',Mnum = 0,Enum = 0,Lnum = 0):

        ##Reduce error rate#########################################
        try:
            if int(width)!=width or int(height)!=height or int(Mnum)!=Mnum or int(Enum)!=Enum or int(Lnum)!=Lnum :
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
        self.width = width
        self.height = height
        self.ObjNum = [Mnum,Enum,Lnum]
        self.Map = []
        self.orgMap = []
        tempMap = []
        doneMap = []
        self.blocknum = width*height
        blocknum = width*height
        
        allblock = range(blocknum)
        tempMap = range(blocknum)
        doneMap = range(blocknum)
        
        for i in allblock:
            doneMap[i] = 0
            
        Temp = []
        udfblockleft = blocknum
        
        try:

            ##Get Emp Block#######################################
            
            empget = random.sample(tempMap,Enum)

            for i in allblock:
                for ii in range(len(empget)):
                    if allblock[i] == empget[ii]:
                        tempMap[i] = 0
                        doneMap[i] = 'E'

            Temp = tempMap
            tempMap = []

            for i in range(udfblockleft):
                if Temp[i] != 0:
                    tempMap.append(Temp[i])

            udfblockleft = len(tempMap)

            ##Get Lock Block & Mine Block########################

            lockget = random.sample(tempMap,Lnum)
            mineget = random.sample(tempMap,Mnum)

            for i in allblock:
                for ii in range(Lnum):
                    if allblock[i] == lockget[ii]:
                        doneMap[i] = 'L'

            for i in allblock:
                for ii in range(Mnum):
                    if allblock[i] == mineget[ii]:
                        MapVal = str(doneMap[i])
                        if MapVal == '0':
                            doneMap[i] = 'M'
                        else:
                            doneMap[i] = 'D'

            for i in range(udfblockleft):
                for ii in range(Lnum):
                    if tempMap[i] == lockget[ii]:
                        tempMap[i] = 0
                for ii in range(Mnum):
                    if tempMap[i] == mineget[ii]:
                        tempMap[i] = 0

            Temp = tempMap
            tempMap = []

            for i in range(udfblockleft):
                if Temp[i] != 0:
                    tempMap.append(Temp[i])

            udfblockleft = len(tempMap)

        except:
            print 'error 3'
            return None

        ##For test use########################################
        #print 'EMP :',len(empget),empget,'\n','Mine:',len(mineget),mineget,'\n','Lock::',len(lockget),lockget,'\n',doneMap
        #for i in range(height):
        #    for ii in range(width):
        #        print str(doneMap[i*width+ii]),
        #    print '//'
        #####################################################

        ##Reform map#################################

        tempMap = doneMap
        doneMap = []
        doneLine = []
        base = 0
        for i in range(height):
            for ii in range(width):
                Bnum = base + ii
                #print Bnum
                doneLine.append(str(tempMap[Bnum]))
            base = (1+i)*width
            doneMap.append(doneLine)
            doneLine = []

        self.orgMap = doneMap
    ##data det func###################################
        
    def get_orgMap(self):
        return self.orgMap

    def get_Map(self):
        return self.Map

    def get_MapValue(self):
        return (self.Maptype,self.width,self.height,self.ObjNum,self.Map)
    
    ##Reset map type#################################
    
    def mapRetype(self,Mtype):
        if Mtype != 'tri' and Mtype != 'box' and Mtype != 'hex':
            print '''Set map type error !!!\nReset to defult['box']'''
            Mtype = 'box'
        self.Maptype = Mtype

    ##Calculate numbers in block(Indicates Mine)##########################
    def mapForm(self):
        Mtype = self.Maptype
        if Mtype == 'box':
            self.BoxBlockReform()
        elif Mtype == 'hex':
            self.HexBlockReform()
        elif Mtype == 'tri':
            self.TriBlockReform()

    ##Calculate numbers in rectangle-block######################
    def BoxBlockReform(self):
        width = self.width
        height = self.height
        Map = self.orgMap
        tempMap = range(width*height)
        for i in range(height):
            for ii in range(width):
                BlockObj = Map[i][ii]
                MineN = 0
                if BlockObj == '0':
                    if i == 0 :
                        if ii == 0:
                            if height == 1:
                                MineN =DMine(Map[i][ii+1])
                            else:
                                MineN =DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])
                        elif ii == width-1 :
                            if height == 1:
                                MineN =DMine(Map[i][ii-1])
                            else:
                                MineN =DMine(Map[i][ii-1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])
                        else:
                            if height == 1:
                                MineN =DMine(Map[i][ii-1])+DMine(Map[i][ii+1])
                            else:
                                MineN =DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])

                    elif i == height-1 :
                        if ii == 0:
                            MineN =DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii+1])
                        elif ii == width-1 :
                            MineN =DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])
                        else:
                            MineN =DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])
                   
                    else:
                        if ii == 0:
                            MineN =DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])
                        elif ii == width-1 :
                            MineN =DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])
                        else:
                            MineN =DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])
                    BlockObj = MineN
                tempMap[i*width+ii] = BlockObj

        doneMap = []
        doneLine = []
        base = 0
        for i in range(height):
            for ii in range(width):
                Bnum = base + ii
                #print Bnum
                doneLine.append(str(tempMap[Bnum]))
            base = (1+i)*width
            doneMap.append(doneLine)
            doneLine = []

        self.Map = doneMap
                
    ##Calculate numbers in hexagon-block######################
    def HexBlockReform(self):
        width = self.width
        height = self.height
        Map = self.orgMap
        tempMap = range(width*height)
        for i in range(height):
            for ii in range(width):
                BlockObj = Map[i][ii]
                MineN = 0
                if BlockObj == '0':
                    if i == 0 :
                        if ii == 0:
                            if height == 1:
                                MineN =DMine(Map[i][ii+1])
                            else:
                                MineN =DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])
                        elif ii == width-1 :
                            if ii%2 :
                                if height == 1:
                                    MineN =DMine(Map[i][ii-1])
                                else:
                                    MineN =DMine(Map[i][ii-1])+DMine(Map[i+1][ii])
                            else:
                                if height == 1:
                                    MineN =DMine(Map[i][ii-1])
                                else:
                                    MineN =DMine(Map[i][ii-1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])
                        else:
                            if ii%2 :
                                if height == 1:
                                    MineN =DMine(Map[i][ii-1])+DMine(Map[i][ii+1])
                                else:
                                    MineN =DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii])
                            else:
                                if height == 1:
                                    MineN =DMine(Map[i][ii-1])+DMine(Map[i][ii+1])
                                else:
                                    MineN =DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])

                    elif i == height-1 :
                        if ii == 0:
                            MineN =DMine(Map[i-1][ii])+DMine(Map[i][ii+1])
                        elif ii == width-1 :
                            if ii%2 :
                                MineN =DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])
                            else:
                                MineN =DMine(Map[i-1][ii])+DMine(Map[i][ii-1])
                        else:
                            if ii%2 :
                                MineN =DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])
                            else:
                                MineN =DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])
                   
                    else:
                        if ii == 0:
                            MineN =DMine(Map[i-1][ii])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])
                        elif ii == width-1 :
                            if ii%2 :
                                MineN =DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i+1][ii])
                            else:
                                MineN =DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])
                        else:
                            if ii%2 :
                                MineN =DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii])
                            else:
                                MineN =DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])
                    BlockObj = MineN
                tempMap[i*width+ii] = BlockObj

        doneMap = []
        doneLine = []
        base = 0
        for i in range(height):
            for ii in range(width):
                Bnum = base + ii
                #print Bnum
                doneLine.append(str(tempMap[Bnum]))
            base = (1+i)*width
            doneMap.append(doneLine)
            doneLine = []

        self.Map = doneMap
        
    ##Calculate numbers in triangle-block######################
    def TriBlockReform(self):
        width = self.width
        height = self.height
        Map = self.orgMap
        tempMap = range(width*height)
        for i in range(height):
            for ii in range(width):
                BlockObj = Map[i][ii]
                MineN = 0
                if BlockObj == '0':
                    if i == 0 :
                        if ii == 0:
                            if height == 1:
                                MineN =DMine(Map[i][ii+1])
                            elif height == 2:
                                MineN =DMine(Map[i][ii+1])+DMine(Map[i+1][ii])
                            elif height == 3:
                                MineN =DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+2][ii])
                            else:
                                MineN =DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+2][ii])+DMine(Map[i+3][ii])
                        elif ii == width-1 :
                            if height == 1:
                                MineN =DMine(Map[i][ii-1])
                            elif height == 2:
                                MineN =DMine(Map[i][ii-1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])
                            elif height == 3:
                                MineN =DMine(Map[i][ii-1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+2][ii-1])+DMine(Map[i+2][ii])
                            else:
                                MineN =DMine(Map[i][ii-1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+2][ii-1])+DMine(Map[i+2][ii])+DMine(Map[i+3][ii])
                        else:
                            if height == 1:
                                MineN =DMine(Map[i][ii-1])+DMine(Map[i][ii+1])
                            elif height == 2:
                                MineN =DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])
                            elif height == 3:
                                MineN =DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+2][ii-1])+DMine(Map[i+2][ii])
                            else:
                                MineN =DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+2][ii-1])+DMine(Map[i+2][ii])+DMine(Map[i+3][ii])

                    elif i == height-1 :
                        if i%4 == 0 :
                            if ii == 0:
                                MineN =DMine(Map[i-2][ii])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii+1])
                            elif ii == width-1 :
                                MineN =DMine(Map[i-2][ii-1])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])
                            else:
                                MineN =DMine(Map[i-2][ii-1])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])
                        elif i%4 == 1 :
                            if ii == 0:
                                if height == 2:
                                    MineN =DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii+1])
                                else:
                                    MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii])+DMine(Map[i-2][ii+1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii+1])
                            elif ii == width-1 :
                                if height == 2:
                                    MineN =DMine(Map[i-1][ii])+DMine(Map[i][ii-1])
                                else:
                                    MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])
                            else:
                                if height == 2:
                                    MineN =DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])
                                else:
                                    MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii])+DMine(Map[i-2][ii+1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])
                        elif i%4 == 2 :
                            if ii == 0:
                                MineN =DMine(Map[i-2][ii])+DMine(Map[i-2][ii+1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii+1])
                            elif ii == width-1 :
                                MineN =DMine(Map[i-2][ii])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])
                            else:
                                MineN =DMine(Map[i-2][ii])+DMine(Map[i-2][ii+1])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])
                        else:
                            if ii == 0:
                                MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii])+DMine(Map[i][ii+1])
                            elif ii == width-1 :
                                MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii-1])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])
                            else:
                                MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii-1])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])

                    elif i == 1 :
                        if ii == 0:
                            if height == 3:
                                MineN =DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])
                            else:
                                MineN =DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])+DMine(Map[i+2][ii])+DMine(Map[i+2][ii+1])
                        elif ii == width-1 :
                            if height == 3:
                                MineN =DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])
                            else:
                                MineN =DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+2][ii])
                        else:
                            if height == 3:
                                MineN =DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])
                            else:
                                MineN =DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])+DMine(Map[i+2][ii])+DMine(Map[i+2][ii+1])

                    elif i == height-2 :
                        if i%4 == 0 :
                            if ii == 0:
                                MineN =DMine(Map[i-2][ii])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii])
                            elif ii == width-1 :
                                MineN =DMine(Map[i-2][ii-1])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])
                            else:
                                MineN =DMine(Map[i-2][ii-1])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])
                        elif i%4 == 1 :
                            if ii == 0:
                                MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii])+DMine(Map[i-2][ii+1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])
                            elif ii == width-1 :
                                MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])
                            else:
                                MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii])+DMine(Map[i-2][ii+1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])
                        elif i%4 == 2 :
                            if ii == 0:
                                MineN =DMine(Map[i-2][ii])+DMine(Map[i-2][ii+1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])
                            elif ii == width-1 :
                                MineN =DMine(Map[i-2][ii])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i+1][ii])
                            else:
                                MineN =DMine(Map[i-2][ii])+DMine(Map[i-2][ii+1])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])
                        else:
                            if ii == 0:
                                MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])
                            elif ii == width-1 :
                                MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii-1])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])
                            else:
                                MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii-1])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])

                    elif i == height-3 :
                        if i%4 == 0 :
                            if ii == 0:
                                MineN =DMine(Map[i-2][ii])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+2][ii])
                            elif ii == width-1 :
                                MineN =DMine(Map[i-2][ii-1])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+2][ii-1])+DMine(Map[i+2][ii])
                            else:
                                MineN =DMine(Map[i-2][ii-1])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+2][ii-1])+DMine(Map[i+2][ii])
                        elif i%4 == 1 :
                            if ii == 0:
                                MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii])+DMine(Map[i-2][ii+1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])+DMine(Map[i+2][ii])+DMine(Map[i+2][ii+1])
                            elif ii == width-1 :
                                MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+2][ii])
                            else:
                                MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii])+DMine(Map[i-2][ii+1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])+DMine(Map[i+2][ii])+DMine(Map[i+2][ii+1])
                        elif i%4 == 2 :
                            if ii == 0:
                                MineN =DMine(Map[i-2][ii])+DMine(Map[i-2][ii+1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])+DMine(Map[i+2][ii])+DMine(Map[i+2][ii+1])
                            elif ii == width-1 :
                                MineN =DMine(Map[i-2][ii])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+2][ii])
                            else:
                                MineN =DMine(Map[i-2][ii])+DMine(Map[i-2][ii+1])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])+DMine(Map[i+2][ii])+DMine(Map[i+2][ii+1])
                        else:
                            if ii == 0:
                                MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])+DMine(Map[i+2][ii])
                            elif ii == width-1 :
                                MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii-1])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+2][ii-1])+DMine(Map[i+2][ii])
                            else:
                                MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii-1])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])+DMine(Map[i+2][ii-1])+DMine(Map[i+2][ii])

                    else:
                        if i%4 == 0 :
                            if ii == 0:
                                MineN =DMine(Map[i-2][ii])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+2][ii])+DMine(Map[i+3][ii])
                            elif ii == width-1 :
                                MineN =DMine(Map[i-2][ii-1])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+2][ii-1])+DMine(Map[i+2][ii])+DMine(Map[i+3][ii])
                            else:
                                MineN =DMine(Map[i-2][ii-1])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+2][ii-1])+DMine(Map[i+2][ii])+DMine(Map[i+3][ii])
                        elif i%4 == 1 :
                            if ii == 0:
                                MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii])+DMine(Map[i-2][ii+1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])+DMine(Map[i+2][ii])+DMine(Map[i+2][ii+1])
                            elif ii == width-1 :
                                MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+2][ii])
                            else:
                                MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii])+DMine(Map[i-2][ii+1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])+DMine(Map[i+2][ii])+DMine(Map[i+2][ii+1])
                        elif i%4 == 2 :
                            if ii == 0:
                                MineN =DMine(Map[i-2][ii])+DMine(Map[i-2][ii+1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])+DMine(Map[i+2][ii])+DMine(Map[i+2][ii+1])+DMine(Map[i+3][ii])
                            elif ii == width-1 :
                                MineN =DMine(Map[i-2][ii])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+2][ii])+DMine(Map[i+3][ii])
                            else:
                                MineN =DMine(Map[i-2][ii])+DMine(Map[i-2][ii+1])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i-1][ii+1])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])+DMine(Map[i+2][ii])+DMine(Map[i+2][ii+1])+DMine(Map[i+3][ii])
                        else:
                            if ii == 0:
                                MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])+DMine(Map[i+2][ii])
                            elif ii == width-1 :
                                MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii-1])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+2][ii-1])+DMine(Map[i+2][ii])
                            else:
                                MineN =DMine(Map[i-3][ii])+DMine(Map[i-2][ii-1])+DMine(Map[i-2][ii])+DMine(Map[i-1][ii-1])+DMine(Map[i-1][ii])+DMine(Map[i][ii-1])+DMine(Map[i][ii+1])+DMine(Map[i+1][ii-1])+DMine(Map[i+1][ii])+DMine(Map[i+1][ii+1])+DMine(Map[i+2][ii-1])+DMine(Map[i+2][ii])

                    BlockObj = MineN
                tempMap[i*width+ii] = BlockObj

        doneMap = []
        doneLine = []
        base = 0
        for i in range(height):
            for ii in range(width):
                Bnum = base + ii
                #print Bnum
                doneLine.append(str(tempMap[Bnum]))
            base = (1+i)*width
            doneMap.append(doneLine)
            doneLine = []

        self.Map = doneMap
    
##To decide whether the block is Mine##############################################
    
def DMine(blockobj):
    if blockobj == 'M' or blockobj =='D' :
        return 1
    else:
        return 0
    
#################################################
       
##Example#####################
def Example():
    Mwidth = 10
    Mheight = 10
    Mtype = 'tri' ###value could be :'box'/'hex'/'tri'
    Mine_number = 2
    Empty_number = 1
    Lock_number = 1
    
    mine = MineMapMake(Mwidth,Mheight,Mtype,Mine_number,Empty_number,Lock_number)
    
    UnFormed_Map = mine.get_orgMap()
    #print UnFormed_Map
    
    for i in range(Mheight):
        print UnFormed_Map[i]
    
    #print UnFormed_Map[2][2]
    #print UnFormed_Map[1][5]
        
    mine.mapForm()
    Formed_Map = mine.get_Map()
    print Formed_Map
    for i in range(Mheight):
        print Formed_Map[i]
        
#############################

if __name__ == "__main__":
    Example()
