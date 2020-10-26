To enable search functionality:

- Virtual Table needs to be created once:
	- 	[Using sqlite3 python module]

		con = sqlite3.connect("db.sqlite3")
		con.execute("CREATE VIRTUAL TABLE search_song USING FTS5 (id, name, album_name, album_id, genre_name, genre_id, artist_name, artist_id);")

	- 	[Using DB Shell]
		sqlite> CREATE VIRTUAL TABLE search_song USING FTS5 (id, name, album_name, album_id, genre_name, genre_id, artist_name, artist_id);

- Batch add songs to the virtual table, forming search tokens post stemming:

	>>> insert_statement = "insert into search_song (id, name, album_name, album_id, genre_name, genre_id, artist_name, artist_id) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');"
	>>>
	>>> script = ''''''
	>>>
    	>>> for song in Song.objects.all():
    		for genre in song.genres.values('id', 'name'):
		    for artist in song.artists.values('id', 'name'):
    	          	script += str(insert_statement % (song.id, song.name, song.album.name, song.album.id, genre['name'], genre['id'], artist['name'], artist['id']))
