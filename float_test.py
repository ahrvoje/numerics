import struct
import toml

with open('strtod_tests.toml') as tests_file:
    tests = toml.loads(tests_file.read())
    conversion_tests = tests['conversionTests']

    all_test_ok = True
    for conversion_test in conversion_tests:
        x = float(conversion_test['str'])
        hex_result = hex(struct.unpack('<Q', struct.pack('<d', x))[0])[2:].zfill(16)

        if hex_result != conversion_test['hex']:
            print('Test UID %s failed!' % conversion_test['UID'])
            all_test_ok = False

    if all_test_ok:
        print('All %d conversion tests passed OK.' % len(conversion_tests))

# Python 3.5.1 64-bit on Win10
# All 75 conversion tests passed OK.
