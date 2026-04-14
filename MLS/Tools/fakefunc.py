import os

import debug
from HEPRun import HepTool, DataPoint
import zslha
"""
Dummy class just for generating parameter cards

"""

import math
class NewTool(HepTool):
    """ overload the init to initialise the DM limit calculator, but name and settings are already given in HepTool """
    def __init__(self, name, settings,global_settings=None):
        HepTool.__init__(self, name, settings,global_settings)
        
        
    def run(self, spc_file, temp_dir, log,data_point):
        m0=0
        m12=0
        #print('Run fake tool')
        if data_point.spc is None:
            #print("No data point, wtf?")
            data_point.spc=zslha.read(spc_file)
            m0=float(data_point.spc.Value("MINPAR",[1]))
            m12=float(data_point.spc.Value("MINPAR",[2]))
            #print(mchi)
        else:
            vars = data_point.get_var_dict()
            m0=vars['m0']
            m12=vars['m12']
        
        #res = math.exp(-((msmu-800.0)**2+(mchi-750.0)**2)/100000.0)
        # Log of gaussian likelihood around a given point ...
        res = -((m0-800.0)**2+(m12-750.0)**2)/100000.0
        blocks={'1':res}
        blockcomments={'1':' Dummy result'}
        data_point.spc.blocks['DUMMY']=blocks
        data_point.spc.blockcomments['DUMMY']=blockcomments
        with open(spc_file,'a') as OF:
            OF.write('BLOCK DUMMY #\n')
            for myentry in blocks:
                OF.write(' %s   %.8E  #  %s\n' %(myentry,blocks[myentry],blockcomments[myentry]))
        return
