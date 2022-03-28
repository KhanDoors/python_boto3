import boto3

# https://www.youtube.com/watch?v=N3dIDz73J30&list=PL8tc66sMn9Kg05l6kvL_ujHKfaLi3fHLH&index=3

mng_cnsl = boto3.session.Session()

# print(dir(mng_cnsl))
print(mng_cnsl.available_profiles)
