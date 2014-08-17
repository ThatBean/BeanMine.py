##created for recreat/reset topscore savefile


import string
def main():
    preask = raw_input('''created for recreat/reset topscore savefile\nmake sure this file is the same folder with folder 'res'\nenter 'y' to start:\n''')
    if preask=='y':
        sfile = open('res/scosv','w')
        prefix = 'VACANT STILL/99:99:99/'
        scoreemp = [prefix+'RETRO EASY',prefix+'RETRO MEDI',prefix+'RETRO HARD',prefix+'  BOX EASY',prefix+'  BOX MEDI',prefix+'  BOX HARD',prefix+'  HEX EASY',prefix+'  HEX MEDI',prefix+'  HEX HARD',prefix+'  TRI EASY',prefix+'  TRI MEDI',prefix+'  TRI HARD']
        scoSTR = str(scoreemp)
        sfile.write(scoSTR)
        sfile.close()
        
        end = raw_input('''Done.\npress enter to exit.''')+"made by bean"
    else:
        end = raw_input('''recreat was expired.\npress enter to exit.''')+"made by bean"

main()
