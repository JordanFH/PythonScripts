# coding=utf-8
import os

pathname = r"C:\Users\USER03-60\Downloads\PracticaSIG2"


# print pathname
# print (os.listdir(pathname))
# print (len(pathname))
# print (pathname[-1])
# s = "COVER"
# print s[1:3]
# print s[:3]

# substring = "tree"
# output = "trees_buffer.shp"
#
# print substring in output

# line = "asfasfasf,dsadasddas,dasdsa"
# print line
# line = line.replace(",", ".")
# print line


def remove_accent(input_string):
    accents = u"áéíóúÁÉÍÓÚ"
    change = "aeiouAEIOU"

    i = 0
    if len(input_string) > 0:
        for s in input_string:
            s = s.encode('utf-8', 'ignore').decode('utf-8')
            for r in accents:
                if r == s:
                    input_string = input_string.replace(s, change[i])
                i += 1
            i = 0
        return input_string

    return ""


s = u"áasfsafsaé"

print remove_accent(s)
