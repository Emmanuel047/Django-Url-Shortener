URL SHORTENER Made in DJANGO
Tech Stack 
DJANGO - Backend
Html, CSS, Frontend

# Clone & Setup
git clone https://github.com/Emmanuel047/Django-Url-Shortener.git
cd url-shortener
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver