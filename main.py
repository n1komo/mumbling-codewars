
def accum(s):
    rdy_list = []
    for count, letter in enumerate(s):
        rdy_list.append( letter.upper() + (letter.lower() * count) )
    return '-'.join(rdy_list)


#     sample tests
#
# accum("abcd")
# accum("RqaEzty")
# accum("cwAt")
# accum("abcd")
# accum("RqaEzty")
# accum("cwAt")