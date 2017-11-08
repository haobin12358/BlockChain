# -*- coding:utf-8 -*-

from collections import OrderedDict
from Chain.BlockChain import BlockChain

class AccountBook(BlockChain):
    def __init__(self):
        self.head = None
        self.blocks = OrderedDict()

    def add_block(self, new_bill):
        new_bill.mine()
        super(AccountBook,self).add_block(new_bill)

    def balance(self):
        balance = 0
        if self.blocks:
            for k,v in self.blocks.items():
                balance += v['block'].get_amount()
        return balance

    def __repr__(self):
        num_existing_blocks = len(self.blocks)
        return 'AccountBook {0} Bills, Head:{1}'.format(
            num_existing_blocks,
            self.head.identifier if self.head else None
        )
