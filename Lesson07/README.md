# Lesson 7: Style Transfer
Notes are available in the [notes](notes/) folder.

The [scripts](scripts/) folder contains a single script used in the lesson for applying style transfer from a given image to another image. For this script I chose a personal image I took while walking in the woods. The style image was retrieved from [here](http://hdwpro.com/artistic-wallpaper.html).

The resulting stylized image:

<image src="scripts/images/stylized_image.jpeg" width=300>

## Lessons learned:
* When using images with different orientations, such as a 'portrait' content image and a 'landscape' style image, I noticed that streaky artifacts appear in the resulting target image. This is the result of 'squishing' the style image resulting in narrow features. Cropping the image to reduce the amount of squishing needed helped resolve this.