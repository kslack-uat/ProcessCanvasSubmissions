## ProcessCanvasSubmissions.py
## Written by: Kent Slack
## 1/11/2018

## Rearranges code submissions downloaded from Canvas into a form that can be analyzed.

from builtins import input
import os
import shutil
import zipfile
import time


languages_map = {'1':'python3','2':'java17','3':'c/c++','4':'c#-1.2','5':'text','6':'text'}


# Prepare a set of assignments downloaded from Canvas for analysis with the tool.
def ProcessCanvasSubmissions():

    directory_or_file = input('What file/directory would you like to prepare for analysis? ')
    directory_to_process = CheckDirectorOrFile(directory_or_file)
    language = SelectLanguageOrProcess()

    if language == '6':
        change_file_extension = True
    else:
        change_file_extension = False

    for file in os.listdir(directory_to_process):
        student_identifier = file.split('_')[0]
        CreateSubDirectoryStructure(student_identifier,directory_to_process)
        relocated_file = ModifyFileLocation(directory_to_process, file)
        file_extension = DetermineFileExtension(relocated_file).lower()
        if file_extension in '.zip':
            UnzipFile(relocated_file, DetermineFilePath(relocated_file))
        if file_extension in ['.rar','.tar.gz','.gz','.bz2','.7z']:
            print('***Unable to automatically process archive ' + str(relocated_file) + '.')
            input('Manually extract the files, and then press any key to continue.')
        if change_file_extension:
            ChangeFileExtension(relocated_file, '.txt')


# Determines if a file or directory has been specified. If it is a zip file, then decompress it.
def CheckDirectorOrFile(directory_or_file):
    if os.path.isdir(directory_or_file):
        return directory_or_file
    if os.path.isfile(directory_or_file):
        if zipfile.is_zipfile(directory_or_file):
            unzip_directory = directory_or_file.replace('.zip','\\')
            os.mkdir(unzip_directory)
            UnzipFile(directory_or_file,unzip_directory)
            return unzip_directory

    raise ValueError(str(directory_or_file) + ' is not a zip file or directory. Please re-run and either specify a directory or a valid zip file.')


# The user specifies the language used to program and thereby analyze the source code.
def SelectLanguageOrProcess():
    print('Select the programming language of the files or the process you would like to complete.')
    print('\t(1) Python')
    print('\t(2) Java')
    print('\t(3) C/C++')
    print('\t(4) C#')
    print('\t(5) Text (the format is already .txt')
    print('\t(6) Generic Language - Rename to Text')
    print('\t(7) Only restructure the files (create a subdirectory for each student), do not run tool automatically.')
    return input('Specify Option and Press Return: ').strip()



# Extracts the student name from the students compressed submission
# Canvas assignments are downloaded in the form studentName_courseNumber_assignmentNumber_assignmentTitle.fileExtension
def DetermineSubdirectory(filename):
    return filename.split('_')[0]


def DetermineFileExtension(filename):
    root, file_extension = os.path.splitext(filename)
    return file_extension.strip()


def DetermineFilePath(filename):
    root, file_extension = os.path.splitext(filename)
    return root


def CreateSubDirectoryStructure(subdirectory_to_create, root_directory):
    os.mkdir(root_directory + '\\' + subdirectory_to_create)


# Moves the student's work to the subdirectory that was recently created for it.
def ModifyFileLocation(root_directory, filename):
    new_file_location = root_directory + '\\' + DetermineSubdirectory(filename) + '\\' + filename
    shutil.move(root_directory + '\\' + filename, root_directory + '\\' + DetermineSubdirectory(filename) + '\\' + filename)
    return new_file_location


def UnzipFile(file_to_unzip, unzip_directory):
    if not zipfile.is_zipfile(file_to_unzip): return

    with zipfile.ZipFile(file_to_unzip,'r') as zip:
        zip.extractall(os.path.dirname(unzip_directory))


def ChangeFileExtension(file,new_extension):
    renamed_filename = file.replace(DetermineFileExtension(file),'.txt')
    os.renames(file,renamed_filename)
    return renamed_filename


if( __name__ == "__main__"):
    #ProcessCanvasSubmissions()
	#runtime = timeit.timeit(ProcessCanvasSubmissions())
	start_time = time.clock()
	ProcessCanvasSubmissions()
	end_time = time.clock()
	print("Runtime was " + str(end_time - start_time))
