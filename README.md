
# Cybersec Training Tool

The Tool helps cybersecurity (SOC) analysts become better analysts, and those preparing for CySA+ exam to be better prepared to pass it. It tests and teaches foundational background knowledge of TCP/UDP ports and acronyms. Acronyms cover a wide range of areas including security analytics, incident response, digital forensics, threat intel, software development, business, governance, risk, compliance aspects of cyber (to the extent that would be useful for a well-rounded SOC analyst). Prerequisites: knowledge equivalent to CompTIA A+, Network+, and Security+. The author's inspiration for creation of the tool was preparation for CompTIA CySA+ certification.


## Installation and Execution

The program is designed to be used on a Windows machine.

- Install Python 3.12 if not already installed (from Downloads section at python.org).
- Download a .py file and a .csv file. Save .py file in a folder of your choice. Save a .csv file in Downloads folder.
- Run a .py file using IDE of your choice, OR run it using Windows command line (navigate to directory where it is saved, then type 'python cybersec_training_tool.py'). When executed for the first time the tool will create a new folder and move a .csv file to it.
    
## Used Technologies

The tool was created with standard Python 3.12 library. It imports the following modules: time, os, shutil, random, csv, datetime.
## Current Features

- The tool greets the user and introduces itself. Then it obtains user's name and explains how the test works. It checks if 'Cybersec Training Tool' folder exists in user's home directory (and creates it on the first ever use), changes current working directory to this directory, and checks if 'ports_acronyms.csv' file is located in this directory (and moves it to this directory from Downloads folder on the first ever use). 
- It displays engaging and visually appealing initialising messages, with a timed release. It reads the contents of a csv file (containing just south of 300 items). It establishes if an item is a port (i.e. contains a digit) or an acronym. Then it randomly chooses 8 ports and 12 acronyms to create a test instance content (utilising a list). 
- It delivers a test, throws in 4 motivators at random intervals and displays half way message after the tenth question. It counts the number of correct answers, and creates a list of incorrect answers. At the end of test it displays 'end' message, then, after a countdown to the moment of truth, a user's score. It evaluates the score. 
- It creates 'results_record.csv' file, to which it writes user's name, score and date. If user has taken two or more tests, the tool calculates some stats and displays them (max. score and dates of it, number of tests taken so far, unique scores achieved so far, and average score). 
- Then it delivers a teaching component by displaying what the question was, what the answer should be, and what the incorrect answer was.
- The author's info is displayed.
- All user's input is stripped of whitespaces and converted to lower case, to minimise the risk of incorrect: scoring and/or saving results' data.


## Roadmap

- Option to skip instructions for those who have used the tool many times before.
- Adding extra definition(s) where an acronym can have more than one definition within ICT/cybersec context.
- Introducing analytical component with visualisations for performance stats.
- Adding GUI.


## Feedback

If you have any feedback, please reach out at martin.j.jasinski@gmail.com 


## Acknowledgements/References

 - [Readme editor tool](https://readme.so/editor)
 - [CompTIA CySA+ CS0-003 Exam Objectives](https://www.comptia.org/certifications/cybersecurity-analyst)
 - [Nmap's top  20 (most commonly open) TCP and UDP ports](https://nmap.org/book/port-scanning.html)
  - [CompTIA Network+ Common Ports youtube video by Professor Messer](https://youtu.be/jX1pobYmZdE?si=ZymMcwGSJ4_8gwm1)
 - Microsoft Copilot (created some docstrings)
 - CompTIA CySA+ CS0-002 Exam Objectives
 - The Official CompTIA CySA+ Self-Paced Study Guide CS0-002

## License

MIT License

Copyright (c) [2024] [Marcin Jan Jasinski]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

