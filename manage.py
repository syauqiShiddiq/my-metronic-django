#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import mimetypes # <--- 1. TAMBAHKAN IMPORT INI

def main():
    """Run administrative tasks."""
    
    # <--- 2. TAMBAHKAN BLOK KODE INI UNTUK MEMPERBAIKI WINDOWS REGISTRY ---
    # Memaksa Windows mengakui CSS sebagai CSS, bukan Text biasa
    mimetypes.init()
    mimetypes.types_map['.css'] = 'text/css'
    mimetypes.types_map['.js'] = 'application/javascript'
    # ---------------------------------------------------------------------

    # Pastikan ini menunjuk ke development settings Anda
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metronic_project.settings.development')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()