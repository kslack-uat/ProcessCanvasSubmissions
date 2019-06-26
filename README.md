# ProcessCanvasSubmissions

This program is designed to prepare student submission files from the Canvas LMS for analysis. The structure of the files needs to be very specific for the analysis software to work, so this script automates the restructuring process. It creates a folder for each students submission so they can be compared.

<h2>Required Libraries</h2>
<ul>
<li>os</li>
<li>shutil</li>
<li>zipfile</li>
<li>time</li>
</ul>

If any of the above libraries are missing, you can install them using pip. To use pip, open your commandline or terminal and type pip install name_of_the_library.

<h2>Example Submissions</h2>
The submissions.zip file found in the repository contains some simple testing data that can be used to determine if the script works.
<h3>Starting State</h3>
A directory that contains a zip file with each student's submission.
OR
A zip file that contains a zip file for each student.
<h3>Ending State</h3>
A directory for each student (with their name or id) that contains all of their source code and submitted files.

<h2>Profiling the Project</h2>
The runtime of the project can be measured using python's profiler. To execute the profiler on this source code, run the program using the following command from the terminal or commandline:<br/>
<i>python -m cProfile ProcessCanvasSubmissions.py</i><br/>
Note, you should be in the directory where ProcessCanvasSubmissions.py exists for this to work.
