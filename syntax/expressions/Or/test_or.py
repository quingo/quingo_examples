"""
function: test "or" function
testpoints:
    res[0]= true || true = true
    res[1]= true || false = true
    res[2]= false || true = true
    res[3]= false || false = false
    res[4][1]= false || res[4][0] = false&true
"""

import os.path
from qgrtsys.if_host.python import *

if_quingo = If_Quingo()


def test_or(detailed=False):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    kernel_file = dir_path + r"\or.qu"
    it_num = 10 if detailed else 1
    count = 0
    true_showed, false_showed = False, False
    while count < it_num:
        print("Iteration number: ", count)
        try:
            if_quingo.call_quingo(kernel_file, 'test_or')
            res = if_quingo.read_result()
            print("Result of or test is:", res)
        except:
            print("Fail to call the kernel")
            sys.exit(0)

        assert(res[0] == True)
        assert(res[1] == True)
        assert(res[2] == False)
        assert(res[3] == True)
        if res[4][0]:
            true_showed = True
            assert(res[4][1] == True)
        else:
            false_showed = True
            assert(res[4][1] == False)
        if true_showed and false_showed:
            return
        count += 1
    assert not detailed, "It is suspicious that the same result showed up to " + \
        str(it_num) + " times!"


if __name__ == '__main__':
    detailed = len(sys.argv) > 1 and sys.argv[1] == '--detailed'
    test_or(detailed)
