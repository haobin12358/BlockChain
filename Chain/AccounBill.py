# -*- coding:utf-8 -*-

from datetime import datetime
from Block.Block import Block

class AccountBill(Block):
    def __init__(self, content, amount):
        t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = '{0}|{1}|{2}'.format(t, content, amount)
        return super(AccountBill, self).__init__(data)

    def get_amount(self):
        amount = 0
        if self.data:
            amount = int(self.data.split('|')[2])
        return amount

    def get_content(self):
        content = ''
        if self.data:
            content = self.data.split('|')[1]
        return content

    def __repr__(self):
        return 'Bill:{0}'.format(self.data)
