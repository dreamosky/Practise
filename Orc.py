from tesserocr import PyTessBaseAPI

images = ['test_jpn_01.jpg', 'test_jpn_02.jpg', 'test_jpn_03.jpg']

with PyTessBaseAPI(lang='jpn', psm=1) as api:
    for img in images:
        api.SetImageFile(img)
        print(api.GetUTF8Text())