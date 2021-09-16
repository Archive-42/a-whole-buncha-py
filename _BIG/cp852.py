""" Python Character Mapping Codec generated from 'VENDORS/MICSFT/PC/CP852.TXT' with gencodec.py.

"""  # "

import codecs

### Codec APIs


class Codec(codecs.Codec):
    def encode(self, input, errors="strict"):
        return codecs.charmap_encode(input, errors, encoding_map)

    def decode(self, input, errors="strict"):
        return codecs.charmap_decode(input, errors, decoding_table)


class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, encoding_map)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):
    def decode(self, input, final=False):
        return codecs.charmap_decode(input, self.errors, decoding_table)[0]


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


### encodings module API


def getregentry():
    return codecs.CodecInfo(
        name="cp852",
        encode=Codec().encode,
        decode=Codec().decode,
        incrementalencoder=IncrementalEncoder,
        incrementaldecoder=IncrementalDecoder,
        streamreader=StreamReader,
        streamwriter=StreamWriter,
    )


### Decoding Map

decoding_map = codecs.make_identity_dict(range(256))
decoding_map.update(
    {
        0x0080: 0x00C7,  #  LATIN CAPITAL LETTER C WITH CEDILLA
        0x0081: 0x00FC,  #  LATIN SMALL LETTER U WITH DIAERESIS
        0x0082: 0x00E9,  #  LATIN SMALL LETTER E WITH ACUTE
        0x0083: 0x00E2,  #  LATIN SMALL LETTER A WITH CIRCUMFLEX
        0x0084: 0x00E4,  #  LATIN SMALL LETTER A WITH DIAERESIS
        0x0085: 0x016F,  #  LATIN SMALL LETTER U WITH RING ABOVE
        0x0086: 0x0107,  #  LATIN SMALL LETTER C WITH ACUTE
        0x0087: 0x00E7,  #  LATIN SMALL LETTER C WITH CEDILLA
        0x0088: 0x0142,  #  LATIN SMALL LETTER L WITH STROKE
        0x0089: 0x00EB,  #  LATIN SMALL LETTER E WITH DIAERESIS
        0x008A: 0x0150,  #  LATIN CAPITAL LETTER O WITH DOUBLE ACUTE
        0x008B: 0x0151,  #  LATIN SMALL LETTER O WITH DOUBLE ACUTE
        0x008C: 0x00EE,  #  LATIN SMALL LETTER I WITH CIRCUMFLEX
        0x008D: 0x0179,  #  LATIN CAPITAL LETTER Z WITH ACUTE
        0x008E: 0x00C4,  #  LATIN CAPITAL LETTER A WITH DIAERESIS
        0x008F: 0x0106,  #  LATIN CAPITAL LETTER C WITH ACUTE
        0x0090: 0x00C9,  #  LATIN CAPITAL LETTER E WITH ACUTE
        0x0091: 0x0139,  #  LATIN CAPITAL LETTER L WITH ACUTE
        0x0092: 0x013A,  #  LATIN SMALL LETTER L WITH ACUTE
        0x0093: 0x00F4,  #  LATIN SMALL LETTER O WITH CIRCUMFLEX
        0x0094: 0x00F6,  #  LATIN SMALL LETTER O WITH DIAERESIS
        0x0095: 0x013D,  #  LATIN CAPITAL LETTER L WITH CARON
        0x0096: 0x013E,  #  LATIN SMALL LETTER L WITH CARON
        0x0097: 0x015A,  #  LATIN CAPITAL LETTER S WITH ACUTE
        0x0098: 0x015B,  #  LATIN SMALL LETTER S WITH ACUTE
        0x0099: 0x00D6,  #  LATIN CAPITAL LETTER O WITH DIAERESIS
        0x009A: 0x00DC,  #  LATIN CAPITAL LETTER U WITH DIAERESIS
        0x009B: 0x0164,  #  LATIN CAPITAL LETTER T WITH CARON
        0x009C: 0x0165,  #  LATIN SMALL LETTER T WITH CARON
        0x009D: 0x0141,  #  LATIN CAPITAL LETTER L WITH STROKE
        0x009E: 0x00D7,  #  MULTIPLICATION SIGN
        0x009F: 0x010D,  #  LATIN SMALL LETTER C WITH CARON
        0x00A0: 0x00E1,  #  LATIN SMALL LETTER A WITH ACUTE
        0x00A1: 0x00ED,  #  LATIN SMALL LETTER I WITH ACUTE
        0x00A2: 0x00F3,  #  LATIN SMALL LETTER O WITH ACUTE
        0x00A3: 0x00FA,  #  LATIN SMALL LETTER U WITH ACUTE
        0x00A4: 0x0104,  #  LATIN CAPITAL LETTER A WITH OGONEK
        0x00A5: 0x0105,  #  LATIN SMALL LETTER A WITH OGONEK
        0x00A6: 0x017D,  #  LATIN CAPITAL LETTER Z WITH CARON
        0x00A7: 0x017E,  #  LATIN SMALL LETTER Z WITH CARON
        0x00A8: 0x0118,  #  LATIN CAPITAL LETTER E WITH OGONEK
        0x00A9: 0x0119,  #  LATIN SMALL LETTER E WITH OGONEK
        0x00AA: 0x00AC,  #  NOT SIGN
        0x00AB: 0x017A,  #  LATIN SMALL LETTER Z WITH ACUTE
        0x00AC: 0x010C,  #  LATIN CAPITAL LETTER C WITH CARON
        0x00AD: 0x015F,  #  LATIN SMALL LETTER S WITH CEDILLA
        0x00AE: 0x00AB,  #  LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
        0x00AF: 0x00BB,  #  RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
        0x00B0: 0x2591,  #  LIGHT SHADE
        0x00B1: 0x2592,  #  MEDIUM SHADE
        0x00B2: 0x2593,  #  DARK SHADE
        0x00B3: 0x2502,  #  BOX DRAWINGS LIGHT VERTICAL
        0x00B4: 0x2524,  #  BOX DRAWINGS LIGHT VERTICAL AND LEFT
        0x00B5: 0x00C1,  #  LATIN CAPITAL LETTER A WITH ACUTE
        0x00B6: 0x00C2,  #  LATIN CAPITAL LETTER A WITH CIRCUMFLEX
        0x00B7: 0x011A,  #  LATIN CAPITAL LETTER E WITH CARON
        0x00B8: 0x015E,  #  LATIN CAPITAL LETTER S WITH CEDILLA
        0x00B9: 0x2563,  #  BOX DRAWINGS DOUBLE VERTICAL AND LEFT
        0x00BA: 0x2551,  #  BOX DRAWINGS DOUBLE VERTICAL
        0x00BB: 0x2557,  #  BOX DRAWINGS DOUBLE DOWN AND LEFT
        0x00BC: 0x255D,  #  BOX DRAWINGS DOUBLE UP AND LEFT
        0x00BD: 0x017B,  #  LATIN CAPITAL LETTER Z WITH DOT ABOVE
        0x00BE: 0x017C,  #  LATIN SMALL LETTER Z WITH DOT ABOVE
        0x00BF: 0x2510,  #  BOX DRAWINGS LIGHT DOWN AND LEFT
        0x00C0: 0x2514,  #  BOX DRAWINGS LIGHT UP AND RIGHT
        0x00C1: 0x2534,  #  BOX DRAWINGS LIGHT UP AND HORIZONTAL
        0x00C2: 0x252C,  #  BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
        0x00C3: 0x251C,  #  BOX DRAWINGS LIGHT VERTICAL AND RIGHT
        0x00C4: 0x2500,  #  BOX DRAWINGS LIGHT HORIZONTAL
        0x00C5: 0x253C,  #  BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
        0x00C6: 0x0102,  #  LATIN CAPITAL LETTER A WITH BREVE
        0x00C7: 0x0103,  #  LATIN SMALL LETTER A WITH BREVE
        0x00C8: 0x255A,  #  BOX DRAWINGS DOUBLE UP AND RIGHT
        0x00C9: 0x2554,  #  BOX DRAWINGS DOUBLE DOWN AND RIGHT
        0x00CA: 0x2569,  #  BOX DRAWINGS DOUBLE UP AND HORIZONTAL
        0x00CB: 0x2566,  #  BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
        0x00CC: 0x2560,  #  BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
        0x00CD: 0x2550,  #  BOX DRAWINGS DOUBLE HORIZONTAL
        0x00CE: 0x256C,  #  BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
        0x00CF: 0x00A4,  #  CURRENCY SIGN
        0x00D0: 0x0111,  #  LATIN SMALL LETTER D WITH STROKE
        0x00D1: 0x0110,  #  LATIN CAPITAL LETTER D WITH STROKE
        0x00D2: 0x010E,  #  LATIN CAPITAL LETTER D WITH CARON
        0x00D3: 0x00CB,  #  LATIN CAPITAL LETTER E WITH DIAERESIS
        0x00D4: 0x010F,  #  LATIN SMALL LETTER D WITH CARON
        0x00D5: 0x0147,  #  LATIN CAPITAL LETTER N WITH CARON
        0x00D6: 0x00CD,  #  LATIN CAPITAL LETTER I WITH ACUTE
        0x00D7: 0x00CE,  #  LATIN CAPITAL LETTER I WITH CIRCUMFLEX
        0x00D8: 0x011B,  #  LATIN SMALL LETTER E WITH CARON
        0x00D9: 0x2518,  #  BOX DRAWINGS LIGHT UP AND LEFT
        0x00DA: 0x250C,  #  BOX DRAWINGS LIGHT DOWN AND RIGHT
        0x00DB: 0x2588,  #  FULL BLOCK
        0x00DC: 0x2584,  #  LOWER HALF BLOCK
        0x00DD: 0x0162,  #  LATIN CAPITAL LETTER T WITH CEDILLA
        0x00DE: 0x016E,  #  LATIN CAPITAL LETTER U WITH RING ABOVE
        0x00DF: 0x2580,  #  UPPER HALF BLOCK
        0x00E0: 0x00D3,  #  LATIN CAPITAL LETTER O WITH ACUTE
        0x00E1: 0x00DF,  #  LATIN SMALL LETTER SHARP S
        0x00E2: 0x00D4,  #  LATIN CAPITAL LETTER O WITH CIRCUMFLEX
        0x00E3: 0x0143,  #  LATIN CAPITAL LETTER N WITH ACUTE
        0x00E4: 0x0144,  #  LATIN SMALL LETTER N WITH ACUTE
        0x00E5: 0x0148,  #  LATIN SMALL LETTER N WITH CARON
        0x00E6: 0x0160,  #  LATIN CAPITAL LETTER S WITH CARON
        0x00E7: 0x0161,  #  LATIN SMALL LETTER S WITH CARON
        0x00E8: 0x0154,  #  LATIN CAPITAL LETTER R WITH ACUTE
        0x00E9: 0x00DA,  #  LATIN CAPITAL LETTER U WITH ACUTE
        0x00EA: 0x0155,  #  LATIN SMALL LETTER R WITH ACUTE
        0x00EB: 0x0170,  #  LATIN CAPITAL LETTER U WITH DOUBLE ACUTE
        0x00EC: 0x00FD,  #  LATIN SMALL LETTER Y WITH ACUTE
        0x00ED: 0x00DD,  #  LATIN CAPITAL LETTER Y WITH ACUTE
        0x00EE: 0x0163,  #  LATIN SMALL LETTER T WITH CEDILLA
        0x00EF: 0x00B4,  #  ACUTE ACCENT
        0x00F0: 0x00AD,  #  SOFT HYPHEN
        0x00F1: 0x02DD,  #  DOUBLE ACUTE ACCENT
        0x00F2: 0x02DB,  #  OGONEK
        0x00F3: 0x02C7,  #  CARON
        0x00F4: 0x02D8,  #  BREVE
        0x00F5: 0x00A7,  #  SECTION SIGN
        0x00F6: 0x00F7,  #  DIVISION SIGN
        0x00F7: 0x00B8,  #  CEDILLA
        0x00F8: 0x00B0,  #  DEGREE SIGN
        0x00F9: 0x00A8,  #  DIAERESIS
        0x00FA: 0x02D9,  #  DOT ABOVE
        0x00FB: 0x0171,  #  LATIN SMALL LETTER U WITH DOUBLE ACUTE
        0x00FC: 0x0158,  #  LATIN CAPITAL LETTER R WITH CARON
        0x00FD: 0x0159,  #  LATIN SMALL LETTER R WITH CARON
        0x00FE: 0x25A0,  #  BLACK SQUARE
        0x00FF: 0x00A0,  #  NO-BREAK SPACE
    }
)

### Decoding Table

decoding_table = (
    u"\x00"  #  0x0000 -> NULL
    u"\x01"  #  0x0001 -> START OF HEADING
    u"\x02"  #  0x0002 -> START OF TEXT
    u"\x03"  #  0x0003 -> END OF TEXT
    u"\x04"  #  0x0004 -> END OF TRANSMISSION
    u"\x05"  #  0x0005 -> ENQUIRY
    u"\x06"  #  0x0006 -> ACKNOWLEDGE
    u"\x07"  #  0x0007 -> BELL
    u"\x08"  #  0x0008 -> BACKSPACE
    u"\t"  #  0x0009 -> HORIZONTAL TABULATION
    u"\n"  #  0x000a -> LINE FEED
    u"\x0b"  #  0x000b -> VERTICAL TABULATION
    u"\x0c"  #  0x000c -> FORM FEED
    u"\r"  #  0x000d -> CARRIAGE RETURN
    u"\x0e"  #  0x000e -> SHIFT OUT
    u"\x0f"  #  0x000f -> SHIFT IN
    u"\x10"  #  0x0010 -> DATA LINK ESCAPE
    u"\x11"  #  0x0011 -> DEVICE CONTROL ONE
    u"\x12"  #  0x0012 -> DEVICE CONTROL TWO
    u"\x13"  #  0x0013 -> DEVICE CONTROL THREE
    u"\x14"  #  0x0014 -> DEVICE CONTROL FOUR
    u"\x15"  #  0x0015 -> NEGATIVE ACKNOWLEDGE
    u"\x16"  #  0x0016 -> SYNCHRONOUS IDLE
    u"\x17"  #  0x0017 -> END OF TRANSMISSION BLOCK
    u"\x18"  #  0x0018 -> CANCEL
    u"\x19"  #  0x0019 -> END OF MEDIUM
    u"\x1a"  #  0x001a -> SUBSTITUTE
    u"\x1b"  #  0x001b -> ESCAPE
    u"\x1c"  #  0x001c -> FILE SEPARATOR
    u"\x1d"  #  0x001d -> GROUP SEPARATOR
    u"\x1e"  #  0x001e -> RECORD SEPARATOR
    u"\x1f"  #  0x001f -> UNIT SEPARATOR
    u" "  #  0x0020 -> SPACE
    u"!"  #  0x0021 -> EXCLAMATION MARK
    u'"'  #  0x0022 -> QUOTATION MARK
    u"#"  #  0x0023 -> NUMBER SIGN
    u"$"  #  0x0024 -> DOLLAR SIGN
    u"%"  #  0x0025 -> PERCENT SIGN
    u"&"  #  0x0026 -> AMPERSAND
    u"'"  #  0x0027 -> APOSTROPHE
    u"("  #  0x0028 -> LEFT PARENTHESIS
    u")"  #  0x0029 -> RIGHT PARENTHESIS
    u"*"  #  0x002a -> ASTERISK
    u"+"  #  0x002b -> PLUS SIGN
    u","  #  0x002c -> COMMA
    u"-"  #  0x002d -> HYPHEN-MINUS
    u"."  #  0x002e -> FULL STOP
    u"/"  #  0x002f -> SOLIDUS
    u"0"  #  0x0030 -> DIGIT ZERO
    u"1"  #  0x0031 -> DIGIT ONE
    u"2"  #  0x0032 -> DIGIT TWO
    u"3"  #  0x0033 -> DIGIT THREE
    u"4"  #  0x0034 -> DIGIT FOUR
    u"5"  #  0x0035 -> DIGIT FIVE
    u"6"  #  0x0036 -> DIGIT SIX
    u"7"  #  0x0037 -> DIGIT SEVEN
    u"8"  #  0x0038 -> DIGIT EIGHT
    u"9"  #  0x0039 -> DIGIT NINE
    u":"  #  0x003a -> COLON
    u";"  #  0x003b -> SEMICOLON
    u"<"  #  0x003c -> LESS-THAN SIGN
    u"="  #  0x003d -> EQUALS SIGN
    u">"  #  0x003e -> GREATER-THAN SIGN
    u"?"  #  0x003f -> QUESTION MARK
    u"@"  #  0x0040 -> COMMERCIAL AT
    u"A"  #  0x0041 -> LATIN CAPITAL LETTER A
    u"B"  #  0x0042 -> LATIN CAPITAL LETTER B
    u"C"  #  0x0043 -> LATIN CAPITAL LETTER C
    u"D"  #  0x0044 -> LATIN CAPITAL LETTER D
    u"E"  #  0x0045 -> LATIN CAPITAL LETTER E
    u"F"  #  0x0046 -> LATIN CAPITAL LETTER F
    u"G"  #  0x0047 -> LATIN CAPITAL LETTER G
    u"H"  #  0x0048 -> LATIN CAPITAL LETTER H
    u"I"  #  0x0049 -> LATIN CAPITAL LETTER I
    u"J"  #  0x004a -> LATIN CAPITAL LETTER J
    u"K"  #  0x004b -> LATIN CAPITAL LETTER K
    u"L"  #  0x004c -> LATIN CAPITAL LETTER L
    u"M"  #  0x004d -> LATIN CAPITAL LETTER M
    u"N"  #  0x004e -> LATIN CAPITAL LETTER N
    u"O"  #  0x004f -> LATIN CAPITAL LETTER O
    u"P"  #  0x0050 -> LATIN CAPITAL LETTER P
    u"Q"  #  0x0051 -> LATIN CAPITAL LETTER Q
    u"R"  #  0x0052 -> LATIN CAPITAL LETTER R
    u"S"  #  0x0053 -> LATIN CAPITAL LETTER S
    u"T"  #  0x0054 -> LATIN CAPITAL LETTER T
    u"U"  #  0x0055 -> LATIN CAPITAL LETTER U
    u"V"  #  0x0056 -> LATIN CAPITAL LETTER V
    u"W"  #  0x0057 -> LATIN CAPITAL LETTER W
    u"X"  #  0x0058 -> LATIN CAPITAL LETTER X
    u"Y"  #  0x0059 -> LATIN CAPITAL LETTER Y
    u"Z"  #  0x005a -> LATIN CAPITAL LETTER Z
    u"["  #  0x005b -> LEFT SQUARE BRACKET
    u"\\"  #  0x005c -> REVERSE SOLIDUS
    u"]"  #  0x005d -> RIGHT SQUARE BRACKET
    u"^"  #  0x005e -> CIRCUMFLEX ACCENT
    u"_"  #  0x005f -> LOW LINE
    u"`"  #  0x0060 -> GRAVE ACCENT
    u"a"  #  0x0061 -> LATIN SMALL LETTER A
    u"b"  #  0x0062 -> LATIN SMALL LETTER B
    u"c"  #  0x0063 -> LATIN SMALL LETTER C
    u"d"  #  0x0064 -> LATIN SMALL LETTER D
    u"e"  #  0x0065 -> LATIN SMALL LETTER E
    u"f"  #  0x0066 -> LATIN SMALL LETTER F
    u"g"  #  0x0067 -> LATIN SMALL LETTER G
    u"h"  #  0x0068 -> LATIN SMALL LETTER H
    u"i"  #  0x0069 -> LATIN SMALL LETTER I
    u"j"  #  0x006a -> LATIN SMALL LETTER J
    u"k"  #  0x006b -> LATIN SMALL LETTER K
    u"l"  #  0x006c -> LATIN SMALL LETTER L
    u"m"  #  0x006d -> LATIN SMALL LETTER M
    u"n"  #  0x006e -> LATIN SMALL LETTER N
    u"o"  #  0x006f -> LATIN SMALL LETTER O
    u"p"  #  0x0070 -> LATIN SMALL LETTER P
    u"q"  #  0x0071 -> LATIN SMALL LETTER Q
    u"r"  #  0x0072 -> LATIN SMALL LETTER R
    u"s"  #  0x0073 -> LATIN SMALL LETTER S
    u"t"  #  0x0074 -> LATIN SMALL LETTER T
    u"u"  #  0x0075 -> LATIN SMALL LETTER U
    u"v"  #  0x0076 -> LATIN SMALL LETTER V
    u"w"  #  0x0077 -> LATIN SMALL LETTER W
    u"x"  #  0x0078 -> LATIN SMALL LETTER X
    u"y"  #  0x0079 -> LATIN SMALL LETTER Y
    u"z"  #  0x007a -> LATIN SMALL LETTER Z
    u"{"  #  0x007b -> LEFT CURLY BRACKET
    u"|"  #  0x007c -> VERTICAL LINE
    u"}"  #  0x007d -> RIGHT CURLY BRACKET
    u"~"  #  0x007e -> TILDE
    u"\x7f"  #  0x007f -> DELETE
    u"\xc7"  #  0x0080 -> LATIN CAPITAL LETTER C WITH CEDILLA
    u"\xfc"  #  0x0081 -> LATIN SMALL LETTER U WITH DIAERESIS
    u"\xe9"  #  0x0082 -> LATIN SMALL LETTER E WITH ACUTE
    u"\xe2"  #  0x0083 -> LATIN SMALL LETTER A WITH CIRCUMFLEX
    u"\xe4"  #  0x0084 -> LATIN SMALL LETTER A WITH DIAERESIS
    u"\u016f"  #  0x0085 -> LATIN SMALL LETTER U WITH RING ABOVE
    u"\u0107"  #  0x0086 -> LATIN SMALL LETTER C WITH ACUTE
    u"\xe7"  #  0x0087 -> LATIN SMALL LETTER C WITH CEDILLA
    u"\u0142"  #  0x0088 -> LATIN SMALL LETTER L WITH STROKE
    u"\xeb"  #  0x0089 -> LATIN SMALL LETTER E WITH DIAERESIS
    u"\u0150"  #  0x008a -> LATIN CAPITAL LETTER O WITH DOUBLE ACUTE
    u"\u0151"  #  0x008b -> LATIN SMALL LETTER O WITH DOUBLE ACUTE
    u"\xee"  #  0x008c -> LATIN SMALL LETTER I WITH CIRCUMFLEX
    u"\u0179"  #  0x008d -> LATIN CAPITAL LETTER Z WITH ACUTE
    u"\xc4"  #  0x008e -> LATIN CAPITAL LETTER A WITH DIAERESIS
    u"\u0106"  #  0x008f -> LATIN CAPITAL LETTER C WITH ACUTE
    u"\xc9"  #  0x0090 -> LATIN CAPITAL LETTER E WITH ACUTE
    u"\u0139"  #  0x0091 -> LATIN CAPITAL LETTER L WITH ACUTE
    u"\u013a"  #  0x0092 -> LATIN SMALL LETTER L WITH ACUTE
    u"\xf4"  #  0x0093 -> LATIN SMALL LETTER O WITH CIRCUMFLEX
    u"\xf6"  #  0x0094 -> LATIN SMALL LETTER O WITH DIAERESIS
    u"\u013d"  #  0x0095 -> LATIN CAPITAL LETTER L WITH CARON
    u"\u013e"  #  0x0096 -> LATIN SMALL LETTER L WITH CARON
    u"\u015a"  #  0x0097 -> LATIN CAPITAL LETTER S WITH ACUTE
    u"\u015b"  #  0x0098 -> LATIN SMALL LETTER S WITH ACUTE
    u"\xd6"  #  0x0099 -> LATIN CAPITAL LETTER O WITH DIAERESIS
    u"\xdc"  #  0x009a -> LATIN CAPITAL LETTER U WITH DIAERESIS
    u"\u0164"  #  0x009b -> LATIN CAPITAL LETTER T WITH CARON
    u"\u0165"  #  0x009c -> LATIN SMALL LETTER T WITH CARON
    u"\u0141"  #  0x009d -> LATIN CAPITAL LETTER L WITH STROKE
    u"\xd7"  #  0x009e -> MULTIPLICATION SIGN
    u"\u010d"  #  0x009f -> LATIN SMALL LETTER C WITH CARON
    u"\xe1"  #  0x00a0 -> LATIN SMALL LETTER A WITH ACUTE
    u"\xed"  #  0x00a1 -> LATIN SMALL LETTER I WITH ACUTE
    u"\xf3"  #  0x00a2 -> LATIN SMALL LETTER O WITH ACUTE
    u"\xfa"  #  0x00a3 -> LATIN SMALL LETTER U WITH ACUTE
    u"\u0104"  #  0x00a4 -> LATIN CAPITAL LETTER A WITH OGONEK
    u"\u0105"  #  0x00a5 -> LATIN SMALL LETTER A WITH OGONEK
    u"\u017d"  #  0x00a6 -> LATIN CAPITAL LETTER Z WITH CARON
    u"\u017e"  #  0x00a7 -> LATIN SMALL LETTER Z WITH CARON
    u"\u0118"  #  0x00a8 -> LATIN CAPITAL LETTER E WITH OGONEK
    u"\u0119"  #  0x00a9 -> LATIN SMALL LETTER E WITH OGONEK
    u"\xac"  #  0x00aa -> NOT SIGN
    u"\u017a"  #  0x00ab -> LATIN SMALL LETTER Z WITH ACUTE
    u"\u010c"  #  0x00ac -> LATIN CAPITAL LETTER C WITH CARON
    u"\u015f"  #  0x00ad -> LATIN SMALL LETTER S WITH CEDILLA
    u"\xab"  #  0x00ae -> LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    u"\xbb"  #  0x00af -> RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    u"\u2591"  #  0x00b0 -> LIGHT SHADE
    u"\u2592"  #  0x00b1 -> MEDIUM SHADE
    u"\u2593"  #  0x00b2 -> DARK SHADE
    u"\u2502"  #  0x00b3 -> BOX DRAWINGS LIGHT VERTICAL
    u"\u2524"  #  0x00b4 -> BOX DRAWINGS LIGHT VERTICAL AND LEFT
    u"\xc1"  #  0x00b5 -> LATIN CAPITAL LETTER A WITH ACUTE
    u"\xc2"  #  0x00b6 -> LATIN CAPITAL LETTER A WITH CIRCUMFLEX
    u"\u011a"  #  0x00b7 -> LATIN CAPITAL LETTER E WITH CARON
    u"\u015e"  #  0x00b8 -> LATIN CAPITAL LETTER S WITH CEDILLA
    u"\u2563"  #  0x00b9 -> BOX DRAWINGS DOUBLE VERTICAL AND LEFT
    u"\u2551"  #  0x00ba -> BOX DRAWINGS DOUBLE VERTICAL
    u"\u2557"  #  0x00bb -> BOX DRAWINGS DOUBLE DOWN AND LEFT
    u"\u255d"  #  0x00bc -> BOX DRAWINGS DOUBLE UP AND LEFT
    u"\u017b"  #  0x00bd -> LATIN CAPITAL LETTER Z WITH DOT ABOVE
    u"\u017c"  #  0x00be -> LATIN SMALL LETTER Z WITH DOT ABOVE
    u"\u2510"  #  0x00bf -> BOX DRAWINGS LIGHT DOWN AND LEFT
    u"\u2514"  #  0x00c0 -> BOX DRAWINGS LIGHT UP AND RIGHT
    u"\u2534"  #  0x00c1 -> BOX DRAWINGS LIGHT UP AND HORIZONTAL
    u"\u252c"  #  0x00c2 -> BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    u"\u251c"  #  0x00c3 -> BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    u"\u2500"  #  0x00c4 -> BOX DRAWINGS LIGHT HORIZONTAL
    u"\u253c"  #  0x00c5 -> BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    u"\u0102"  #  0x00c6 -> LATIN CAPITAL LETTER A WITH BREVE
    u"\u0103"  #  0x00c7 -> LATIN SMALL LETTER A WITH BREVE
    u"\u255a"  #  0x00c8 -> BOX DRAWINGS DOUBLE UP AND RIGHT
    u"\u2554"  #  0x00c9 -> BOX DRAWINGS DOUBLE DOWN AND RIGHT
    u"\u2569"  #  0x00ca -> BOX DRAWINGS DOUBLE UP AND HORIZONTAL
    u"\u2566"  #  0x00cb -> BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
    u"\u2560"  #  0x00cc -> BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
    u"\u2550"  #  0x00cd -> BOX DRAWINGS DOUBLE HORIZONTAL
    u"\u256c"  #  0x00ce -> BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
    u"\xa4"  #  0x00cf -> CURRENCY SIGN
    u"\u0111"  #  0x00d0 -> LATIN SMALL LETTER D WITH STROKE
    u"\u0110"  #  0x00d1 -> LATIN CAPITAL LETTER D WITH STROKE
    u"\u010e"  #  0x00d2 -> LATIN CAPITAL LETTER D WITH CARON
    u"\xcb"  #  0x00d3 -> LATIN CAPITAL LETTER E WITH DIAERESIS
    u"\u010f"  #  0x00d4 -> LATIN SMALL LETTER D WITH CARON
    u"\u0147"  #  0x00d5 -> LATIN CAPITAL LETTER N WITH CARON
    u"\xcd"  #  0x00d6 -> LATIN CAPITAL LETTER I WITH ACUTE
    u"\xce"  #  0x00d7 -> LATIN CAPITAL LETTER I WITH CIRCUMFLEX
    u"\u011b"  #  0x00d8 -> LATIN SMALL LETTER E WITH CARON
    u"\u2518"  #  0x00d9 -> BOX DRAWINGS LIGHT UP AND LEFT
    u"\u250c"  #  0x00da -> BOX DRAWINGS LIGHT DOWN AND RIGHT
    u"\u2588"  #  0x00db -> FULL BLOCK
    u"\u2584"  #  0x00dc -> LOWER HALF BLOCK
    u"\u0162"  #  0x00dd -> LATIN CAPITAL LETTER T WITH CEDILLA
    u"\u016e"  #  0x00de -> LATIN CAPITAL LETTER U WITH RING ABOVE
    u"\u2580"  #  0x00df -> UPPER HALF BLOCK
    u"\xd3"  #  0x00e0 -> LATIN CAPITAL LETTER O WITH ACUTE
    u"\xdf"  #  0x00e1 -> LATIN SMALL LETTER SHARP S
    u"\xd4"  #  0x00e2 -> LATIN CAPITAL LETTER O WITH CIRCUMFLEX
    u"\u0143"  #  0x00e3 -> LATIN CAPITAL LETTER N WITH ACUTE
    u"\u0144"  #  0x00e4 -> LATIN SMALL LETTER N WITH ACUTE
    u"\u0148"  #  0x00e5 -> LATIN SMALL LETTER N WITH CARON
    u"\u0160"  #  0x00e6 -> LATIN CAPITAL LETTER S WITH CARON
    u"\u0161"  #  0x00e7 -> LATIN SMALL LETTER S WITH CARON
    u"\u0154"  #  0x00e8 -> LATIN CAPITAL LETTER R WITH ACUTE
    u"\xda"  #  0x00e9 -> LATIN CAPITAL LETTER U WITH ACUTE
    u"\u0155"  #  0x00ea -> LATIN SMALL LETTER R WITH ACUTE
    u"\u0170"  #  0x00eb -> LATIN CAPITAL LETTER U WITH DOUBLE ACUTE
    u"\xfd"  #  0x00ec -> LATIN SMALL LETTER Y WITH ACUTE
    u"\xdd"  #  0x00ed -> LATIN CAPITAL LETTER Y WITH ACUTE
    u"\u0163"  #  0x00ee -> LATIN SMALL LETTER T WITH CEDILLA
    u"\xb4"  #  0x00ef -> ACUTE ACCENT
    u"\xad"  #  0x00f0 -> SOFT HYPHEN
    u"\u02dd"  #  0x00f1 -> DOUBLE ACUTE ACCENT
    u"\u02db"  #  0x00f2 -> OGONEK
    u"\u02c7"  #  0x00f3 -> CARON
    u"\u02d8"  #  0x00f4 -> BREVE
    u"\xa7"  #  0x00f5 -> SECTION SIGN
    u"\xf7"  #  0x00f6 -> DIVISION SIGN
    u"\xb8"  #  0x00f7 -> CEDILLA
    u"\xb0"  #  0x00f8 -> DEGREE SIGN
    u"\xa8"  #  0x00f9 -> DIAERESIS
    u"\u02d9"  #  0x00fa -> DOT ABOVE
    u"\u0171"  #  0x00fb -> LATIN SMALL LETTER U WITH DOUBLE ACUTE
    u"\u0158"  #  0x00fc -> LATIN CAPITAL LETTER R WITH CARON
    u"\u0159"  #  0x00fd -> LATIN SMALL LETTER R WITH CARON
    u"\u25a0"  #  0x00fe -> BLACK SQUARE
    u"\xa0"  #  0x00ff -> NO-BREAK SPACE
)

### Encoding Map

encoding_map = {
    0x0000: 0x0000,  #  NULL
    0x0001: 0x0001,  #  START OF HEADING
    0x0002: 0x0002,  #  START OF TEXT
    0x0003: 0x0003,  #  END OF TEXT
    0x0004: 0x0004,  #  END OF TRANSMISSION
    0x0005: 0x0005,  #  ENQUIRY
    0x0006: 0x0006,  #  ACKNOWLEDGE
    0x0007: 0x0007,  #  BELL
    0x0008: 0x0008,  #  BACKSPACE
    0x0009: 0x0009,  #  HORIZONTAL TABULATION
    0x000A: 0x000A,  #  LINE FEED
    0x000B: 0x000B,  #  VERTICAL TABULATION
    0x000C: 0x000C,  #  FORM FEED
    0x000D: 0x000D,  #  CARRIAGE RETURN
    0x000E: 0x000E,  #  SHIFT OUT
    0x000F: 0x000F,  #  SHIFT IN
    0x0010: 0x0010,  #  DATA LINK ESCAPE
    0x0011: 0x0011,  #  DEVICE CONTROL ONE
    0x0012: 0x0012,  #  DEVICE CONTROL TWO
    0x0013: 0x0013,  #  DEVICE CONTROL THREE
    0x0014: 0x0014,  #  DEVICE CONTROL FOUR
    0x0015: 0x0015,  #  NEGATIVE ACKNOWLEDGE
    0x0016: 0x0016,  #  SYNCHRONOUS IDLE
    0x0017: 0x0017,  #  END OF TRANSMISSION BLOCK
    0x0018: 0x0018,  #  CANCEL
    0x0019: 0x0019,  #  END OF MEDIUM
    0x001A: 0x001A,  #  SUBSTITUTE
    0x001B: 0x001B,  #  ESCAPE
    0x001C: 0x001C,  #  FILE SEPARATOR
    0x001D: 0x001D,  #  GROUP SEPARATOR
    0x001E: 0x001E,  #  RECORD SEPARATOR
    0x001F: 0x001F,  #  UNIT SEPARATOR
    0x0020: 0x0020,  #  SPACE
    0x0021: 0x0021,  #  EXCLAMATION MARK
    0x0022: 0x0022,  #  QUOTATION MARK
    0x0023: 0x0023,  #  NUMBER SIGN
    0x0024: 0x0024,  #  DOLLAR SIGN
    0x0025: 0x0025,  #  PERCENT SIGN
    0x0026: 0x0026,  #  AMPERSAND
    0x0027: 0x0027,  #  APOSTROPHE
    0x0028: 0x0028,  #  LEFT PARENTHESIS
    0x0029: 0x0029,  #  RIGHT PARENTHESIS
    0x002A: 0x002A,  #  ASTERISK
    0x002B: 0x002B,  #  PLUS SIGN
    0x002C: 0x002C,  #  COMMA
    0x002D: 0x002D,  #  HYPHEN-MINUS
    0x002E: 0x002E,  #  FULL STOP
    0x002F: 0x002F,  #  SOLIDUS
    0x0030: 0x0030,  #  DIGIT ZERO
    0x0031: 0x0031,  #  DIGIT ONE
    0x0032: 0x0032,  #  DIGIT TWO
    0x0033: 0x0033,  #  DIGIT THREE
    0x0034: 0x0034,  #  DIGIT FOUR
    0x0035: 0x0035,  #  DIGIT FIVE
    0x0036: 0x0036,  #  DIGIT SIX
    0x0037: 0x0037,  #  DIGIT SEVEN
    0x0038: 0x0038,  #  DIGIT EIGHT
    0x0039: 0x0039,  #  DIGIT NINE
    0x003A: 0x003A,  #  COLON
    0x003B: 0x003B,  #  SEMICOLON
    0x003C: 0x003C,  #  LESS-THAN SIGN
    0x003D: 0x003D,  #  EQUALS SIGN
    0x003E: 0x003E,  #  GREATER-THAN SIGN
    0x003F: 0x003F,  #  QUESTION MARK
    0x0040: 0x0040,  #  COMMERCIAL AT
    0x0041: 0x0041,  #  LATIN CAPITAL LETTER A
    0x0042: 0x0042,  #  LATIN CAPITAL LETTER B
    0x0043: 0x0043,  #  LATIN CAPITAL LETTER C
    0x0044: 0x0044,  #  LATIN CAPITAL LETTER D
    0x0045: 0x0045,  #  LATIN CAPITAL LETTER E
    0x0046: 0x0046,  #  LATIN CAPITAL LETTER F
    0x0047: 0x0047,  #  LATIN CAPITAL LETTER G
    0x0048: 0x0048,  #  LATIN CAPITAL LETTER H
    0x0049: 0x0049,  #  LATIN CAPITAL LETTER I
    0x004A: 0x004A,  #  LATIN CAPITAL LETTER J
    0x004B: 0x004B,  #  LATIN CAPITAL LETTER K
    0x004C: 0x004C,  #  LATIN CAPITAL LETTER L
    0x004D: 0x004D,  #  LATIN CAPITAL LETTER M
    0x004E: 0x004E,  #  LATIN CAPITAL LETTER N
    0x004F: 0x004F,  #  LATIN CAPITAL LETTER O
    0x0050: 0x0050,  #  LATIN CAPITAL LETTER P
    0x0051: 0x0051,  #  LATIN CAPITAL LETTER Q
    0x0052: 0x0052,  #  LATIN CAPITAL LETTER R
    0x0053: 0x0053,  #  LATIN CAPITAL LETTER S
    0x0054: 0x0054,  #  LATIN CAPITAL LETTER T
    0x0055: 0x0055,  #  LATIN CAPITAL LETTER U
    0x0056: 0x0056,  #  LATIN CAPITAL LETTER V
    0x0057: 0x0057,  #  LATIN CAPITAL LETTER W
    0x0058: 0x0058,  #  LATIN CAPITAL LETTER X
    0x0059: 0x0059,  #  LATIN CAPITAL LETTER Y
    0x005A: 0x005A,  #  LATIN CAPITAL LETTER Z
    0x005B: 0x005B,  #  LEFT SQUARE BRACKET
    0x005C: 0x005C,  #  REVERSE SOLIDUS
    0x005D: 0x005D,  #  RIGHT SQUARE BRACKET
    0x005E: 0x005E,  #  CIRCUMFLEX ACCENT
    0x005F: 0x005F,  #  LOW LINE
    0x0060: 0x0060,  #  GRAVE ACCENT
    0x0061: 0x0061,  #  LATIN SMALL LETTER A
    0x0062: 0x0062,  #  LATIN SMALL LETTER B
    0x0063: 0x0063,  #  LATIN SMALL LETTER C
    0x0064: 0x0064,  #  LATIN SMALL LETTER D
    0x0065: 0x0065,  #  LATIN SMALL LETTER E
    0x0066: 0x0066,  #  LATIN SMALL LETTER F
    0x0067: 0x0067,  #  LATIN SMALL LETTER G
    0x0068: 0x0068,  #  LATIN SMALL LETTER H
    0x0069: 0x0069,  #  LATIN SMALL LETTER I
    0x006A: 0x006A,  #  LATIN SMALL LETTER J
    0x006B: 0x006B,  #  LATIN SMALL LETTER K
    0x006C: 0x006C,  #  LATIN SMALL LETTER L
    0x006D: 0x006D,  #  LATIN SMALL LETTER M
    0x006E: 0x006E,  #  LATIN SMALL LETTER N
    0x006F: 0x006F,  #  LATIN SMALL LETTER O
    0x0070: 0x0070,  #  LATIN SMALL LETTER P
    0x0071: 0x0071,  #  LATIN SMALL LETTER Q
    0x0072: 0x0072,  #  LATIN SMALL LETTER R
    0x0073: 0x0073,  #  LATIN SMALL LETTER S
    0x0074: 0x0074,  #  LATIN SMALL LETTER T
    0x0075: 0x0075,  #  LATIN SMALL LETTER U
    0x0076: 0x0076,  #  LATIN SMALL LETTER V
    0x0077: 0x0077,  #  LATIN SMALL LETTER W
    0x0078: 0x0078,  #  LATIN SMALL LETTER X
    0x0079: 0x0079,  #  LATIN SMALL LETTER Y
    0x007A: 0x007A,  #  LATIN SMALL LETTER Z
    0x007B: 0x007B,  #  LEFT CURLY BRACKET
    0x007C: 0x007C,  #  VERTICAL LINE
    0x007D: 0x007D,  #  RIGHT CURLY BRACKET
    0x007E: 0x007E,  #  TILDE
    0x007F: 0x007F,  #  DELETE
    0x00A0: 0x00FF,  #  NO-BREAK SPACE
    0x00A4: 0x00CF,  #  CURRENCY SIGN
    0x00A7: 0x00F5,  #  SECTION SIGN
    0x00A8: 0x00F9,  #  DIAERESIS
    0x00AB: 0x00AE,  #  LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x00AC: 0x00AA,  #  NOT SIGN
    0x00AD: 0x00F0,  #  SOFT HYPHEN
    0x00B0: 0x00F8,  #  DEGREE SIGN
    0x00B4: 0x00EF,  #  ACUTE ACCENT
    0x00B8: 0x00F7,  #  CEDILLA
    0x00BB: 0x00AF,  #  RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x00C1: 0x00B5,  #  LATIN CAPITAL LETTER A WITH ACUTE
    0x00C2: 0x00B6,  #  LATIN CAPITAL LETTER A WITH CIRCUMFLEX
    0x00C4: 0x008E,  #  LATIN CAPITAL LETTER A WITH DIAERESIS
    0x00C7: 0x0080,  #  LATIN CAPITAL LETTER C WITH CEDILLA
    0x00C9: 0x0090,  #  LATIN CAPITAL LETTER E WITH ACUTE
    0x00CB: 0x00D3,  #  LATIN CAPITAL LETTER E WITH DIAERESIS
    0x00CD: 0x00D6,  #  LATIN CAPITAL LETTER I WITH ACUTE
    0x00CE: 0x00D7,  #  LATIN CAPITAL LETTER I WITH CIRCUMFLEX
    0x00D3: 0x00E0,  #  LATIN CAPITAL LETTER O WITH ACUTE
    0x00D4: 0x00E2,  #  LATIN CAPITAL LETTER O WITH CIRCUMFLEX
    0x00D6: 0x0099,  #  LATIN CAPITAL LETTER O WITH DIAERESIS
    0x00D7: 0x009E,  #  MULTIPLICATION SIGN
    0x00DA: 0x00E9,  #  LATIN CAPITAL LETTER U WITH ACUTE
    0x00DC: 0x009A,  #  LATIN CAPITAL LETTER U WITH DIAERESIS
    0x00DD: 0x00ED,  #  LATIN CAPITAL LETTER Y WITH ACUTE
    0x00DF: 0x00E1,  #  LATIN SMALL LETTER SHARP S
    0x00E1: 0x00A0,  #  LATIN SMALL LETTER A WITH ACUTE
    0x00E2: 0x0083,  #  LATIN SMALL LETTER A WITH CIRCUMFLEX
    0x00E4: 0x0084,  #  LATIN SMALL LETTER A WITH DIAERESIS
    0x00E7: 0x0087,  #  LATIN SMALL LETTER C WITH CEDILLA
    0x00E9: 0x0082,  #  LATIN SMALL LETTER E WITH ACUTE
    0x00EB: 0x0089,  #  LATIN SMALL LETTER E WITH DIAERESIS
    0x00ED: 0x00A1,  #  LATIN SMALL LETTER I WITH ACUTE
    0x00EE: 0x008C,  #  LATIN SMALL LETTER I WITH CIRCUMFLEX
    0x00F3: 0x00A2,  #  LATIN SMALL LETTER O WITH ACUTE
    0x00F4: 0x0093,  #  LATIN SMALL LETTER O WITH CIRCUMFLEX
    0x00F6: 0x0094,  #  LATIN SMALL LETTER O WITH DIAERESIS
    0x00F7: 0x00F6,  #  DIVISION SIGN
    0x00FA: 0x00A3,  #  LATIN SMALL LETTER U WITH ACUTE
    0x00FC: 0x0081,  #  LATIN SMALL LETTER U WITH DIAERESIS
    0x00FD: 0x00EC,  #  LATIN SMALL LETTER Y WITH ACUTE
    0x0102: 0x00C6,  #  LATIN CAPITAL LETTER A WITH BREVE
    0x0103: 0x00C7,  #  LATIN SMALL LETTER A WITH BREVE
    0x0104: 0x00A4,  #  LATIN CAPITAL LETTER A WITH OGONEK
    0x0105: 0x00A5,  #  LATIN SMALL LETTER A WITH OGONEK
    0x0106: 0x008F,  #  LATIN CAPITAL LETTER C WITH ACUTE
    0x0107: 0x0086,  #  LATIN SMALL LETTER C WITH ACUTE
    0x010C: 0x00AC,  #  LATIN CAPITAL LETTER C WITH CARON
    0x010D: 0x009F,  #  LATIN SMALL LETTER C WITH CARON
    0x010E: 0x00D2,  #  LATIN CAPITAL LETTER D WITH CARON
    0x010F: 0x00D4,  #  LATIN SMALL LETTER D WITH CARON
    0x0110: 0x00D1,  #  LATIN CAPITAL LETTER D WITH STROKE
    0x0111: 0x00D0,  #  LATIN SMALL LETTER D WITH STROKE
    0x0118: 0x00A8,  #  LATIN CAPITAL LETTER E WITH OGONEK
    0x0119: 0x00A9,  #  LATIN SMALL LETTER E WITH OGONEK
    0x011A: 0x00B7,  #  LATIN CAPITAL LETTER E WITH CARON
    0x011B: 0x00D8,  #  LATIN SMALL LETTER E WITH CARON
    0x0139: 0x0091,  #  LATIN CAPITAL LETTER L WITH ACUTE
    0x013A: 0x0092,  #  LATIN SMALL LETTER L WITH ACUTE
    0x013D: 0x0095,  #  LATIN CAPITAL LETTER L WITH CARON
    0x013E: 0x0096,  #  LATIN SMALL LETTER L WITH CARON
    0x0141: 0x009D,  #  LATIN CAPITAL LETTER L WITH STROKE
    0x0142: 0x0088,  #  LATIN SMALL LETTER L WITH STROKE
    0x0143: 0x00E3,  #  LATIN CAPITAL LETTER N WITH ACUTE
    0x0144: 0x00E4,  #  LATIN SMALL LETTER N WITH ACUTE
    0x0147: 0x00D5,  #  LATIN CAPITAL LETTER N WITH CARON
    0x0148: 0x00E5,  #  LATIN SMALL LETTER N WITH CARON
    0x0150: 0x008A,  #  LATIN CAPITAL LETTER O WITH DOUBLE ACUTE
    0x0151: 0x008B,  #  LATIN SMALL LETTER O WITH DOUBLE ACUTE
    0x0154: 0x00E8,  #  LATIN CAPITAL LETTER R WITH ACUTE
    0x0155: 0x00EA,  #  LATIN SMALL LETTER R WITH ACUTE
    0x0158: 0x00FC,  #  LATIN CAPITAL LETTER R WITH CARON
    0x0159: 0x00FD,  #  LATIN SMALL LETTER R WITH CARON
    0x015A: 0x0097,  #  LATIN CAPITAL LETTER S WITH ACUTE
    0x015B: 0x0098,  #  LATIN SMALL LETTER S WITH ACUTE
    0x015E: 0x00B8,  #  LATIN CAPITAL LETTER S WITH CEDILLA
    0x015F: 0x00AD,  #  LATIN SMALL LETTER S WITH CEDILLA
    0x0160: 0x00E6,  #  LATIN CAPITAL LETTER S WITH CARON
    0x0161: 0x00E7,  #  LATIN SMALL LETTER S WITH CARON
    0x0162: 0x00DD,  #  LATIN CAPITAL LETTER T WITH CEDILLA
    0x0163: 0x00EE,  #  LATIN SMALL LETTER T WITH CEDILLA
    0x0164: 0x009B,  #  LATIN CAPITAL LETTER T WITH CARON
    0x0165: 0x009C,  #  LATIN SMALL LETTER T WITH CARON
    0x016E: 0x00DE,  #  LATIN CAPITAL LETTER U WITH RING ABOVE
    0x016F: 0x0085,  #  LATIN SMALL LETTER U WITH RING ABOVE
    0x0170: 0x00EB,  #  LATIN CAPITAL LETTER U WITH DOUBLE ACUTE
    0x0171: 0x00FB,  #  LATIN SMALL LETTER U WITH DOUBLE ACUTE
    0x0179: 0x008D,  #  LATIN CAPITAL LETTER Z WITH ACUTE
    0x017A: 0x00AB,  #  LATIN SMALL LETTER Z WITH ACUTE
    0x017B: 0x00BD,  #  LATIN CAPITAL LETTER Z WITH DOT ABOVE
    0x017C: 0x00BE,  #  LATIN SMALL LETTER Z WITH DOT ABOVE
    0x017D: 0x00A6,  #  LATIN CAPITAL LETTER Z WITH CARON
    0x017E: 0x00A7,  #  LATIN SMALL LETTER Z WITH CARON
    0x02C7: 0x00F3,  #  CARON
    0x02D8: 0x00F4,  #  BREVE
    0x02D9: 0x00FA,  #  DOT ABOVE
    0x02DB: 0x00F2,  #  OGONEK
    0x02DD: 0x00F1,  #  DOUBLE ACUTE ACCENT
    0x2500: 0x00C4,  #  BOX DRAWINGS LIGHT HORIZONTAL
    0x2502: 0x00B3,  #  BOX DRAWINGS LIGHT VERTICAL
    0x250C: 0x00DA,  #  BOX DRAWINGS LIGHT DOWN AND RIGHT
    0x2510: 0x00BF,  #  BOX DRAWINGS LIGHT DOWN AND LEFT
    0x2514: 0x00C0,  #  BOX DRAWINGS LIGHT UP AND RIGHT
    0x2518: 0x00D9,  #  BOX DRAWINGS LIGHT UP AND LEFT
    0x251C: 0x00C3,  #  BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    0x2524: 0x00B4,  #  BOX DRAWINGS LIGHT VERTICAL AND LEFT
    0x252C: 0x00C2,  #  BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    0x2534: 0x00C1,  #  BOX DRAWINGS LIGHT UP AND HORIZONTAL
    0x253C: 0x00C5,  #  BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    0x2550: 0x00CD,  #  BOX DRAWINGS DOUBLE HORIZONTAL
    0x2551: 0x00BA,  #  BOX DRAWINGS DOUBLE VERTICAL
    0x2554: 0x00C9,  #  BOX DRAWINGS DOUBLE DOWN AND RIGHT
    0x2557: 0x00BB,  #  BOX DRAWINGS DOUBLE DOWN AND LEFT
    0x255A: 0x00C8,  #  BOX DRAWINGS DOUBLE UP AND RIGHT
    0x255D: 0x00BC,  #  BOX DRAWINGS DOUBLE UP AND LEFT
    0x2560: 0x00CC,  #  BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
    0x2563: 0x00B9,  #  BOX DRAWINGS DOUBLE VERTICAL AND LEFT
    0x2566: 0x00CB,  #  BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
    0x2569: 0x00CA,  #  BOX DRAWINGS DOUBLE UP AND HORIZONTAL
    0x256C: 0x00CE,  #  BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
    0x2580: 0x00DF,  #  UPPER HALF BLOCK
    0x2584: 0x00DC,  #  LOWER HALF BLOCK
    0x2588: 0x00DB,  #  FULL BLOCK
    0x2591: 0x00B0,  #  LIGHT SHADE
    0x2592: 0x00B1,  #  MEDIUM SHADE
    0x2593: 0x00B2,  #  DARK SHADE
    0x25A0: 0x00FE,  #  BLACK SQUARE
}
