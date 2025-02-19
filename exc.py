import sosa

sosa.register_user('user1', '山田太郎')
sosa.register_book(9784772611534,1)
sosa.update_user('user1', '山田花子')
sosa.update_book(9784772611534, 10)
sosa.register_book(9784297110116,1)

sosa.search_users()
sosa.search_books()

sosa.delete_book(9784297110116)
sosa.register_user('user2', '鈴木次郎') 
sosa.delete_user('user2')

sosa.rent_book('user1', 9784772611534)
sosa.search_rent_books()
sosa.return_book('user1', 9784772611534)
sosa.search_rent_books()


    