# Delete user metadata
This code lets you search and delete user metadata in Kaltura

## Requirements  
Kaltura partner id  
Kaltura admin secret  
Python3  (tested on 3.8.5)  
KalturaApiClient (tested on 15.14.0)  

## Setup
Install stuff

## Usage  
1. Run the program: `python3 deletemetadata.py`  
2. When asked, enter `kaltura partner id`  
3. When asked, enter `kaltura admin secret`  
4. When asked, enter `user id`  
5. Answer **y** to delete user metadata
6. You will be asked to  enter `user id` once again. This time leave it empty.  
7. When asked, enter `user email`  
8. Answer **y** to delete user metadata  
9. You will be asked to  enter `user id` and `user email` once again. Leave both empty.
10. When asked, enter `full name`
11. Answer **y** to delete user metadata  
12. Press `ctrl+c` to exit program. You're done.
