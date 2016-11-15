# djangovue
simple project to connect django as a backend and vue-cli as frontend and vue-material by [@marcosmoura](https://github.com/marcosmoura/vue-material)

# how to use
1. clone repo
2. setup backend
    * open backend
        ```bash
        $ cd backend
        ```
    * create virtualenv
        ```bash
        $ virtualenv env
        ```
    * activate virtualenv
        ```bash
        $ env\Script\activate        
        ```
    * install all requirements
        ```bash
        $ pip install -r requirement.txt
        ```
    * migrate and create superuser
        ```bash
        $ python src\manage.py migrate
        $ python src\manage.py createsuperuser
        ```
    * make migration for todos apps    
        ```bash
        $ python src\manage.py makemigrations todos
        $ python src\manage.py migrate
        ```
    * run server
        ```bash
        $ python src\manage.py runserver
        ```
    * fire admin panel to add more todolist
        [localhost:8000/admin](https://localhost:8000/admin) and 
        [localhost:8000/api/todos](https://localhost:8000/api/todos)
        
3. setup frontend
    * open frontend dir (open it in separated terminal)
        ```bash
        $ cd frontend
        ```
    * install all dependencies
        ```bash
        $ npm install 
        ```
    * start local server development
         ```bash
        $ npm run dev 
        ```
    
    