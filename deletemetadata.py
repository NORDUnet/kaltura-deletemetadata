import KalturaClient
from KalturaClient.Plugins import Core as KalturaCore
from KalturaClient.exceptions import KalturaException


partnerId = input("Enter partner id: ")
adminSecret = input("Enter admin secret: ")

conf = KalturaClient.KalturaConfiguration()
conf.serviceUrl = "https://api.kaltura.nordu.net"

kc = KalturaClient.KalturaClient(conf)
kc.clientConfiguration['clientTag'] = 'metadata-deleter'
ks = kc.session.start(adminSecret, None, 2, partnerId)
kc.setKs(ks)
print(ks)


while True:
    users = []

    userId = input("Enter user ID: ")
    if userId != "":
        try:
            user = kc.user.get(userId)
        except KalturaException as err:
            if err.code == "INVALID_USER_ID":
                print("User not found")
                continue
            else:
                raise err
        users.append(user)
    else:
        email = input("Enter user email: ")
        fullname = input("Enter full name: ")
        names = fullname.split(" ")

        userFilter = KalturaCore.KalturaUserFilter()
        if email != "":
            userFilter.emailLike = email
        if fullname != "":
            userFilter.firstNameStartsWith = names[0]
            userFilter.lastNameStartsWith = names[-1]

        users = kc.user.list(userFilter).objects

    if len(users) == 0:
        print("User not found")
        continue

    for user in users:
        userId = user.id
        user = kc.user.get(userId=userId)
        print('')
        print(f'ID: {user.id}')
        print(f'Screenname: {user.screenName}')
        print(f'Full name: {user.fullName}')
        print(f'Email: {user.email}')

        filter = KalturaClient.Plugins.Metadata.KalturaMetadataFilter()
        filter.metadataObjectTypeEqual = KalturaClient.Plugins.Metadata.KalturaMetadataObjectType.USER
        filter.objectIdEqual = userId
        result = kc.metadata.metadata.list(filter, None)
        # print(kc.metadata.__dict__.keys())

        print('')
        if len(result.objects) > 0:
            for res in result.objects:
                print(f'ID: {res.id}')
                print(f'XML: {res.xml}')

            delete = input("Delete metadata? (Y/n) ")

            if delete.lower() == 'y' or delete == '':
                for res in result.objects:
                    print(f'deleting: {res.id}')
                    kc.metadata.metadata.delete(res.id)
        else:
            print("No metadata found")

        print('')
        print('')
