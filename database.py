#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 02:27:35 2019

@author: lucky
"""

import sqlite3
from sqlite3 import Error

#Creating the database.
def sql_connection():
    try:
        connection = sqlite3.connect("database.db")
        print("Connection is established: Database is created in memory")
        return connection
    except Error:
        print(Error)

        
#Creating the tables for the database..        

#Starting of the main()
def insert_db(connection,entities,table_name):
    curso=connection.cursor()
    if(table_name=="USER"):
        curso.execute("INSERT INTO User(username,email,mob_n,address,city,state,country) VALUES(?,?,?,?,?,?,?)",entities)
    if(table_name=="LOGIN"):
        curso.execute("INSERT INTO login(Username,Password) VALUES(?,?)",entities)
        
    connection.commit()
    
#calling the connection function 
connect=sql_connection()
cor=connect.cursor()
#this function will help us in doing all the work

#to access the login table in the form of list.
def login_table( ):
    table_ob=cor.execute("SELECT * FROM login")
    table_list=table_ob.fetchall()
    return table_list

def job_categories_table():
    table_ob=cor.execute("SELECT * FROM job_categories")
    table_list=table_ob.fetchall()
    return table_list

def Applicant_table():
    table_ob=cor.execute("SELECT * FROM Applicant")
    table_list=table_ob.fetchall()
    return table_list

#to update tables
def update_job_catgories_table(job_name,vacant):
    sql_update_query = """Update job_categories set vacant = ? where job_name = ?"""
    data = ( vacant,job_name)
    cor.execute(sql_update_query, data)
    connect.commit()
    
def update_Applicant_table(username,email,r_n,value):
    if(r_n==1):
        sql_update_query = """Update Applicant set round_1 = ? where username = ? AND email = ? """
    if(r_n==2):
        sql_update_query = """Update Applicant set final_round = ? where username = ? AND email = ? """
    
    data = (value,username,email)
    cor.execute(sql_update_query, data)
    connect.commit()
   
def insert_shortlisted_candidate(name,email,job_name):
    sql_update_query = """INSERT INTO shortlisted_candidate(name,email,job_name) VALUES(?,?,?)"""
    data = (name,email,job_name)
    cor.execute(sql_update_query, data)
    connect.commit()
    
def insert_final_candidate(name,email,job_name):
    sql_update_query = """INSERT INTO Interview_results(username,email,job_name) VALUES(?,?,?)"""
    data = (name,email,job_name)
    cor.execute(sql_update_query, data)
    connect.commit()    
    
def database():
    print("WE ARE POSSIBLE")
    #entities=("lucky","lucky.agarwl96@gmail.com","9634013823","Purani Mandi Gate","Nanital","Uttarakhand","India")
    entities=("Lucky agarwal","34501829")
   
    #Creating table
    #connect.execute("CREATE TABLE User(username text NOT NULL,email text NOT NULL PRIMARY KEY,\
                                       #mob_n text,address text,city text,state text,country text)")

    #connect.execute("CREATE TABLE login(Username text NOT NULL, Password text NOT NULL)")
    insert_db(connect,entities,"USER")
    insert_db(connect,entities,"LOGIN")
    #our database script is working pretty fine ...
    connect.close()