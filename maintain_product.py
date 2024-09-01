# -*- coding: utf-8 -*-
"""
Created on Wed May  5 14:37:15 2021

@author: Hemant Vijaykumar
"""
import mysql_interface
import validate_input
def display_all_products():
    s = "select product_id,product_name,quantity_in_stock,rate from product;"
    status, err_msg, data=mysql_interface.execute_select(s)
    if status==True:
        print(data)
    else :
        print(err_msg)
def search_for_products():
    inp_id=validate_input.validate_integer("Enter Product ID:",True,"Enter Product ID>0",lower_limit=1)
    s='''select product_id, product_name, category_id, quantity_in_stock, rate from product
    where product_id = {};'''.format(inp_id)
    status, err_msg, data=mysql_interface.execute_select(s)
    if status==True:
        if len(data)>0:
            print(data)
        else:
            print("No product exists for product id =",inp_id)
    else:
        print(err_msg)
def input_inp_id():
    while True:
        global inp_id
        inp_id=validate_input.validate_integer("Enter Product ID:",True,"Enter Product ID>0",lower_limit=1)
        sel='''select {} from product where product_id={}'''.format(inp_id,inp_id)
        status, err_msg, data=mysql_interface.execute_select(sel)
        if status==True:
            if len(data)>0:
                print("Product ID already exists.")
            else:
                break       
def insert_products():
    input_inp_id()     
    inp_name=input("Enter Product Name:")
    inp_cat=validate_input.validate_integer("Enter Category ID:",True,"Enter Category ID>0",lower_limit=1)
    inp_qty=validate_input.validate_float("Enter Quantity:",True,"Enter Quantity>0",lower_limit=1)
    inp_rate=validate_input.validate_float("Enter Rate:",True)
    Ins1 = '''insert into product (product_id, product_name, category_id, quantity_in_stock, rate) values ({}, '{}', {}, {}, {});'''.format(inp_id, inp_name, inp_cat, inp_qty, inp_rate)
    lst = [Ins1]
    status, error_msg = mysql_interface.execute_iud(lst)
    if status == False:
        print(error_msg)
    else:
        print("Product successfully inserted.")
def update_product():
    inp_id=validate_input.validate_integer("Enter Product ID:",True,"Enter Product ID>0",lower_limit=1)
    inp_name=input("Enter Product Name:")
    inp_cat=validate_input.validate_integer("Enter Category ID:",True,"Enter Category ID>0",lower_limit=1)
    inp_qty=validate_input.validate_float("Enter Quantity:",True,"Enter Quantity>0",lower_limit=1,)
    inp_rate=validate_input.validate_float("Enter Rate:",True)
    upd = ''' update product set product_name='{}', category_id={}, quantity_in_stock={}, rate={} where product_id={};'''.format(inp_name, inp_cat, inp_qty, inp_rate, inp_id)
    lt=[upd]
    status, error_msg = mysql_interface.execute_iud(lt)
    if status == False:
        print(error_msg)
    else:
        print("Product successfully updated.")
def delete_product():
    inp_id=validate_input.validate_integer("Enter Product ID:",True,"Enter Product ID>0",lower_limit=1)
    delt=''' delete from product where product_id={};'''.format(inp_id)
    lit=[delt]
    status, error_msg = mysql_interface.execute_iud(lit)
    if status == False:
        print(error_msg)
    else:
        print("Product sucessfully removed.")