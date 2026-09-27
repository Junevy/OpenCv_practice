class my_dic(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError('the key is error')

    def __setattr__(self, key, value):
        self[key] = value

import unittest

class test_dict(unittest.TestCase):
    def test_init(self):
        d = my_dic(a = 1, b = 'test', c= '123')
        self.assertEqual(d['a'], 1)
        self.assertEqual(d['b'], 'test')
        self.assertEqual(b['c'], '123')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = my_dic()
        d['key'] = 'value'
        self.assertEqual(d['key'], 'value')

    def test_attr(self):
        d = my_dic()
        d.key = 'key'
        self.assertTrue('key' in d)

if __name__ == '__main__':
    unittest.main()