"""
    pygments.lexers._vbscript_builtins
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    These are manually translated lists from
    http://www.indusoft.com/pdf/VBScript%20Reference.pdf.

    :copyright: Copyright 2006-2021 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

KEYWORDS = [
    "ByRef",
    "ByVal",
    # dim: special rule
    "call",
    "case",
    "class",
    # const: special rule
    "do",
    "each",
    "else",
    "elseif",
    "end",
    "erase",
    "execute",
    "function",
    "exit",
    "for",
    "function",
    "GetRef",
    "global",
    "if",
    "let",
    "loop",
    "next",
    "new",
    # option: special rule
    "private",
    "public",
    "redim",
    "select",
    "set",
    "sub",
    "then",
    "wend",
    "while",
    "with",
]

BUILTIN_FUNCTIONS = [
    "Abs",
    "Array",
    "Asc",
    "Atn",
    "CBool",
    "CByte",
    "CCur",
    "CDate",
    "CDbl",
    "Chr",
    "CInt",
    "CLng",
    "Cos",
    "CreateObject",
    "CSng",
    "CStr",
    "Date",
    "DateAdd",
    "DateDiff",
    "DatePart",
    "DateSerial",
    "DateValue",
    "Day",
    "Eval",
    "Exp",
    "Filter",
    "Fix",
    "FormatCurrency",
    "FormatDateTime",
    "FormatNumber",
    "FormatPercent",
    "GetObject",
    "GetLocale",
    "Hex",
    "Hour",
    "InStr",
    "inStrRev",
    "Int",
    "IsArray",
    "IsDate",
    "IsEmpty",
    "IsNull",
    "IsNumeric",
    "IsObject",
    "Join",
    "LBound",
    "LCase",
    "Left",
    "Len",
    "LoadPicture",
    "Log",
    "LTrim",
    "Mid",
    "Minute",
    "Month",
    "MonthName",
    "MsgBox",
    "Now",
    "Oct",
    "Randomize",
    "RegExp",
    "Replace",
    "RGB",
    "Right",
    "Rnd",
    "Round",
    "RTrim",
    "ScriptEngine",
    "ScriptEngineBuildVersion",
    "ScriptEngineMajorVersion",
    "ScriptEngineMinorVersion",
    "Second",
    "SetLocale",
    "Sgn",
    "Space",
    "Split",
    "Sqr",
    "StrComp",
    "String",
    "StrReverse",
    "Tan",
    "Time",
    "Timer",
    "TimeSerial",
    "TimeValue",
    "Trim",
    "TypeName",
    "UBound",
    "UCase",
    "VarType",
    "Weekday",
    "WeekdayName",
    "Year",
]

BUILTIN_VARIABLES = [
    "Debug",
    "Dictionary",
    "Drive",
    "Drives",
    "Err",
    "File",
    "Files",
    "FileSystemObject",
    "Folder",
    "Folders",
    "Match",
    "Matches",
    "RegExp",
    "Submatches",
    "TextStream",
]

OPERATORS = [
    "+",
    "-",
    "*",
    "/",
    "\\",
    "^",
    "|",
    "<",
    "<=",
    ">",
    ">=",
    "=",
    "<>",
    "&",
    "$",
]

OPERATOR_WORDS = ["mod", "and", "or", "xor", "eqv", "imp", "is", "not"]

BUILTIN_CONSTANTS = [
    "False",
    "True",
    "vbAbort",
    "vbAbortRetryIgnore",
    "vbApplicationModal",
    "vbArray",
    "vbBinaryCompare",
    "vbBlack",
    "vbBlue",
    "vbBoole",
    "vbByte",
    "vbCancel",
    "vbCr",
    "vbCritical",
    "vbCrLf",
    "vbCurrency",
    "vbCyan",
    "vbDataObject",
    "vbDate",
    "vbDefaultButton1",
    "vbDefaultButton2",
    "vbDefaultButton3",
    "vbDefaultButton4",
    "vbDouble",
    "vbEmpty",
    "vbError",
    "vbExclamation",
    "vbFalse",
    "vbFirstFullWeek",
    "vbFirstJan1",
    "vbFormFeed",
    "vbFriday",
    "vbGeneralDate",
    "vbGreen",
    "vbIgnore",
    "vbInformation",
    "vbInteger",
    "vbLf",
    "vbLong",
    "vbLongDate",
    "vbLongTime",
    "vbMagenta",
    "vbMonday",
    "vbMsgBoxHelpButton",
    "vbMsgBoxRight",
    "vbMsgBoxRtlReading",
    "vbMsgBoxSetForeground",
    "vbNewLine",
    "vbNo",
    "vbNull",
    "vbNullChar",
    "vbNullString",
    "vbObject",
    "vbObjectError",
    "vbOK",
    "vbOKCancel",
    "vbOKOnly",
    "vbQuestion",
    "vbRed",
    "vbRetry",
    "vbRetryCancel",
    "vbSaturday",
    "vbShortDate",
    "vbShortTime",
    "vbSingle",
    "vbString",
    "vbSunday",
    "vbSystemModal",
    "vbTab",
    "vbTextCompare",
    "vbThursday",
    "vbTrue",
    "vbTuesday",
    "vbUseDefault",
    "vbUseSystem",
    "vbUseSystem",
    "vbVariant",
    "vbVerticalTab",
    "vbWednesday",
    "vbWhite",
    "vbYellow",
    "vbYes",
    "vbYesNo",
    "vbYesNoCancel",
]
