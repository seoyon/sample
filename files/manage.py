from files.models import *
import os

BASE_DIR = os.path.join(os.path.dirname(__file__), "attach/")

def upload(f):
    name = f.name.replace(" ", "_").replace(",", "_")
    path = os.path.join(BASE_DIR, name)
    with open(path, "wb") as dest:
        for chunk in f.chunks():
            dest.write(chunk)
    File(
        name = name,
        path = path
    ).save()

def delete(f_id):
    f = File.objects.get(id = f_id)
    os.remove(f.path)
    f.delete()
