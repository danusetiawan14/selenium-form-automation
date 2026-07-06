from src.config import APP_NAME, VERSION

def show_banner():
    print("=" * 60)
    print(APP_NAME.center(60))
    print("=" * 60)
    print("Author  : Danu Setiawan")
    print(f"Version : {VERSION}")
    print("GitHub  : github.com/danusetiawan14")
    print("=" * 60)