#!/usr/bin/python
import MySQLdb
import numpy as np

hostname = 'localhost'
username = 'root'
password = '12345678'
database = 'COMPLETE'

# Simple routine to run a query on a database and print the results:
def doQuery1v( conn, st, patient,sen) :
    cur = conn.cursor()

    cur.execute( "SELECT wave FROM waves_v1.samples WHERE file=\'"+patient+"\' AND sensor=\'"+sen+"\' AND state=\'"+st+"\';" )

    #print cur.fetchall()
    datos=[]
    res=cur.fetchall()
    cant= len(res)
    for wave in res:
    	#print"asdsfsd"
    	#print "la",wave
    	a=np.fromstring(wave[0][1:-1], dtype=float, sep=', ')
    	#print a
    	datos.append([a])
    	#print "**************************************\n"
    #datos=np.array(datos)
    #
    #print datos
    #print"-------------------------------!!"
    return datos, cant

patients = ['SC4001E0','SC4051E0','SC4101E0','SC4151E0']
sensor = ["EEGPzOz", "EEGFpzCz"];
state = ["W", "1", "2", "3", "4", "R", "M"];


def get_data_1v():
	myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
	k=1
	j=1
	data=[]
	labels=[]
	for i in state:
		d,c=doQuery1v( myConnection,i,patients[j],sensor[k] )
		data+=d
		labels+=c*[i]
		#print i,d,c

	data=np.array(data)
	print data.shape
	print labels	

	myConnection.close()
	return data, labels


def doQuerynv( conn, st, patient) : #sen is number of variables in order:
 # EEGFpzCz,EEGPzOz,EOGhorizontal,Resporonasal,EMGsubmental,Temprectal,Eventmarker

    cur = conn.cursor()

    cur.execute("SELECT wave FROM waves_v1.samples WHERE file=\'"+patient+"\' AND state=\'"+st+"\' order by pos_begin, pos_end ASC;" )

    #print cur.fetchall()
    datos=[]
    res=cur.fetchall()
    cant= len(res)
    print cant,cant%7
    cont=0
    for wave in res:
    	#print"asdsfsd" order by pos_begin, pos_end ASC
    	#print "la",wave
    	if cont%7==0:
    		l=[]
    		a=np.fromstring(wave[0][1:-1], dtype=float, sep=', ')
    		l.append(a)
    	else:
    		a=np.fromstring(wave[0][1:-1], dtype=float, sep=', ')
    		l.append(a)
    		if cont%7==6:
    			datos.append(l)
    	#print a
    	#print datos 
    	cont=cont+1
    	#print "**************************************\n"
    #datos=np.array(datos)
    #
    #print datos
    #print"-------------------------------!!"
    return datos, cant

def get_data_nv(n):
	myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
	k=1
	j=1
	data=[]
	labels=[]
	for i in state:
		d,c=doQuerynv( myConnection,i,patients[j])
		data+=d
		labels+=(c/7)*[i]
		#print i,d,c

	data=np.array(data)
	print data.shape
	#print labels
	print "after ddc"

	myConnection.close()
	for i in range(n,7):
		data=np.delete(data, n, 1) 
	print data.shape
	#print labels	

	return data, labels	

def get_data_pp(patient,nv): # Funcion para obtener en orden de tiempo 
    conn = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
    data=[]
    labels=[]

    cur = conn.cursor()

    cur.execute("SELECT wave FROM COMPLETE.samples WHERE  file=\""+patient +"\" order by CAST(pos_begin AS UNSIGNED)")

    #print cur.fetchall()
    ts=4
    datos=[]
    res=cur.fetchall()
    cant= len(res)
    print cant,cant%ts
    cont=0
    for wave in res:
        #print"asdsfsd" order by pos_begin, pos_end ASC
        #print "la",wave
        if cont%ts==0:
            l=[]
            a=np.fromstring(wave[0][1:-1], dtype=float, sep=', ')
            l.append(a)
        else:
            a=np.fromstring(wave[0][1:-1], dtype=float, sep=', ')
            l.append(a)
            if cont%ts==ts-1:
                datos.append(l)
        #print a
        #print datos 
        cont=cont+1
    data=np.array(datos)
    cur.execute("SELECT state FROM COMPLETE.samples WHERE sensor=\"EEGPzOz\" and file=\""+patient +"\" order by CAST(pos_begin AS UNSIGNED)")
    res=cur.fetchall()
    ll=[state[0] for state in res]
    conn.close()
    print "before deleting",data.shape
    for i in range(nv,4):
        data=np.delete(data, nv, 1) 
    print data.shape
    #print data
    print data.shape
    return data, ll


# el cero es el 1


#get_data_1v()

# print "Using pymysql"
# import pymysql
# myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
# doQuery( myConnection )
# myConnection.close()

# print "Using mysql.connector"
# import mysql.connector
# myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
# doQuery( myConnection )
# myConnection.close()