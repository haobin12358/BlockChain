# -*- coding:utf-8 -*-
from Block.Block import Block
from Chain.BlockChain import BlockChain
from Chain.AccounBill import AccountBill

if __name__ == '__main__':
    block = Block("hello world")
    #block.mine()

    chain = BlockChain()
    accountBill = AccountBill('测试',100)
    print accountBill


    for i in range(6):
        new_block = Block(i)
        #new_block.mine()
        #chain.add_block(new_block)
    #print chain

    #print block.__repr__()
    #print block.hash(1)
    #print block.hash_is_valid(block.hash(1))

