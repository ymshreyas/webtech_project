# Introduction
Accessing investment opportunities is hindered by complex and inaccessible data from financial institutions. Limited accessibility to insights, often tied to brokerageaffiliations, poses a significant barrier for the general public. This lack of transparencyrestricts individuals' ability to make informed investment decisions, perpetuating adisparity in wealth accumulation and hindering financial inclusivity. Efforts todemocratize access to financial data and insights are crucial for leveling the playing field and empowering individuals to participate more effectively in the investment landscape.

# Objective
The website's primary objective is to democratize access to financial insights by providing free technical analysis and plots on stock market data. It aims to bridge the educational gap for traders of all levels, offering comprehensive learning resources from basic concepts to advanced strategies. Real-time market data accessibility enhances the relevance of content and fosters practical understanding. By offering these resources for free, the platform promotes financial inclusivity, breaking down barriers to entry and empowering a diverse community of investors. It seeks to instill confidence by enabling users to make informed decisions independently, reducing reliance on biased information sources. Ultimately, the initiative aims to create a more informed, diverse, and resilient community of investors prepared to navigate market fluctuations confidently.

# Techstack used
## Front End
1) HTML
2) CSS
3) Bootstrap
## Middleware
1) Django
## Backend
1) MongoDB Atlas
2) Plotly

# Implementation
## Front End
1) Writing HTML, CSS code to create the user interface (UI) of Stock Market Technical Analysis
2) Implementing user interactions, such as form submissions, and button clicks.

## Back End
1) Backend Development include creating models to store data in the database, views to display the html pages and URL patterns for integrating all the web pages and mapping them accordingly.
2) It also includes creating APIs (Application Programming Interfaces) to handle requests from the frontend and perform operations such as data retrieval, manipulation, and storage.
3) The data collection process from NSEDT API involves retrieving real-time stock market data, including price, volume, and other relevant metrics. After obtaining the data, a batchification process is implemented to organize it into manageable segments for efficient processing. This involves grouping the data into batches based on specified parameters, such as time intervals or stock symbols. Batchifying enables streamlined analysis and facilitates parallel processing, optimizing computational efficiency.

## Database Configuration
1) MongoDB Atlas is a cloud database where data will be stored in one central database and they can be retrieved from remote devices connected to it.
2) The models are defined to represent the tables in the database. In this projects, models such as user_info and plot_info are created in the form of classes and they are stored in a file named ‘models.py’.Setting up logging to record system events, errors, and user actions for troubleshooting and auditing purposes.
3) Django contains an inbuilt feature to create the tables in the database that are defined in models.py file by running ‘python manage.py makemigrations’ and ‘python manage.py migrate’ commands.

## Implement templates, media and views
1) Create Views : Different views have been created using functions to handle different functionalities such as ‘signup’, ‘user_login’, ‘generate’, etc. These views handle user requests, retrieve data from database and render appropriate templates.
2) Create template directory : Template directory is created to store all the html files called as templates and Django’s template language is used to dynamically data and handle form submissions.
3) Create Media directory : Media directory is created to store all the images and files that are provided by the user during registration and they are retrieved accordingly.
4) Setting up Templates and media directory : These directories are setup in the settings.py file by joining them with the ‘BASE’ with the help of ‘os.path.join’ command.

## Configure URL Patterns
1) Setting up urls.py file : urls.py will be created during the creation of the project in which URL patterns are configured using ‘path’ function and they are mapped to appropriate views.
2) Some of the URL patterns are ‘admin/’, ‘signup/’, ‘plot_generate/’, ‘complaints/’, ‘first_page/’, etc.

## Project Working
1) Upon running the server, the landing page arrives where the user can see interactive plots which gives an idea about how the plots might look.
2) User can register by giving their email address and password, they can login and generate variety of plots by choosing the analysis type, period, scrip code, price lines, start date and end date.
3) The user will have the privilege to download the generated plot, concentrate on specific period by shortening the entire period, etc.
4) The plot history will be stored in the user’s home page for future reference.

# Results
![image](https://github.com/ymshreyas/webtech_project/assets/123388366/091e16b7-47e1-40ec-a4e5-41e4acb06910)
![image](https://github.com/ymshreyas/webtech_project/assets/123388366/6dfe203b-e780-44b9-bcf5-80142d878572)
![image](https://github.com/ymshreyas/webtech_project/assets/123388366/d28edc3c-ed35-4bc6-92d1-9c9069583f4f)
![image](https://github.com/ymshreyas/webtech_project/assets/123388366/eb0115e1-46b7-4c72-b87e-077e069e3b44)
![image](https://github.com/ymshreyas/webtech_project/assets/123388366/3efe06d5-389e-48c4-a55d-288a12036544)
![image](https://github.com/ymshreyas/webtech_project/assets/123388366/12e3f7a4-ddc5-4e84-be87-20f3425d4152)
![image](https://github.com/ymshreyas/webtech_project/assets/123388366/b8e240b4-7c4a-47a0-8e0e-39ef968ecce2)






