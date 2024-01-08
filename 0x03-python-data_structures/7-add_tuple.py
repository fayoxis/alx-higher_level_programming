#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    ta_len = len(tuple_a)
    tb_len = len(tuple_b)
    new_tup = ()
    
    for i in range(2):
        val_a = tuple_a[i] if i < ta_len else 0
        val_b = tuple_b[i] if i < tb_len else 0
        
        if i == 0:
            new_tup = val_a + val_b
        else:
            new_tup = (new_tup, val_a + val_b)
    
    return new_tup
