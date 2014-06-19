# Requirements
# $ apt-get install libmagickwand-dev
# $ pip install Wand


from wand.image import Image
with Image(filename='/test.pdf', resolution=200) as image:
   image.compression_quality = 99
   image.save(filename='test.jpg')
             
