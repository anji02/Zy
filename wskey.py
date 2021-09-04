# -*- coding: utf-8 -*
'''
cron: 15 */16 * * * wskey.py
new Env('wskey转换');
'''

import base64
import lzma

exec(lzma.decompress(base64.b64decode('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')))
