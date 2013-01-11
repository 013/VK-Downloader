# -*- coding: utf-8 -*-

import string
import unicodedata

__version__ = VERSION = '1.4'
__all__ = ['sanitize', 'FilenameSanitationFailed', 'InvalidFilename']

COMMON_VALID_CHARS = "-_.() %s%s" % (string.ascii_letters, string.digits)
RESERVED = {
    'windows': ['CON', 'PRN', 'AUX', 'NUL', 'COM0', 'COM1', 'COM2', 'COM3',
                'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'LPT0',
                'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 
                'LPT8', 'LPT9']
}

class FilenameSanitationFailed(Exception): pass
class InvalidFilename(Exception): pass

def _partition_filename(filename):
    ext_index = filename.rfind('.')
    if ext_index != -1:
        return (filename[:ext_index], filename[ext_index:])
    else:
        return (filename, None)

def sanitize(filename, limit=260, whitespace=True, lower=True):
    # Clean up characters
    temp = unicode(filename.strip())
    temp = unicodedata.normalize('NFKD', temp).encode('ASCII', 'ignore')
    temp = ''.join(c for c in temp if c in COMMON_VALID_CHARS)
    
    # Whitespace
    # Remove double spaces
    while '  ' in temp:
        temp = temp.replace('  ', ' ')
    # Substitute spaces
    if whitespace:
        temp = temp.replace(' ', '-')
    # Remove duplicate dashes
    while '--' in temp:
        temp = temp.replace('--', '-')
    
    # Length
    if len(temp) > limit:
        name, ext = _partition_filename(temp)
        if ext:
            # Can we keep this extension?
            if len(ext) < limit:
                chars_left = limit - len(ext)
                name = name[:chars_left]
                temp = ''.join([name, ext])
            else:
                raise FilenameSanitationFailed('Extension "{0}" is \
                        longer than limit "{1}"'.format(ext, limit))
        else:
            temp = temp[:limit]
    
    # Reserved words
    name, ext = _partition_filename(temp)
    for plat, reserved in RESERVED.items():
        for word in reserved:
            if name.lower() == word.lower():
                raise InvalidFilename('Filename "{0}" uses a reserved word: \
                                      "{1}"'.format(temp, word))
    
    # Lower output
    if lower:
        temp = temp.lower()
    
    return temp



if __name__ == '__main__':
    import unittest
    
    class TestConversion(unittest.TestCase):
        
        def test_doc_examples(self):
            filename = sanitize(u'qwerty$%&/-äç S P A C E.pdf')
            self.assertEqual(filename, 'qwerty-ac-s-p-a-c-e.pdf')
            filename = sanitize('Qwerty.pdf', limit=5)
            self.assertEqual(filename, 'q.pdf')
        
        def test_removal(self):
            filename = sanitize('qwerty<>:"/\|?*.pdf')
            self.assertEqual(filename, 'qwerty.pdf')
        
        def test_shorten(self):
            filename = sanitize('lorem', limit=3)
            self.assertEqual(filename, 'lor')
        
        def test_shorten_with_extension(self):
            filename = sanitize('lorem.pdf', limit=7)
            self.assertEqual(filename, 'lor.pdf')
        
        def helper_test_shorten_impossible(self):
            filename = sanitize('lorem.pdf', limit=3)
        
        def test_shorten_impossible(self):
            self.assertRaises(FilenameSanitationFailed,
                              self.helper_test_shorten_impossible)
        
        def helper_invalid(self):
            filename = sanitize('AUX')
        
        def test_invalid(self):
            self.assertRaises(InvalidFilename, self.helper_invalid)
        
        def helper_invalid_with_extension(self):
            filename = sanitize('AUX.pdf')
        
        def test_invalid_with_extension(self):
            self.assertRaises(InvalidFilename,
                              self.helper_invalid_with_extension)
        
        def test_whitespace_allowed(self):
            filename = sanitize(' q w e r t y .pdf', whitespace=False)
            self.assertEqual(filename, 'q w e r t y .pdf')
            filename = sanitize(' q     w e r   t y   .pdf', whitespace=False)
            self.assertEqual(filename, 'q w e r t y .pdf')
        
        def test_whitespace_not_allowed(self):
            filename = sanitize(' q w e r t y .pdf', whitespace=True)
            self.assertEqual(filename, 'q-w-e-r-t-y-.pdf')
            filename = sanitize(' q w       e r  t y .pdf', whitespace=True)
            self.assertEqual(filename, 'q-w-e-r-t-y-.pdf')
        
        def test_case(self):
            filename = sanitize('QwErTy.PDF', lower=True)
            self.assertEqual(filename, 'qwerty.pdf')
            filename = sanitize('QwErTy.PDF', lower=False)
            self.assertEqual(filename, 'QwErTy.PDF')
    
    unittest.main()
