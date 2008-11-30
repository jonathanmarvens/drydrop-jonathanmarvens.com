# -*- mode: python; coding: utf-8 -*-
import os
import os.path
import glob
import re
import string
import time
from app.consts import *
from lib.utils import *
import urlparse
from drydrop_handler import DRY_ROOT

def cache_buster(html, dev):
    def url_replacer(match):
        def get_stamp(files):
            stamp = ""
            for file in files:
                try:
                    s = os.stat(file)
                    stamp += time.strftime("%H%M%S", time.localtime(s.st_mtime))
                except:
                    # TODO: log this situation? missing main.html is a valid case
                    pass
            return stamp
        
        # break url into parts
        url = match.groups(1)[1]
        parts = urlparse.urlparse(url)
        original = match.groups(1)[0]
        
        # do not touch absolute urls
        is_absolute = parts[1]!=''
        if is_absolute:
            return original
        
        path = os.path.join(DRY_ROOT, 'sys', parts[2].lstrip('/'))
        dir = os.path.dirname(path)
        
        files = [path]
        base = os.path.basename(path)
        
        stamp = get_stamp(files)
        
        if parts[3]=='':
            part3 = stamp
        else:
            part3 = parts[3] + "&" + stamp
            
        new_url = parts[2]+"?"+part3
        result = string.replace(original, url, new_url)
        return result
        
    html = re.sub(r'(src="([^"]*)")', url_replacer, html)
    html = re.sub(r'(src=\'([^\']*)\')', url_replacer, html)
    html = re.sub(r'(href="([^#][^"]*)")', url_replacer, html)
    html = re.sub(r'(href=\'([^#][^\']*)\')', url_replacer, html)
    return html