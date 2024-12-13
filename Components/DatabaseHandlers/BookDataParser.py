from ..ContextManager import RequestContextManager
from ..DatabaseQueries import BOOK_HANDLER_QUERIES
from mariadb import Error
from math import ceil

class BookDataParser:
    def build_search_filter(self, filter_term, search_term):
        print(f"Filter Term: {filter_term}, Search Term: {search_term}")
        if not search_term or not filter_term:
            return "", []
        filters = {
            "acc_num": "access_number",
            "call_num": "call_number"
        }
        filter_by = filters.get(filter_term, filter_term)
        return f"WHERE {filter_by} LIKE %s", [f"%{search_term}%"]
        
    def parse_book_insertion_data(self, book_data):
        book_array = []
        for book in book_data:
                book_array.append((
                    book['access_number'],
                    book['call_number'],
                    book['title'],
                    book['author'],
                    book['status'],
                    book['qr_code_path']
                    )
                    )
        return book_array
    
    def parse_book_update_data(self, book_data):
        book_array = []
        for book in book_data:
                book_array.append((
                    book['access_number'],
                    book['call_number'],
                    book['title'],
                    book['author'],
                    book['status'],
                    book['id'])
                    )
        return book_array
        
    def delete_books(self, book_ids):
        try:
            book_ids_tuple = [(book_id,) for book_id in book_ids]
            with RequestContextManager() as cursor:
                cursor.executemany(BOOK_HANDLER_QUERIES.DELETE_BOOK, book_ids_tuple)
                return {"success": True, "message": f"{cursor.rowcount} books deleted successfully."}
        except Error as err:
            return {"success": False, "message": f"Error: {err}"}