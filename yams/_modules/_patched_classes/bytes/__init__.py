# -*- coding: utf-8 -*-
class bytes(bytes):
    @staticmethod
    def pretty_print(arg):
        '''
        equivalent of .decode but that doesn't matter
        '''
        print(str(arg)[2:-1], end='')

    def __str__(self):
        return super().__str__()[2:-1]
    __repr__ = __str__

    def __iter__(self):
        for _ord in super().__iter__():
            result = bytes(chr(_ord), 'utf-8')
            yield result
