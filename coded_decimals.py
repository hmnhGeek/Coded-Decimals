#!/usr/bin/env/python

class coded_decimals(object):

    def __init__(self, decimal_number):
        self.d = decimal_number

    def XOR(self, dig1, dig2):

        if (dig1 == 1 and dig2 == 0) or (dig2 == 1 and dig1 == 0):
            return 1
        else:
            return 0

    def make_four_bit(self, binary_digit):
        b = binary_digit
        b = b[2::]

        #reverse the binary string.
        b = b[-1:-len(b)-1:-1]

        while len(b) != 4:
            b+='0'

        return b[-1:-len(b)-1:-1]

    def BCD(self):
        BCDString = ''
        decimal_string = str(self.d)

        for digit in decimal_string:
            # now make it 4 bit
            BCDString += self.make_four_bit(bin(int(digit)))

        return BCDString

    def XS3(self):
        XS3String = ''
        decimal_string = str(self.d)
        XS3decimal_string = ''

        for digit in decimal_string:
            digit = int(digit)+3
            XS3String += self.make_four_bit(bin(digit))
        
        return XS3String

    def GRAY(self):

        GRAYString = ''

        #get the binary equivalent of the decimal number.
        binary_eqv = bin(self.d)
        binary_eqv = binary_eqv[2::] # to remove '0b'

        i = 0
        while i != len(binary_eqv)-1:
            first_digit = binary_eqv[i]
            second_digit = binary_eqv[i+1]

            GRAYString += str(self.XOR(int(first_digit), int(second_digit)))
            i+=1

        GrayList = [i for i in GRAYString]
        GrayList.insert(0, binary_eqv[0])

        GRAYString = ''.join(GrayList)

        return GRAYString
