# Music Rack

Django web application for sorting your music library.

## Requirements
Have python 3.10 or higher and Django installed. See https://docs.djangoproject.com/en/5.2/intro/install/

## Usage

- Git clone the repository
- python manage.py runserver
- Use the upload file command to upload your song file to the site:

`python manage.py uploadfile --file <song file path>`

- Go to http://127.0.0.1:8000/admin/login/ and login with:
```
user: admin
password: password
(This is only for local use so security is not a concern)
```
- If you have already added any data, uploading a file will only add missing items, it will not overwrite or delete existing data.
- Then on the left sidebar under Data you can click of Albums, Artists or Songs to view them.
- Clicking on a specific Artist lets you edit it and it's Albums
- Clicking on a specific Album lets you edit it and it's Songs
- Within each data page there is a search bar that searches based on information in all columns.
- You can also add items (using the +Add button) and delete items (using the Action dropdown menu)
- Deleting an Album deletes all songs belonging to it.
- Deleting an Artist deletes all Albums belonging to it (and therefore all songs belonging to the Artist).

## Assumptions
 - The song file is in the correct format:
    - No empty lines
    - Each row's id must be unique for all rows of all types
    - Each Artist row must contain it's id, name and genre. The genre must not contain any digits (this is how Music Rack identifies it as an artist).
    - Each Album row must contain it's id, name and year released. The year released must be a 4 digit number (this is how Music Rack identifies it as an album).
    - Each Song row must contains it's id, name and length. An row that is not an Artist or Album is assumed to be a song.
    - All rows below an Artist (and above the next Artist) are assumed to be the Artists albums and songs.
    - All song rows below an Album (and above the next Album) are assumed to be in the Album.
    - A song must belong to an Album and an Album must belong to an Artist. So the file can't have a Song row with an Album and Artist row first.
    - For example the row ordering can be:

 ```
 Artist 
    Album
        Song
    Album
        Song
        Song
        Song
Artist
    Album
    Album
Artist
Artist
```

## Testing

Run `python manage.py test data` to run all tests.

## Limitations

- Tests should clean up after themselves (specifically deleting test files they created) even if they fail
- Song listing should show which Artist they belong to - Django easily lets you should 1 step relationships (song-album and album-song) but 2 step (song-artist) would be harder to add.
- If the song file is incorrectly formatted the error message should say which row is at fault and why. (Currently there is just a generic error message for any problem)
- Validate the uploaded data. I.e. check that an Albums year of release is exactly 4 digits and a songs length is of the correct format (a custom data type could be used for this) 
