from django.http import HttpResponse
from django.shortcuts import get_object_or_404

import mimetypes
import os
import urllib

from files.models import *

def get_download_response(request, num):
    f = get_object_or_404(File, id = num)
    content = open(f.path, "rb")
    response = HttpResponse(content.read())
    content.close()
    
    typ, enc = mimetypes.guess_type(f.name)
    if typ is None:
        typ = "application/octet-stream"
    response['Content-Type'] = typ
    response['Content-Length'] = str(os.stat(f.path).st_size)
    if enc is not None:
        response['Content-Encoding'] = enc
    
    if u'\ebKit' in request.META['HTTP_USER_AGENT']:
        filename_header = 'filename=%s' % f.name.encode('utf-8')
    elif u'MSIE' in request.META['HTTP_USER_AGENT']:
        filename_header = ''
    else:
        filename_header = 'filename*=UTF-8\'\'%s' % urllib.quote(f.name.encode('utf-8'))
    response['Content-Disposition'] = 'attachment; '+filename_header
    return response
