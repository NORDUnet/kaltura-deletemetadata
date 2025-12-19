# Delete user metadata
This code lets you search and delete user metadata in Kaltura

## Requirements
- Kaltura Session or kaltura partner id and admin secret
- Python3  (tested on 3.8.5)
- KalturaApiClient (tested on 15.14.0)

## Setup
Run `./setup-venv.sh` to setup the Python virtual environment.

## Usage
Run the program, etiher with Kaltura session directly:
   
    $ ./deletemetadata.sh <KS>
    
Or with no parameters and enter partner ID and admin secret:

    $ ./deletemetadata.sh
    Enter partner id: 123
    Enter admin secret: super-secret

When asked, enter `user id`
If user is found, user info will be shown and all metadata object listed:

    Enter user ID: user@test.com
    
    ID: user@test.com
    Screenname: user@test.com
    Full name: Test User
    Email: user@test.com
    
    ID: 12
    XML: <metadata><role>privateOnlyRole</role></metadata>
    ID: 21
    XML: <?xml version="1.0"?>
    <metadata><Detail><Key>canvasUserToken</Key><Value>CanvasUserTokenKey==</Value></Detail></metadata>

    Delete metadata? (Y/n)

Answer **y** to delete user metadata, or **n** to skip.
If no user is found with `user id`, leave it empty and then enter `user email` and/or `full name` to search for user:

    Enter user ID:
    Enter user email: 
    Enter full name: Test User

Press `ctrl+c` to exit program. You're done.
