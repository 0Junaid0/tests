# Ecommerce

**Ecommerce app built in django/python**.

## How to run

1. Clone this repository  
    ```shell
    git clone https://github.com/0Junaid0/tests.git
    ```
   
2. Create a virtual environment and activate it  
    ```shell
    python -m venv .venv
    .\.venv\Scripts\activate
    ```
   
3. [Optional] Set your IDE to point to the virtual environment python.  

4. Install the requirements.  
    ```shell
    pip intall -r requirements.txt
    ```

5. Run migrations.
    ```shell
    cd cartzilla
    python manage.py migrate
    ```

6. Run the server.
    ```shell
    cd cartzilla
    python manage.py runserver
    ```
