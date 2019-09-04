# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 16:13:06 2018

@author: sdksbe
"""
import swat
import os

# lab10 environment:
# cas_shared_default_srv --> lab10-viyac1.lab.local     
#                            CAS Server configured with it's own certificate signed by Nordic Labs
#                            This certificate is in the windows trust store
cas_shared_default_srv = "lab10-viyac1.lab.local"

# cas_shared_dev_srv     --> lab10-viyadev.lab.local    
#                            CS Server used the default Viya certificate
cas_shared_dev_srv     = "lab10-viyadev.lab.local"

#---------------- SELECT THE CAS SERVER ----------------------
selected_cas = cas_shared_default_srv
#-------------------------------------------------------------

if (selected_cas == cas_shared_dev_srv):
    os.environ['CAS_CLIENT_SSL_CA_LIST']=r"/opt/sasviyarepo/lab10/viya-certificates/vault-ca.crt"

# Connect to the cas server and get a CAS Session
conn = swat.CAS(selected_cas, 5570)

# Load CAS Table and display Info
print('titanic3 table ---------------------------------------------------')

titanic3 = conn.CASTable("TITANIC3", replace=True)
conn.upload_file(r'C:/dev/github/viya/python-labs/pylab03-CallViyaActions/titanic3.csv', casout=titanic3)

print(titanic3.table.columnInfo())

summaryResult = titanic3.simple.summary()
print(summaryResult.Summary[['Column','Min','Max','N','NMiss','Mean','Sum','Std','StdErr']])
print('------------------------------------------------------------------')
print()

# End CAS Session
print('END SESSION ------------------------------------------------------')

r=conn.session.endSession()
print(r)

print('------------------------------------------------------------------')