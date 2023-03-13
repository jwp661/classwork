#!/usr/bin/env python
# coding: utf-8

# # 📝Logistics and Final Exam
# 
# We are rapidly approaching the Final Exam!

# ## Final Exam Information
# 
# ### Final Exam 
# 
# **TIME CHANGE**: 10:30 am -12:30 pm March 20, 2023
# 
# **Location**: Main Auditorium & PISB 106 - In the near future, we will send instructions regarding who should attend which location.

# ### Exam Structure
# 
# **Make certain to read these instructions in detail**
# 
# The final exam will have two computerized parts: 
# 

# 
# 1. Part 1 (30%): A Drexel Learn-based conceptual examination. This will be similar in structure to the midterm exam. We will only cover problems of types 1, 2, and 3 of the practice midterm. These questions will cover the topics throughout the entire term. 
# 

# 
# 2. Part 2 (70%): A practical coding exam. 
# * This will be a practical exam similar in structure to Lab 10 - **making sure you understand all concepts used to complete Lab 10 will be the best way to study for the Final**.
# 

# * The lab will be a jupyter notebook which you will complete live during the examination period. 
# 

# * We will provide you with a pdf version of the exam questions and documentation at 8 am on Friday March 17, 2023. You will not be able to use the autograder functions for your practice. 

# The instructors will not be answering specific questions about code for the final exam. You can ask general conceptual coding questions or clarification questions about the questions or the documentation provided.
# 

# * For the exam you will only be allowed to work within a jupyterhub. This means you are not allowed to use search engines, ChatGPT, or any other resource not available in native jupyterhub. 
# 

# * You can, and should, refamilarize yourself with how to view documentation within jupyterhub. This is allowed and will help you on the exam. 
# 

# * The exam will make use of the autograder. This will provide line-by-line feedback to assess your completion of tasks throughout the exam. We will be using the same tests to grade your exam, thus you will have transparency regarding your score. Furthermore, this will mitigate simple mistakes.
# 

# * The python instance will have all packages pre-installed - or you will be provided with code in the jupyter notebook which when run will install all required packages. 
# 

# In[1]:


import matplotlib.pyplot as plt

get_ipython().run_line_magic('pinfo2', ' plt.plot')


# ### Technology and Logistics
# 
# **Computing Platform**
# 
# * Our JupyterHub will not support all students in the class. Prior to the exam it is your responsibility to setup a codespaces account. Please see the instructions. We will be testing codespaces in lab this week. We would recommend that you try and setup your codespaces account prior to Lab.
# 

# 
# * We will be requesting that you use Zoom to record your screen during the entirety of the exam. 
#     - We will expect that you demonstrate that you have closed all other open software besides a private web browser. 
#     - Your browser window should be maximized to fill the screen throughout the entire exam, and your clock should be visible.
#     - If you have an issue with your screen sharing or recording, you need to immediately notify a instructor.
#     - With the final assignment there is a log file that is required for grading. You will need to turn this in with your completed notebook.
#     - The log file and Jupyter Notebook will be turned in on Drexel Learn. You should record the entire process of turning in the Jupyter Notebook and log file.
#     - The video file once complied will need to be uploaded to a shared Microsoft OneDrive folder. We note that a two-hour Zoom recording takes approximately 40 minutes to compile and 10 minutes to upload. We would recommend that you remain in the exam room until your compression is complete or your files are uploaded. If you encounter an error while in the exam room, we can address your technological challenges. If you choose to leave the examination room, it is your responsibility to ensure the video is received by 5 pm. We will do our best to provide support for students who decide to leave the exam room; however, we can not make any promises that we will be able to resolve the issues. 
#      - The video file should follow the naming convention FirstName_LastName_StudentIDNumber_ENGR131_FINAL. Failure to comply runs the risk that your video is not accepted.
#      - If you fail to turn in a video recording (without an approved exception) or if the video recording does not include your screen capture the maximum grade you can receive is a **50\%** on the final.
#     - If you do not turn in the log file `output.log` or your notebook in `.ipynb` format, your exam will be unable to be graded.
#     - It goes without saying that any evidence of intentional deviation from the exam procedures will be reported as outlined in the [Academic Integrity Conduct Process](https://drexel.edu/studentlife/community-standards/code-of-conduct/academic-integrity-policy/conduct-process)
# 
#     - There will not be a makeup exam except for students with a University-excused absence. Missing the exam without a University-excused absence will result in a 0 on the final exam.

# 
# 
# **Computer Preparation**
# 

# 
# We expect that you have a tested plan in place prior to the exam to meet the computing requirements. The next two labs will follow these guidelines as practice for the final exam. 
# 

# 
# * A computer with a sufficiently charged battery for 3 hours of use with recording. We will have limited access to power outlets. It will be the students responsibility to ensure they manage their laptops power. If a laptop reaches 25% power during the exam it is the students responsibility to notify the instructor. 
# 

# * Your computer must have Zoom with recording capabilities and a modern web browser. We recommend microsoft edge, firefox, google chrome, or safari.
# 

# * Your computer must have sufficient hard drive space to store a 2 hour video. We recommend having at least 5 GB of free space on your computer. 
# 

# * Your computer must have the ability to connect to the network over WiFi
# 

# * Your computer must run MacOS, Windows, or Linux. Chromebooks and IPads are not sufficient.
# 

# 
# If you have concerns about your access to an acceptable computing platform for the final exam it is your responsibility to inform the instructors by email at [engr131.w23@drexel.edu](mailto:engr131.w23@drexel.edu) at least 1 week prior to the exam. If you fail to notify us within this timeline we will do our best to accommodate your needs, however, cannot ensure access to resources to take the exam. 
# 
# 
# 
# 
# 
