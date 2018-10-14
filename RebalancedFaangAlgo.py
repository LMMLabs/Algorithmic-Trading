#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Quantopian Algorithm
"""
Created on Sat Oct 14 17:10:31 2018

@author: ljfarre
"""

'''
A simple algorithm showing how a rebalanced FAANG algorithm would have returned 
an excellent return over the past 4 years.
'''

def initialize(context):
    """
    Called once at the start of the algorithm.
    """   
    
    # Here are any algorithm 'constants' we'll be using
    context.target_leverage = 1.0
    
    # Here are the ETFs we want to trade along with the weights 
    # Ensure they add to 1.00
    context.etfs = {
        symbol('AMZN'): 0.2, # Daily Amazon shares
        symbol('AAPL'): 0.2, # Daily Apple shares
        symbol('FB'): 0.2, # Daily Facebook shares
        symbol('NFLXL'): 0.2, # Daily Netflix
        symbol('GOOG'): 0.2, # Daily Google shares

    }
    
    # Set commision model for Robinhood
    set_commission(commission.PerShare(cost=0.0, min_trade_cost=0.0))
 
    # Rebalance our portfolio to maintain target weights
    schedule_function(rebalance, date_rules.every_day(), time_rules.market_open(minutes = 35))


def rebalance(context, data):
    for stock, weight in context.etfs.items():
        order_target_percent(stock, weight*context.target_leverage)