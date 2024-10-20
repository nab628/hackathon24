# Lehigh-Valley-Hackathon

Our project is a website that allows students to access textbooks at a much more affordable cost. Although Lehigh has the Learning Unlimited system for $375, there are students students who find this unaffordable and unreasonable. Furthermore, some classes don't requrire textbooks so this cost of $375 would simply be unnecessary. 

The website has two users, users who are looking to upload textbooks, and others who are looking to access textbooks. It prompts users to log in with their Lehigh.edu email, making the website only accessible to Lehigh students. Following that, they are prompted whether they are  looking to access a textbook or upload a textbook. Uploaders then are taken to a page in which they can import their textbook file, the class the textbook is used for, and any other additional information they think may be helpful. We plan to use some sort of database to store all of these inputs in. The people that are looking to access the textbooks should be prompted to the home page in which they will enter the specific class they are looking for, or the textbook name, and related search results could pop up. 

To create this website, we utilized Flask to create a Python-based website. We also used the SQL Alchemy library to have a SQL database for storage of textbooks information. SQL Alchemy is an object relational mapper that essentially translates a Python statement into a SQL query.

To operate this, create a python virtual environment, install flask and SQL Alchemy, and run app.py.
