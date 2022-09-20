# This code tests that your Python installation worked.
# It generates a png image file that you should upload to Canvas
# The png file will be located in the folder in which the code is run.
import scipy
import numpy
import matplotlib
import matplotlib.pyplot as plt
import platform
import socket

# If you are a student, please fill in your first and last
# names and GitHub username inside the quotes in the three lines below.  Do not
# modify anything else in this file

your_first_name = 'Aiden'
your_last_name = 'Ebner'
your_github_username = 'Ebneras'

# If you are an instructor, modify the next 3 lines.
# You do not need to modify anything else in this file.

classname = 'Foundations of Physics'
term = 'Fall_2022'      # must contain no spaces

plt.plot([0,1], 'r', [1,0], 'b')
plt.text( 0.5, 0.8, '{0:s} {1:s} {2:s}'
        .format(your_first_name, your_last_name, your_github_username),
        horizontalalignment='center',
        size = 'x-large',
        bbox=dict(facecolor='purple', alpha=0.4))
plt.text( 0.5, 0.1,
    '{1:s}\nscipy {2:s}\nnumpy {3:s}\nmatplotlib {4:s}\non {5:s}\n{6:s}'
        .format(
        classname,
        term,
        scipy.__version__,
        numpy.__version__,
        matplotlib.__version__,
        platform.platform(),
        socket.gethostname()
        ) ,
    horizontalalignment='center'
    )
filename = your_last_name + '_' + your_first_name + '_' + term + '.png'
plt.title('*** Upload the saved version of this plot to Python Assignment 0 on Canvas ***\n',fontsize=12)
plt.savefig(filename)
plt.show()

#Check successful use of np
a=numpy.sqrt(2)
print(a)