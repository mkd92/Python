import re


def stripping(sting_to_strip, *args):
    if args:
        return re.sub(args[0], "", sting_to_strip)
    space_regex = re.compile(r'\S')
    return "".join(space_regex.findall(sting_to_strip))


print(stripping("man ij f ng   nf  d nd fn", "nd"))
