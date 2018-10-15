#!/usr/bin/env python
import sys
import os
from tinytag import TinyTag

def changed_filename(file, track):
    return "{:03d}__{}".format(track, file)


def main():
    if len(sys.argv)<2:
        print("Usage")
        sys.exit(1)
    dirname = sys.argv[1]
    files = os.listdir(dirname)
    file_table=[]
    for f in sorted(files):
        file = os.path.join(dirname,f)
        try: 
            tag=TinyTag.get(file)
            t=0 if tag.track is None else int(tag.track)
        except:
            continue
        fchanged=changed_filename(f,t)
        print(f,"->",fchanged)
        file_table.append((file,os.path.join(dirname,fchanged)))
    print("Change file names? [y/n]:",end="")
    ans=input()
    if ans.lower()=="y":
        for x, y in file_table:
            os.rename(x,y)


if __name__=="__main__":
    main()
            
