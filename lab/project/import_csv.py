import os
import django
import pandas as pd	
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings') 
django.setup()
from news.models import Article

def import_csv():
    data = pd.read_csv('D:\\Lessons\\Django\\lab\\project\\text.csv', delimiter=';')
    for row in data.iterrows():
        Article.objects.create(
            title=row['title'],
            keywords=row['keywords'],
            annotation=row['annotation'],
            rubNum_id=row['rubNum']
            )

if __name__ == "__main__":
    import_csv()