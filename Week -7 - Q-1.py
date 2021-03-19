### All Rights Reserved ###

#Copyright (c) ${HiddenIDFinder.2021} ${Ozkan TOPRAK}

#Created by InfotechAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

#################################
# Write a program that detects the ID number hidden in a text.
# We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit
# (For example: AA4ZA11B1). 9digit total!?
#
# Input : AABZA1111AEGTV5YH678MK4FM53B6
#
# Output : MK4FM53B6
#
# Input : AEGTV5VZ4PF94B6YH678
#
# Output : VZ4PF94B6

import re

def in_out():
    with open('hiddenID.txt', 'a', encoding="utf-8") as file:
        text = file.read()
        pattern = r'\w{2}\d\w{2}\d{2}\w\d'
    return print('Founded hidden ID list: ', re.findall(pattern, text))


def findhiddenID():
    with open('hiddenID.txt', 'r', encoding="utf-8") as file:
        text = file.read()
        pattern = r'\w{2}\d\w{2}\d{2}\w\d'
    return print('Founded hidden ID list: ' ,re.findall(pattern, text))


findhiddenID()


####################
### All Rights Reserved ###

#Copyright (c) ${HiddenIDFinder.2021} ${Ozkan TOPRAK}

#Created by InfotechAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
