# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 16:13:08 2021

@author: Hemant Vijaykumar

Module      : Validate_Input
Objective   : To validate different values
"""
def validate_integer(prompt,mandatory=False,
                     err_msg="Entered Number Is Invalid",
                     lower_limit=None,
                     upper_limit=None):
    '''
    Function    : validate_integer
    Objective   : To make sure user enters valid
    integer number.

    Parameters
    ----------
    1. prompt :
        DESCRIPTION : This text should be displayed to
        the user for entering the number.
    2. mandatory : optional
        DESCRIPTION: If True, then user must enter valid
        integer. The default is False.
    3. err_msg : optional
        DESCRIPTION: This is the message that should be
        displayed when invalid input is entered.
        The default is "Entered Number Is Invalid".
    4. lower_limit : optional
        DESCRIPTION: User entered number must be greater
        than or equal to lower limit.
        The default is None.
    5. upper_limit : optional
        DESCRIPTION: User entered number must be less than
        or equal to upper limit provided.
        The default is None.

    Returns
    -------
    None if mandatory is false. String if mandatory is true.

    '''
    while True:
        try:
            num=int(input(prompt))
            if lower_limit != None:
                if lower_limit>num:
                    print(err_msg)
                    continue
            if upper_limit != None:
                if upper_limit<num:
                    print(err_msg)
                    continue
            break
        except:
            print(err_msg)
    return num
def validate_float(prompt,mandatory=False,
                     err_msg="Entered Number Is Invalid",
                     lower_limit=None,
                     upper_limit=None):
    '''
    
    Function   
    --------
    validate_float
    
    Objective  
    ---------
    To make sure user enters validinteger number.
    
    Parameters
    ----------
    1. prompt :
        DESCRIPTION : This text should be displayed to
        the user for entering the number.
    2. mandatory : optional
        DESCRIPTION: If True, then user must enter valid
        float. The default is False.
    3. err_msg : optional
        DESCRIPTION: This is the message that should be
        displayed when invalid input is entered.
        The default is "Entered Number Is Invalid".
    4. lower_limit : optional
        DESCRIPTION: User entered number must be greater
        than or equal to lower limit.
        The default is None.
    5. upper_limit : optional
        DESCRIPTION: User entered number must be less than
        or equal to upper limit provided.
        The default is None.

    Returns
    -------
    None if mandatory is false. String if mandatory is true.   
    '''
    while True:
        try:
            num=float(input(prompt))
            if lower_limit != None:
                if lower_limit>num:
                    print(err_msg)
                    continue
            if upper_limit != None:
                if upper_limit<num:
                    print(err_msg)
                    continue
            break
        except:
            print(err_msg)
    return num