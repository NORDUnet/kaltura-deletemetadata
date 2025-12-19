# Delete user metadata
This code lets you search and delete user metadata in Kaltura

## Requirements
- Kaltura Session or kaltura partner id and admin secret
- Python3  (tested on 3.8.5)
- KalturaApiClient (tested on 15.14.0)

## Setup
Run `./setup-venv.sh` to setup the Python virtual environment.

## Usage
1. Run the program, etiher with Kaltura session directly:
    ./deletemetadata.sh <KS>
Or with no parameters and enter partner ID and admin secret:
    ./deletemetadata.sh
    Enter partner id: 123
    Enter admin secret: super-secret
4. When asked, enter `user id`
5. Answer **y** to delete user metadata, or **n** to skip.
6. If no user is found with `user id`, leave it empty and then enter `user
   email` and/or `full name` to search for user.
12. Press `ctrl+c` to exit program. You're done.
