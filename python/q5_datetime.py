# Hint:  use Google to find python function

####a) 

date_start = '01-02-2013'  
date_stop = '07-28-2015'   

import datetime
start = datetime.datetime.strptime(date_start, '%m-%d-%Y')
end  = datetime.datetime.strptime(date_stop, '%m-%d-%Y')
delta = end - start
print delta.days


####b) 
date_start = '12312013'  
date_stop = '05282015'    

import datetime
start = datetime.datetime.strptime(date_start, '%m%d%Y')
end  = datetime.datetime.strptime(date_stop, '%m%d%Y')
delta = end - start
print delta.days


####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'      

import datetime
start = datetime.datetime.strptime(date_start, '%d-%b-%Y')
end  = datetime.datetime.strptime(date_stop, '%d-%b-%Y')
delta = end - start
print delta.days