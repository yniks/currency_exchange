from datetime import datetime
from sys import stderr
'''     
        Prints debug message  as : `{date} :: message`
        This module exports a singlton class (i.e only a single instance is ever created).

        This mdule exports a class which creates a callble function, which can be called to 
        print debug message to console based on the verbosoty value
        So, point to remember

        Message will be printed
        1. if the level of the message (default 1) is smaller than verbosoty of the object
        2. every inistationa of this class retuens the same isntance, BUT, the verbosoty can be increased by 
                instatiating this class with increased verbosity
        3. By default , this class prints to stderr 
'''

instance=None

class Debug:
        verbose=0
        def __new__(cls,verbosity=0):
            
            if (instance):
                instance.verbose=max(verbosity,instance.verbose)
                return instance
            else:
                return super(Debug,cls).__new__(cls)

        def __init__(self,verbosity=0):
                global instance
                self.verbose=verbosity
                instance=self

        def __call__(self,message,level=1):
                if(self.verbose>=level):
                        print(datetime.now(),"::",message,file=stderr)

