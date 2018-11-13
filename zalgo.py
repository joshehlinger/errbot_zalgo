from errbot import BotPlugin, botcmd, re_botcmd
import re, random, math


CHARS = \
    [
        ['\u030d','\u030e','\u0304','\u0305','\u033f','\u0311','\u0306','\u0310','\u0352','\u0357','\u0351','\u0307',
        '\u0308','\u030a','\u0342','\u0343','\u0344','\u034a','\u034b','\u034c','\u0303','\u0302','\u030c','\u0350',
        '\u0300','\u0301','\u030b','\u030f','\u0312','\u0313','\u0314','\u033d','\u0309','\u0363','\u0364','\u0365',
        '\u0366','\u0367','\u0368','\u0369','\u036a','\u036b','\u036c','\u036d','\u036e','\u036f','\u033e','\u035b',
        '\u0346','\u031a'],
        ['\u0316','\u0317','\u0318','\u0319','\u031c','\u031d','\u031e','\u031f','\u0320','\u0324','\u0325','\u0326',
        '\u0329','\u032a','\u032b','\u032c','\u032d','\u032e','\u032f','\u0330','\u0331','\u0332','\u0333','\u0339',
        '\u033a','\u033b','\u033c','\u0345','\u0347','\u0348','\u0349','\u034d','\u034e','\u0353','\u0354','\u0355',
        '\u0356','\u0359','\u035a','\u0323'],
        ['\u0315','\u031b','\u0340','\u0341','\u0358','\u0321','\u0322','\u0327','\u0328','\u0334','\u0335','\u0336',
        '\u034f','\u035c','\u035d','\u035e','\u035f','\u0360','\u0362','\u0338','\u0337','\u0361','\u0489']
    ]


class Zalgo(BotPlugin):

    def randomify(self, length):
        if length == 1:
            return 0
        if length:
            return math.floor(random.random() * length + 1) - 1
        else:
            return random.random()

    def generate(self, string):
        string_array = list(string)
        output_array = list()
        for char in string_array:
            if char == ' ':
                output_array.append(char)
                continue
            i = 0
            l = self.randomify(16)
            while i < l:
                rand = self.randomify(3)
                char += CHARS[rand][self.randomify(len(CHARS[rand]))]
                i += 1
            output_array.append(char)
        output = ''.join(output_array)
        return output

    @re_botcmd(pattern=r"(^|.?)lovecraft|cthulhu(.?|$)", prefixed=False, flags=re.IGNORECASE)
    def cthulhu_chant(self, msg, args):
        """
        Cthulhu F'thagn
        """
        yield self.generate("ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn")

    @botcmd()
    def zalgo(self, msg, args):
        """
        HE COMES
        """
        yield self.generate(args)