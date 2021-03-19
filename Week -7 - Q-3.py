### All Rights Reserved ###

#Copyright (c) ${mailusername.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.


# ###########
# Write a program that list according to email addresses without email domains in a text.
#
# Example:
#
# Input:
#
# The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com.
# Then New Yorker article on wind farms...
#
# Output :
#
# franky
#
# sinatra123

import re

with open('mailtext.txt', 'r', encoding="utf-8") as file:
    text = file.read()
    # pattern = r'\S+@'
    pattern = r'[a-z|A-Z|0-9]+[\._]?[a-z|A-Z|0-9]+[@]'
    lst = re.findall(pattern, text)
    new_lst = []

    for i in range(len(lst)):
        new_lst.append(lst[i][:-1])
        print(new_lst[i])
 
###########
### All Rights Reserved ###

#Copyright (c) ${mailusername.2021} ${Ozkan TOPRAK}

#Created by InfotecAcademy

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
