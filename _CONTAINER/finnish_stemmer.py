# Generated by Snowball 2.1.0 - https://snowballstem.org/

from .basestemmer import BaseStemmer
from .among import Among


class FinnishStemmer(BaseStemmer):
    """
    This class implements the stemming algorithm defined by a snowball script.
    Generated by Snowball 2.1.0 - https://snowballstem.org/
    """

    a_0 = [
        Among(u"pa", -1, 1),
        Among(u"sti", -1, 2),
        Among(u"kaan", -1, 1),
        Among(u"han", -1, 1),
        Among(u"kin", -1, 1),
        Among(u"h\u00E4n", -1, 1),
        Among(u"k\u00E4\u00E4n", -1, 1),
        Among(u"ko", -1, 1),
        Among(u"p\u00E4", -1, 1),
        Among(u"k\u00F6", -1, 1),
    ]

    a_1 = [
        Among(u"lla", -1, -1),
        Among(u"na", -1, -1),
        Among(u"ssa", -1, -1),
        Among(u"ta", -1, -1),
        Among(u"lta", 3, -1),
        Among(u"sta", 3, -1),
    ]

    a_2 = [
        Among(u"ll\u00E4", -1, -1),
        Among(u"n\u00E4", -1, -1),
        Among(u"ss\u00E4", -1, -1),
        Among(u"t\u00E4", -1, -1),
        Among(u"lt\u00E4", 3, -1),
        Among(u"st\u00E4", 3, -1),
    ]

    a_3 = [Among(u"lle", -1, -1), Among(u"ine", -1, -1)]

    a_4 = [
        Among(u"nsa", -1, 3),
        Among(u"mme", -1, 3),
        Among(u"nne", -1, 3),
        Among(u"ni", -1, 2),
        Among(u"si", -1, 1),
        Among(u"an", -1, 4),
        Among(u"en", -1, 6),
        Among(u"\u00E4n", -1, 5),
        Among(u"ns\u00E4", -1, 3),
    ]

    a_5 = [
        Among(u"aa", -1, -1),
        Among(u"ee", -1, -1),
        Among(u"ii", -1, -1),
        Among(u"oo", -1, -1),
        Among(u"uu", -1, -1),
        Among(u"\u00E4\u00E4", -1, -1),
        Among(u"\u00F6\u00F6", -1, -1),
    ]

    a_6 = [
        Among(u"a", -1, 8),
        Among(u"lla", 0, -1),
        Among(u"na", 0, -1),
        Among(u"ssa", 0, -1),
        Among(u"ta", 0, -1),
        Among(u"lta", 4, -1),
        Among(u"sta", 4, -1),
        Among(u"tta", 4, 2),
        Among(u"lle", -1, -1),
        Among(u"ine", -1, -1),
        Among(u"ksi", -1, -1),
        Among(u"n", -1, 7),
        Among(u"han", 11, 1),
        Among(u"den", 11, -1, "_FinnishStemmer__r_VI"),
        Among(u"seen", 11, -1, "_FinnishStemmer__r_LONG"),
        Among(u"hen", 11, 2),
        Among(u"tten", 11, -1, "_FinnishStemmer__r_VI"),
        Among(u"hin", 11, 3),
        Among(u"siin", 11, -1, "_FinnishStemmer__r_VI"),
        Among(u"hon", 11, 4),
        Among(u"h\u00E4n", 11, 5),
        Among(u"h\u00F6n", 11, 6),
        Among(u"\u00E4", -1, 8),
        Among(u"ll\u00E4", 22, -1),
        Among(u"n\u00E4", 22, -1),
        Among(u"ss\u00E4", 22, -1),
        Among(u"t\u00E4", 22, -1),
        Among(u"lt\u00E4", 26, -1),
        Among(u"st\u00E4", 26, -1),
        Among(u"tt\u00E4", 26, 2),
    ]

    a_7 = [
        Among(u"eja", -1, -1),
        Among(u"mma", -1, 1),
        Among(u"imma", 1, -1),
        Among(u"mpa", -1, 1),
        Among(u"impa", 3, -1),
        Among(u"mmi", -1, 1),
        Among(u"immi", 5, -1),
        Among(u"mpi", -1, 1),
        Among(u"impi", 7, -1),
        Among(u"ej\u00E4", -1, -1),
        Among(u"mm\u00E4", -1, 1),
        Among(u"imm\u00E4", 10, -1),
        Among(u"mp\u00E4", -1, 1),
        Among(u"imp\u00E4", 12, -1),
    ]

    a_8 = [Among(u"i", -1, -1), Among(u"j", -1, -1)]

    a_9 = [Among(u"mma", -1, 1), Among(u"imma", 0, -1)]

    g_AEI = [17, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8]

    g_C = [119, 223, 119, 1]

    g_V1 = [17, 65, 16, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 32]

    g_V2 = [17, 65, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 32]

    g_particle_end = [17, 97, 24, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 32]

    B_ending_removed = False
    S_x = ""
    I_p2 = 0
    I_p1 = 0

    def __r_mark_regions(self):
        self.I_p1 = self.limit
        self.I_p2 = self.limit
        if not self.go_out_grouping(FinnishStemmer.g_V1, 97, 246):
            return False
        if not self.go_in_grouping(FinnishStemmer.g_V1, 97, 246):
            return False
        self.cursor += 1
        self.I_p1 = self.cursor
        if not self.go_out_grouping(FinnishStemmer.g_V1, 97, 246):
            return False
        if not self.go_in_grouping(FinnishStemmer.g_V1, 97, 246):
            return False
        self.cursor += 1
        self.I_p2 = self.cursor
        return True

    def __r_R2(self):
        if not self.I_p2 <= self.cursor:
            return False
        return True

    def __r_particle_etc(self):
        if self.cursor < self.I_p1:
            return False
        v_2 = self.limit_backward
        self.limit_backward = self.I_p1
        self.ket = self.cursor
        among_var = self.find_among_b(FinnishStemmer.a_0)
        if among_var == 0:
            self.limit_backward = v_2
            return False
        self.bra = self.cursor
        self.limit_backward = v_2
        if among_var == 1:
            if not self.in_grouping_b(FinnishStemmer.g_particle_end, 97, 246):
                return False
        else:
            if not self.__r_R2():
                return False
        if not self.slice_del():
            return False

        return True

    def __r_possessive(self):
        if self.cursor < self.I_p1:
            return False
        v_2 = self.limit_backward
        self.limit_backward = self.I_p1
        self.ket = self.cursor
        among_var = self.find_among_b(FinnishStemmer.a_4)
        if among_var == 0:
            self.limit_backward = v_2
            return False
        self.bra = self.cursor
        self.limit_backward = v_2
        if among_var == 1:
            v_3 = self.limit - self.cursor
            try:
                if not self.eq_s_b(u"k"):
                    raise lab0()
                return False
            except lab0:
                pass
            self.cursor = self.limit - v_3
            if not self.slice_del():
                return False

        elif among_var == 2:
            if not self.slice_del():
                return False

            self.ket = self.cursor
            if not self.eq_s_b(u"kse"):
                return False
            self.bra = self.cursor
            if not self.slice_from(u"ksi"):
                return False
        elif among_var == 3:
            if not self.slice_del():
                return False

        elif among_var == 4:
            if self.find_among_b(FinnishStemmer.a_1) == 0:
                return False
            if not self.slice_del():
                return False

        elif among_var == 5:
            if self.find_among_b(FinnishStemmer.a_2) == 0:
                return False
            if not self.slice_del():
                return False

        else:
            if self.find_among_b(FinnishStemmer.a_3) == 0:
                return False
            if not self.slice_del():
                return False

        return True

    def __r_LONG(self):
        if self.find_among_b(FinnishStemmer.a_5) == 0:
            return False
        return True

    def __r_VI(self):
        if not self.eq_s_b(u"i"):
            return False
        if not self.in_grouping_b(FinnishStemmer.g_V2, 97, 246):
            return False
        return True

    def __r_case_ending(self):
        if self.cursor < self.I_p1:
            return False
        v_2 = self.limit_backward
        self.limit_backward = self.I_p1
        self.ket = self.cursor
        among_var = self.find_among_b(FinnishStemmer.a_6)
        if among_var == 0:
            self.limit_backward = v_2
            return False
        self.bra = self.cursor
        self.limit_backward = v_2
        if among_var == 1:
            if not self.eq_s_b(u"a"):
                return False
        elif among_var == 2:
            if not self.eq_s_b(u"e"):
                return False
        elif among_var == 3:
            if not self.eq_s_b(u"i"):
                return False
        elif among_var == 4:
            if not self.eq_s_b(u"o"):
                return False
        elif among_var == 5:
            if not self.eq_s_b(u"\u00E4"):
                return False
        elif among_var == 6:
            if not self.eq_s_b(u"\u00F6"):
                return False
        elif among_var == 7:
            v_3 = self.limit - self.cursor
            try:
                v_4 = self.limit - self.cursor
                try:
                    v_5 = self.limit - self.cursor
                    try:
                        if not self.__r_LONG():
                            raise lab2()
                        raise lab1()
                    except lab2:
                        pass
                    self.cursor = self.limit - v_5
                    if not self.eq_s_b(u"ie"):
                        self.cursor = self.limit - v_3
                        raise lab0()
                except lab1:
                    pass
                self.cursor = self.limit - v_4
                if self.cursor <= self.limit_backward:
                    self.cursor = self.limit - v_3
                    raise lab0()
                self.cursor -= 1
                self.bra = self.cursor
            except lab0:
                pass
        elif among_var == 8:
            if not self.in_grouping_b(FinnishStemmer.g_V1, 97, 246):
                return False
            if not self.in_grouping_b(FinnishStemmer.g_C, 98, 122):
                return False
        if not self.slice_del():
            return False

        self.B_ending_removed = True
        return True

    def __r_other_endings(self):
        if self.cursor < self.I_p2:
            return False
        v_2 = self.limit_backward
        self.limit_backward = self.I_p2
        self.ket = self.cursor
        among_var = self.find_among_b(FinnishStemmer.a_7)
        if among_var == 0:
            self.limit_backward = v_2
            return False
        self.bra = self.cursor
        self.limit_backward = v_2
        if among_var == 1:
            v_3 = self.limit - self.cursor
            try:
                if not self.eq_s_b(u"po"):
                    raise lab0()
                return False
            except lab0:
                pass
            self.cursor = self.limit - v_3
        if not self.slice_del():
            return False

        return True

    def __r_i_plural(self):
        if self.cursor < self.I_p1:
            return False
        v_2 = self.limit_backward
        self.limit_backward = self.I_p1
        self.ket = self.cursor
        if self.find_among_b(FinnishStemmer.a_8) == 0:
            self.limit_backward = v_2
            return False
        self.bra = self.cursor
        self.limit_backward = v_2
        if not self.slice_del():
            return False

        return True

    def __r_t_plural(self):
        if self.cursor < self.I_p1:
            return False
        v_2 = self.limit_backward
        self.limit_backward = self.I_p1
        self.ket = self.cursor
        if not self.eq_s_b(u"t"):
            self.limit_backward = v_2
            return False
        self.bra = self.cursor
        v_3 = self.limit - self.cursor
        if not self.in_grouping_b(FinnishStemmer.g_V1, 97, 246):
            self.limit_backward = v_2
            return False
        self.cursor = self.limit - v_3
        if not self.slice_del():
            return False

        self.limit_backward = v_2
        if self.cursor < self.I_p2:
            return False
        v_5 = self.limit_backward
        self.limit_backward = self.I_p2
        self.ket = self.cursor
        among_var = self.find_among_b(FinnishStemmer.a_9)
        if among_var == 0:
            self.limit_backward = v_5
            return False
        self.bra = self.cursor
        self.limit_backward = v_5
        if among_var == 1:
            v_6 = self.limit - self.cursor
            try:
                if not self.eq_s_b(u"po"):
                    raise lab0()
                return False
            except lab0:
                pass
            self.cursor = self.limit - v_6
        if not self.slice_del():
            return False

        return True

    def __r_tidy(self):
        if self.cursor < self.I_p1:
            return False
        v_2 = self.limit_backward
        self.limit_backward = self.I_p1
        v_3 = self.limit - self.cursor
        try:
            v_4 = self.limit - self.cursor
            if not self.__r_LONG():
                raise lab0()
            self.cursor = self.limit - v_4
            self.ket = self.cursor
            if self.cursor <= self.limit_backward:
                raise lab0()
            self.cursor -= 1
            self.bra = self.cursor
            if not self.slice_del():
                return False

        except lab0:
            pass
        self.cursor = self.limit - v_3
        v_5 = self.limit - self.cursor
        try:
            self.ket = self.cursor
            if not self.in_grouping_b(FinnishStemmer.g_AEI, 97, 228):
                raise lab1()
            self.bra = self.cursor
            if not self.in_grouping_b(FinnishStemmer.g_C, 98, 122):
                raise lab1()
            if not self.slice_del():
                return False

        except lab1:
            pass
        self.cursor = self.limit - v_5
        v_6 = self.limit - self.cursor
        try:
            self.ket = self.cursor
            if not self.eq_s_b(u"j"):
                raise lab2()
            self.bra = self.cursor
            try:
                v_7 = self.limit - self.cursor
                try:
                    if not self.eq_s_b(u"o"):
                        raise lab4()
                    raise lab3()
                except lab4:
                    pass
                self.cursor = self.limit - v_7
                if not self.eq_s_b(u"u"):
                    raise lab2()
            except lab3:
                pass
            if not self.slice_del():
                return False

        except lab2:
            pass
        self.cursor = self.limit - v_6
        v_8 = self.limit - self.cursor
        try:
            self.ket = self.cursor
            if not self.eq_s_b(u"o"):
                raise lab5()
            self.bra = self.cursor
            if not self.eq_s_b(u"j"):
                raise lab5()
            if not self.slice_del():
                return False

        except lab5:
            pass
        self.cursor = self.limit - v_8
        self.limit_backward = v_2
        if not self.go_in_grouping_b(FinnishStemmer.g_V1, 97, 246):
            return False
        self.ket = self.cursor
        if not self.in_grouping_b(FinnishStemmer.g_C, 98, 122):
            return False
        self.bra = self.cursor
        self.S_x = self.slice_to()
        if self.S_x == "":
            return False
        if not self.eq_s_b(self.S_x):
            return False
        if not self.slice_del():
            return False

        return True

    def _stem(self):
        v_1 = self.cursor
        self.__r_mark_regions()
        self.cursor = v_1
        self.B_ending_removed = False
        self.limit_backward = self.cursor
        self.cursor = self.limit
        v_2 = self.limit - self.cursor
        self.__r_particle_etc()
        self.cursor = self.limit - v_2
        v_3 = self.limit - self.cursor
        self.__r_possessive()
        self.cursor = self.limit - v_3
        v_4 = self.limit - self.cursor
        self.__r_case_ending()
        self.cursor = self.limit - v_4
        v_5 = self.limit - self.cursor
        self.__r_other_endings()
        self.cursor = self.limit - v_5
        try:
            try:
                if not self.B_ending_removed:
                    raise lab1()
                v_7 = self.limit - self.cursor
                self.__r_i_plural()
                self.cursor = self.limit - v_7
                raise lab0()
            except lab1:
                pass
            v_8 = self.limit - self.cursor
            self.__r_t_plural()
            self.cursor = self.limit - v_8
        except lab0:
            pass
        v_9 = self.limit - self.cursor
        self.__r_tidy()
        self.cursor = self.limit - v_9
        self.cursor = self.limit_backward
        return True


class lab0(BaseException):
    pass


class lab1(BaseException):
    pass


class lab2(BaseException):
    pass


class lab3(BaseException):
    pass


class lab4(BaseException):
    pass


class lab5(BaseException):
    pass
