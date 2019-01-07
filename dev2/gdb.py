#https://sourceware.org/gdb/onlinedocs/gdb/Python-API.html#Python-API
#I have used a lot this website

class Fpoint_CMD (gdb.Command):
    """Report all the pointers present in the area that point to other addresses in the same range"""
    def __init__(self):
        super(Fpoint_CMD, self).__init__("fpointers", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        argv=gdb.string_to_argv(arg)
        start_range = int(argv[0], 16)
        delta_range = int(argv[1], 16)
        end_range = start_range + delta_range
        for address in range(start_range, end_range+1):
            return_val = int(gdb.execute("x/gx" + hex(address), True, True).split(':')[1], 16)
            if return_val in range(start_range, end_range):
                print ('Pointer at {} --> {}'.format(hex(address), hex(return_val)))

Fpoint_CMD ()
