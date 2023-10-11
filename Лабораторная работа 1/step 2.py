# TODO Найдите количество книг, которое можно разместить на дискете
disk_size_Mb = 1.44
number_of_pages = 100
number_of_rows = 50
number_of_symbols = 25
symbol_size = 4
disk_size = disk_size_Mb * 1024 * 1024
number_of_all_symbols = number_of_pages * number_of_rows * number_of_symbols
book_size = symbol_size * number_of_all_symbols
number_of_books = int(disk_size//book_size)
print("Количество книг, помещающихся на дискету:", number_of_books)
