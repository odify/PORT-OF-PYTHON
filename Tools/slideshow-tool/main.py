#!/usr/bin/env python3


import os

#webtemplate:

print("""<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {box-sizing: border-box;}
html {
    height:740px;
}
body {background-color: Gainsboro;}

.mySlides {display: inline-block;}

img {vertical-align: middle;position:fixed;top:0px;left:0px;}
</style>
</head>
<body>

<img src="https://www.pngkey.com/png/full/339-3396597_2018-honda-civic-type-r-rear-angle-honda.png"/>

<script>
var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByTagName("img");
slides[0].style.opacity = "0";
  for (i = 1; i < slides.length; i++) {
    slides[i].style.display = "none"; 
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}   
   slides[slideIndex-1].style.display = "block"; 
 
  setTimeout(showSlides, 1000); // Change image every 3 seconds
}

</script>

</body>
</html>
""")



import urllib.request as req
url = 'https://de.cdn.mazda.media/3c7c7d9c041d45e7a96d3f619d02c132/99f5ef746f8c43cc83165518ba4b01a6.png?rnd=49bc43'
req.urlretrieve(url, 'river.png')

import urllib.request as req1
url = 'https://i.pinimg.com/originals/77/f9/a8/77f9a84b36bcc511df0f6be1c465c38b.png'
req1.urlretrieve(url, 'fuji.png');

import urllib.request as req2
url = 'https://smartcdn.prod.postmedia.digital/driving/wp-content/uploads/2021/05/chrome-image-413700.png'
req2.urlretrieve(url, 'palm.png');

import urllib.request as req3
url = 'https://freepngimg.com/thumb/honda/32430-8-honda-civic-transparent.png'
req3.urlretrieve(url, 'boats.png');

import urllib.request as req4
url = 'https://www.ford.ru/content/dam/guxeu/ru/ru_ru/vehicle-images/ecosport/Ford-Ecosport-ru-__-16x9-2160x1215-fc.png'
req4.urlretrieve(url, 'field.png');

import urllib.request as req5
url = 'https://www.pngall.com/wp-content/uploads/2016/05/Mercedes-Benz-Free-Download-PNG.png'
req5.urlretrieve(url, 'teahub.png');

import urllib.request as req6
url = 'https://freepngimg.com/thumb/chevrolet/32548-8-chevrolet-camaro-photo-thumb.png'
req6.urlretrieve(url, 'flowers.png');



