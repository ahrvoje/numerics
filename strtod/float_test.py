import struct
import toml


with open('strtod_tests.toml') as tests_file:
    def execute_tests(test_class):
        all_test_ok = True
        for test in tests[test_class]:
            test_str = test['str']

            if 'nan' in test_str.lower():
                continue

            x = float(test_str)
            hex_result = hex(struct.unpack('<Q', struct.pack('<d', x))[0])[2:].zfill(16)

            if hex_result != test['hex']:
                print('Test UID %s failed!' % test['UID'])
                all_test_ok = False

        if all_test_ok:
            print('All %d %s passed OK.' % (len(tests[test_class]), test_class))

    tests = toml.loads(tests_file.read())

    execute_tests('FormattingTests')
    execute_tests('ConversionTests')


# Python 3.5.1 64-bit on Win10
# All 35 FormattingTests passed OK.
# All 75 ConversionTests passed OK.
