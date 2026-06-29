from dotenv import load_dotenv
import os



def print_author():

  load_dotenv(dotenv_path = '.env')
  author = os.getenv('author')
  print(f"Автор проекта: {author}")

AUTHOR = print_author()



