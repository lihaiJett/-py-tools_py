import sys  
import time  
      
for i in range(10000):   
    percent = 1.0 * i / 10000 * 100
    print('complete percent:%10.8s%s'%(str(percent),'%'),end='\r')        
    time.sleep(0.1)  
