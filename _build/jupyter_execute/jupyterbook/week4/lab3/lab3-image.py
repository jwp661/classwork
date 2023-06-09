#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Initialize Otter
import otter
grader = otter.Notebook("lab3-image.ipynb")


# # 🧪🖥 Lab 3: Image Processing
# 
# This lab explores basic image processing in Python.
# 
# 

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np


# **Loading and viewing Images** 
# 
# The matplotlib.pyplot module, which has been imported, can be used to load and view images. The following code loads an image called ```"bird.jpeg"```, scales it to have floating point pixel values from 0 to 1 (instead of 0 to 255), and stores it in a variable called ```img```. Make sure the provided ```bird.jpeg``` file is in the same directory as this notebook.

# In[ ]:


img = plt.imread("bird.jpeg").astype("float") / 255


# To view the image, we can use plt.imshow()

# In[ ]:


plt.imshow(img);


# This image is represented in Python as a 3 dimensional array with dimensions ($H$, $W$, $C$), where 
# 
# <center>
# 
# $H$ = height
# 
# $W$ = width
# 
# $C$ = number of color channels
# 
# </center>
# 
# 
# To view the dimensions, we can print the img array's "shape" as below:

# In[ ]:


print(img.shape)


# From this, we can see that this image has a height of 854 pixels, a width of 1000 pixels, and 3 color channels. The 3 color channels represent the red, green, and blue components of an image. The color of each pixel in the full color image is determined by its RGB components. 
# 
# The following code lets us extract the three separate color channels from the image. We store these color channels – each with dimensions ($H$,$W$) – in variables `R`, `G`, and `B`.

# In[ ]:


# For red, get the contents of the image at color channel index 0
R = img[:,:,0]

# For green, get the contents of the image at color channel index 1
G = img[:,:,1]

# For blue, get the contents of the image at color channel index 2
B = img[:,:,2]


# We can view the 3 color channels individually like this:

# In[ ]:


# create a plot containing 3 subplots
figure, plots = plt.subplots(ncols=3, nrows=1)

### plotting the red component
# start with an empty image array of zeros
r_img = np.zeros(img.shape)
# populate the image with the red color channel data from img
r_img[:,:,0] = R
# plot the red component image
plots[0].imshow(r_img)
# turn off the axis to make the plot look tidy
plots[0].set_axis_off()

### plotting the green component
# start with an empty image array of zeros
g_img = np.zeros(img.shape)
# populate the image with the green color channel data from img
g_img[:,:,1] = G
# plot the red component image
plots[1].imshow(g_img)
# turn off the axis to make the plot look tidy
plots[1].set_axis_off()

### plotting the blue component
# start with an empty image array of zeros
b_img = np.zeros(img.shape)
# populate the image with the blue color channel data from img
b_img[:,:,2] = B
# plot the red component image
plots[2].imshow(b_img)
# turn off the axis to make the plot look tidy
plots[2].set_axis_off()


# **Task 1: To Black and White** 
# 
# Your task is to write a function that computes a black and white version of an image. A black and white (or grayscale) image has equal values for its $R$, $G$, and $B$ components. One way to create a black and white version of a color images, that we will use in this lab, is to average the three color components. The new components `newR`, `newG`, and `newB` would be computed as follows.
# 
# <center>
# 
# `newR` = `newG` = `newB` = $\frac{1}{3} $ (`R` $ + $ `G` $ + $ `B` $)$
# 
# 
# </center>
# 
# Hint: Numpy arrays of equal size can be added, subtracted, multiplied, etc. as if the were numbers. For instance, two arrays of equal dimensions `a` and `b` can be added pixel-by-pixel with the single line:
# 
# <center>
# 
# `a` + `b`
# 
# </center>
# 
# Write python code to do the following:
# 
# * Define a function called ``to_bw`` which accepts as input a single argument, `I`, an array containing a color image.
# * In the function, first extract the red, blue, and green color components of the image. (You may replicate how this was done above.)
# * Compute the new components `newR`, `newG`, and `newB`, from `R`, `G`, and `B` using the equation above.
# * Create an array of zeros called `bwI` and give it the same shape as the input array `I`.
# * Populate the color channels of `bwI` to have the color components `newR`, `newG`, and `newB`.
# * Return the grayscale image `bwI`
# 
# Hint: If you have a numpy array `X` and you want to create an array of zeros that has the same shape as `X`, do the following:
# ```np.zeros(X.shape)``` 
# 
# Your code replaces the prompt:  `...`
# 

# In[ ]:


...


# In[ ]:


grader.check("task1-toBW")


# View your black and white image:

# In[ ]:


plt.imshow(to_bw(img));


# **Task 2: To Sepia Tone** 
# 
# Sepia toning is a chemical process used in photography which gives an image a brownish coloring. Image editing software can approximate the effect of sepia toning using the given set of equations.
# 
# <center>
# 
# `newR` =  0.393 `R` + 0.769 `G` + 0.189 `B`
# 
# `newG` =  0.349 `R` + 0.686 `G` + 0.168 `B`
# 
# `newB` =  0.272 `R` + 0.534 `G` + 0.131 `B`
# 
# </center>
# 
# Finally, any resulting pixel values `> 1.0` get assigned a value of `1.0`.
# 
# 
# Write python code to do the following:
# 
# * Define a function called ``to_sepia`` which accepts as input a single argument, `I`, an array containing a color image.
# * As before, first extract the red, blue, and green color components of the image.
# * Compute the new components `newR`, `newG`, and `newB`, from `R`, `G`, and `B` using the set of equations above.
# * Create an array of zeros called `sepiaI` and give it the same shape as the input array `I`.
# * Populate the color channels of `sepiaI` to have the color components `newR`, `newG`, and `newB`.
# * For any values in the resulting image greater than $1$, replace them with the value $1$ 
# * Return the sepia tone image `sepiaI`
# 
# Hint: Use `np.where(sepiaI > 1.0)` to get the indices in the sepia image where the value is greater than 1.
# 
# 
# Your code replaces the prompt:  `...`
# 

# In[ ]:


...


# In[ ]:


grader.check("task2-sepia")


# View your sepia tone image:

# In[ ]:


plt.imshow(to_sepia(img));


# **Task 3: Cropping** 
# 
# It can be helpful to crop an image to make its size smaller and focus around an object of interest. Some AI image classification systems require training data that is cropped to a square region of interest.
# 
# In this problem your task is to crop the black and white image of the bird so that it is a square image centered around the bird. Specifically, you should crop a $601$ x $601$ square centered around the pixel with $(x,y)$ coordinates $(565,375)$. Note: The point $(0,0)$ is the top left of the image, and $y$ coordinates increase towards the bottom.
# 
# Write python code to do the following:
# 
# * Determine the desired range of $x$- and $y$-coordinates to crop
# * Use array slicing to crop the black and white bird image and store it in a variable called `bw_bird_cropped`.
# 
# Hint: The code `I_crop = I[y1:y2+1,x1:x2+1]` crops image `I` between $x$ bounds [`x1`,`x2`] and $y$ bounds [`y1`,`y2`] and stores the resulting image in a variable called `I_crop`.
# 
# 
# Your code replaces the prompt:  `...`
# 

# In[ ]:


...


# In[ ]:


grader.check("task3-cropping")


# Let's view the cropped image.

# In[ ]:


plt.imshow(bw_bird_cropped);


# **Task 4: Processing your own image** 
# 
# In this final task, you will load your own image and process it as if it were an input in an AI image classification network. You will choose an image relevant to your area of engineering, filter it to be black and white, and perform a square cropping around a region of interest. 
# 
# Write python code to do the following:
# 
# * Load an image of your choosing and store it in a variable called `my_img`
# * Store a black and white version of the image in a varialbe called `bw_my_img`
# * Store a cropped version of the black and white image in a variable called `bw_my_img_cropped`
# * Your crop should be square of an appropriate size, centered around the region of interest.
# 
# Hint: You will need to upload your image so that it is in the same directory as this notebook.
# 
# 
# Your code replaces the prompt:  `...`
# 

# In[ ]:


...


# In[ ]:


grader.check("task4-own-image")


# View your cropped image:

# In[ ]:


plt.imshow(bw_my_img_cropped);

