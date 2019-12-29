import requests
import os



def is_downloadable(url):

    while True:
        try:
            h = requests.head(url, allow_redirects=True)
            header = h.headers
            content_type = header.get('content-type')  
            break 
        except Exception as e:
            print ('Exception:', e)
            pass    

    if 'image' in content_type.lower():
        return True

    return False



def download(url, folder):   

    while True:
        try:
            r = requests.get(url, allow_redirects=True)
            break
        except Exception as e:
            print ('Exception:', e)
            pass
            
    filename = url.rsplit('/', 1)[1]
    open(folder + '/' + filename, 'wb').write(r.content)

    pass



def ensure_dir(file_path):

    directory = os.path.dirname(file_path)

    if not os.path.exists(directory):
        os.makedirs(directory)


# main

print ("This is Viber stickers downloader %)")

ensure_dir('./stickers/')

for pack in range(1,2010):

    pack_format = str("{:0>4d}".format(pack))
    pack_dir = './stickers/' + pack_format + '/'

    for sticker in range(0,99):

        sticker_format = str("{:0>2d}".format(sticker))
        resolution = "144" # 72 or 144
        sticker_url = 'http://content.cdn.viber.com/stickers/' + resolution + '/' + str(pack) + '00/00' + pack_format + sticker_format + '.png'
        
        if not is_downloadable(sticker_url):
            break
        
        print(sticker_url)

        if sticker == 0:
            ensure_dir(pack_dir)
            
        download(sticker_url, pack_dir) 

print('That\'s all, folks!')


