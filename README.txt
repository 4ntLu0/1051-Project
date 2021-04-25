Milestone 3, EAAA. Simple Interactive Photo Editor (SIPE)
Release: 1.0.0 Nov 1, 2019 by Fall 2019 ECOR 1051 Group L2_5
Team Leader: Anthony Luo, #101145222
Contact: a26luo@uwaterloo.ca (outdated -> anthonyluo4@cmail.carleton.ca)

DESCRIPTION
----------------------------------
This interactive photo editing program enables users to retouch images by applying a variety of filters in a cumulative manner.

INSTALLATION
----------------------------------
Installation requires:
    1) CIMPL Version 1.04 (October 6th, 2017)
    2) Pillow 6.1.0
    3) Python 3.7
- Ensure that CIMPL is located within the same folder as L2_5_image_filters.py and L2_5_interactive_ui.py
- Ensure that Pillow is downloaded and installed correctly. Documentation for this process can be found at pillow.readthedocs.io
- Ensure that Python is correctly installed. Documentation for this process can be found at python.org

USAGE
----------------------------------
- Run L2_5_interactive_ui.py
- [insert shell commands and not images]
- It is recommended that you load an image file before attempting to apply a filter. (Input the letter 'L')
- When loading an image, the filename.jpg must be indicated.
- If applying the Two Tone, Three Tone, Edge Detection or Improved Edge Detection Filters, additional input is required. 
- Users must enter input that corresponds to the options displayed in the menu
- Once the filter is applied, the new image might take several seconds to appear depending on the size of the image that was loaded. Please be patient. 
- Filters will be applied cumulatively.
- The final image will be saved to filepath.jpg

CREDITS
----------------------------------
Authors of Functions:
detect_edges - Alia Nichol
detect_edges_better - Anthony Luo
flip_horizontal - Abdelrahman Alatoom
flip_vertical - Emilio Lindia
posterize - Emilio Lindia
sepia - Anthony Luo
three_tone - Abdelrahman Alatoom
two_tone - Abdelrahman Alatoom
extreme_contrast - Alia Nichol
interactive program - Anthony Luo, Alia Nichol, Emilio Lindia

LICENSE
----------------------------------
MIT License

Copyright (c) 2019. Team "EAAA"

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files "L2_5_image_filters.py" and 
"L2_5_interactive_ui.py", to dealin the software without restriction, including 
without limitation the rights to use, copy, modify, merge, publish, distribute, 
sublicense, and/or sellcopies of "L2_5_image_filters.py" and "L2_5_interactive_ui.py",
and to permit persons to whom "L2_5_image_filters.py" and "L2_5_interactive_ui.py" 
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of "L2_5_image_filters.py" and "L2_5_interactive_ui.py".

THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.





