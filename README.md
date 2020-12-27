# 🎨 random_shapes

Turn your photos into art. 

## About

This script takes a photo as input and returns an abstract version of it:

![skyline](sky.png)

## How does it work?

The program uses a number of iterations as input by the user to **randomly** overlay "N" number of rectangles with area "A" (whose range of aspect ratios can be defined) for each iteration. The area and number of rectangles decreases and increases with rates and models entered as desired by the user. Each rectangle is then shaded according to the mean area it covers from the original photo. Here's an example of what happens as you increase the number of iterations in *.gif* format:

![city](city.gif)

There are also two other functions aside from the main "paint" function to help generate frames for making gifs. "gifproducer" increments the number of iterations and saves a picture at the end of each iteration to visualize what happens with increasing iterations (above gif). "gifstatic" on the other hand, will generate the *same* iteration 7 times. Since each frame has somoe degree of randomness associated with it, sequencing the frames will give it a cool live effect (see below).

![city_static](ezgif.com-optimize(3).gif)


## More examples

![boston](bost.png)
